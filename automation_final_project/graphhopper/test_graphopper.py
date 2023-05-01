import allure
import csv
import logging
import numpy as np
import pytest
import random
import requests
import subprocess
import time

# TODO logger
# todo more tests

API_URL = "http://localhost:8989/route"
API_KEY = "a395ba03-722e-476a-bec8-4642beb0e763"
API_QUERY = {
    "profile": "car",
    "point": "string",
    "point_hint": "string",
    "snap_prevention": "string",
    "curbside": "any",
    "locale": "en",
    "elevation": "false",
    "details": "string",
    "optimize": "false",
    "instructions": "true",
    "calc_points": "true",
    "debug": "false",
    "points_encoded": "true",
    "ch.disable": "false",
    "heading": "0",
    "heading_penalty": "120",
    "pass_through": "false",
    "algorithm": "round_trip",
    "round_trip.distance": "10000",
    "round_trip.seed": "0",
    "alternative_route.max_paths": "2",
    "alternative_route.max_weight_factor": "1.4",
    "alternative_route.max_share_factor": "0.6",
    "key": "a395ba03-722e-476a-bec8-4642beb0e763"
}
DOWNLOAD_GRAPHHOPPER_LOCAL_SERVER_FILES_TERMINAL_COMMAND = """wget https://repo1.maven.org/maven2/com/graphhopper
/graphhopper-web/7.0/graphhopper-web-7.0.jar https://raw.githubusercontent.com/graphhopper/graphhopper/7.x/config
-example.yml http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf """
SETUP_GRAPHHOPPER_LOCAL_SERVER_TERMINAL_COMMAND = """java -D"dw.graphhopper.datareader.file=berlin-latest.osm.pbf" -jar graphhopper*.jar server config-example.yml"""
STATUS_400_ONE_POINT_ERROR_MESSAGE = r'{"message":"At least 2 points have to be specified, but was:1","hints":[{"message":"At least 2 points have to be specified, but was:1","details":"java.lang.IllegalArgumentException"}]}'
MIN_SPEED_IN_KM_H = 30
MAX_SPEED_IN_KM_H = 140


def create_csv_locations_of_berlin():
    lat_range = (52.462256, 52.567321)
    lng_range = (13.294987, 13.521670)
    np.random.seed(42)
    locations = [(np.random.uniform(lat_range[0], lat_range[1]),
                  np.random.uniform(lng_range[0], lng_range[1])) for _ in range(20000)]
    with open('berlin_locations.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for lat, lng in locations:
            writer.writerow([lat, lng])


def get_data_from_csv():
    with open("berlin_locations.csv", newline='') as f:
        reader = csv.reader(f)
        locations_list = [tuple(row) for row in reader]
        return locations_list


def wait_for_server(url, retries=300, interval=1):
    """Wait for a server to be up and running.

        Args:
            url (str): The URL to check.
            retries (int, optional): The number of retries to make. Defaults to 300.
            interval (int, optional): The interval between retries in seconds. Defaults to 1.

        Raises:
            TimeoutError: If the server doesn't respond within the given number of retries.
        """
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return
        except requests.exceptions.RequestException:
            pass
        time.sleep(interval)
    raise TimeoutError(f"Server did not respond after {retries} retries.")


class Test_Graphhopper:
    locations = []
    download_files_process = None
    start_server_process = None

    # @pytest.fixture(scope="class", autouse=True)
    @classmethod
    def setup_class(cls):
        create_csv_locations_of_berlin()
        Test_Graphhopper.locations = get_data_from_csv()
        cls.download_files_process = subprocess.Popen(DOWNLOAD_GRAPHHOPPER_LOCAL_SERVER_FILES_TERMINAL_COMMAND,
                                                      shell=True)
        cls.download_files_process.wait()
        cls.start_server_process = subprocess.Popen(SETUP_GRAPHHOPPER_LOCAL_SERVER_TERMINAL_COMMAND, shell=True)
        wait_for_server("http://localhost:8989")
        print("Local server has started!")

    @classmethod
    def teardown_class(cls):
        cls.start_server_process.kill()
        cls.start_server_process.wait()

    @allure.title("getRoute: 200 OK Routing Result")
    @allure.description("This test gets the route between two points. "
                        "Verifies a path exists between the two points.")
    def test_get_route_exists(self):
        for loc1, loc2 in zip(Test_Graphhopper.locations[:-1], Test_Graphhopper.locations[1:]):
            params = {
                'point': [f'{loc1[0]},{loc1[1]}', f'{loc2[0]},{loc2[1]}'],
                'profile': 'car',
                'key': API_KEY
            }
            response = requests.get(API_URL, params=params)
            if response.status_code == 429:
                pytest.fail("API key limit reached, stopping the test. "
                            "Status code: {response.status_code}"
                            "Reason: {response.reason}")
            assert response.status_code == 200
            assert response.reason == 'OK'
            assert len(response.json()['paths']) > 0

    @allure.title("getRoute: 400 Request Not Valid")
    @allure.description(
        "This test gets a request with a single point, and expects status 400: Your request is not valid.")
    def test_get_route_single_point(self):
        params = {
            'point': [f'{Test_Graphhopper.locations[0][0]},{Test_Graphhopper.locations[0][1]}'],
            'profile': 'car',
            'key': API_KEY
        }
        response = requests.get(API_URL, params=params)
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.text == STATUS_400_ONE_POINT_ERROR_MESSAGE

    @allure.title("getRoute: Response Structure")
    @allure.description("This test gets the route between two points. "
                        "Verifies the response structure consists of the fields \"info\", \"paths\", \"distance\", "
                        "\"time\", \"ascend\", \"descend\", \"points\", \"snapped_waypoints\", \"points_encoded\", "
                        "\"bbox\", \"instructions\" and \"details\".")
    def test_get_route_response_structure(self):
        params = {
            'point': [f'{Test_Graphhopper.locations[0][0]},{Test_Graphhopper.locations[0][1]}',
                      f'{Test_Graphhopper.locations[1][0]},{Test_Graphhopper.locations[1][1]}'],
            'profile': 'car',
            'key': API_KEY
        }
        response = requests.get(API_URL, params=params)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert 'info' in response.json()
        assert 'paths' in response.json()
        assert 'distance' in response.json()['paths'][0]
        assert 'time' in response.json()['paths'][0]
        assert 'ascend' in response.json()['paths'][0]
        assert 'descend' in response.json()['paths'][0]
        assert 'points' in response.json()['paths'][0]
        assert 'snapped_waypoints' in response.json()['paths'][0]
        assert 'points_encoded' in response.json()['paths'][0]
        assert 'bbox' in response.json()['paths'][0]
        assert 'instructions' in response.json()['paths'][0]
        assert 'details' in response.json()['paths'][0]

    @allure.title("getRoute: Detect Suspicious Routes")
    @allure.description("This test detects suspicious routes where the duration does not match the distance.")
    def test_detect_suspicious_routes(self):
        params = {
            'point': [f'{Test_Graphhopper.locations[0][0]},{Test_Graphhopper.locations[0][1]}',
                      f'{Test_Graphhopper.locations[1][0]},{Test_Graphhopper.locations[1][1]}'],
            'profile': 'car',
            'key': API_KEY
        }
        response = requests.get(API_URL, params=params)
        assert response.status_code == 200
        assert 'paths' in response.json()
        path = response.json()['paths'][0]
        distance_in_kilometers = path['distance'] / 1000  # convert from meters to kilometers
        time_in_hours = path['time'] / (1000 * 60 * 60)  # convert from milliseconds to hours
        speed_km_per_hour = distance_in_kilometers / time_in_hours
        assert MIN_SPEED_IN_KM_H < speed_km_per_hour <= MAX_SPEED_IN_KM_H
