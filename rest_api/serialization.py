import csv
import json
import yaml
import xml.etree.cElementTree as ET


class Test_Serialization:
    csv_header = ['name', 'age', 'location', 'phone']
    csv_data = ['Tamir', 29, 'TLV', 'iPhone 14 Pro']
    flat_data = {
        "Name": "Tamir",
        "Age": "29",
        "Location": "TLV",
        "Phone": "iPhone 14 Pro"}
    json_data = {"employees": [
        {"firstName": "Tamir", "lastName": "Dayan"},
        {"firstName": "Shay", "lastName": "Kober"},
    ]}
    yaml_data = {'Record-1': {'name': 'Yoni Flenner', 'job': 'Developer', 'skill' : 'None'}}

    def test_data_repr(self):
        print(repr(self.flat_data))

    def test_data_csv_write(self):
        with open('file.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_header)
            writer.writerow(self.csv_data)

    def test_data_csv_read(self):
        with open('file.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def test_data_json_write(self):
        with open('jsonfile.json', 'w') as file:
            json.dump(self.json_data, file, sort_keys=True)

    def test_data_json_read(self):
        with open('jsonfile.json', 'r') as file:
            json_data = json.load(file)
            print(json_data)

    def test_data_yaml_write(self):
        with open('file.yml', 'w') as yaml_file:
            yaml.dump(self.yaml_data, yaml_file, default_flow_style=False)

    def test_data_yaml_read(self):
        with open('file.yml', 'r', newline='') as yaml_file:
            try:
                print(yaml.safe_load(yaml_file))
            except yaml.YAMLError as ymelexception:
                print(ymelexception)

