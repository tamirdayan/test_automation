import json
import requests


get_url = "http://localhost:9000/student/list"
response = requests.get(get_url)
response_json = response.json()

post_url = "http://localhost:9000/student"
header = {'Content-type': 'application/json'}


def test_get_students():
    for student in response_json:
        print("\nid: ", student["id"])
        print("firstName: ", student["firstName"])
        print("lastName:  ", student["lastName"])


def test_post_student():
    payload = {'firstName' : 'Tamir', 'lastName' : 'Dayan', 'email' : 'tamir@ridewithvia.com', 'programme': 'Psychology'}
    response = requests.post(post_url, json=payload, headers=header)
    response_json = response.json()
    print("response code: ", response)
    print("response body: ", response_json)
    assert(response.status_code == 201)


def test_put_student_with_courses():
    id = '/101'
    payload = {'firstName' : 'Tamir', 'lastName' : 'Dayan', 'email' : 'tamir@ridewithvia.com', 'programme': 'Psychology', 'courses' : ["Java Course", "CSharp Course", "Python Course"]}
    response = requests.put(post_url + id, json=payload, headers=header)
    response_json = response.json()
    print("response code: ", response)
    print("response body: ", response_json)
    assert(response.status_code == 200)


def test_delete_student():
    id = '/101'
    response = requests.delete(post_url + id)
    print(response)
