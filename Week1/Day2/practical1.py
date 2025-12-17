import csv
import json

class DataExtractor:
    def read_csv(self, file_path):
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def read_json(self, file_path):
        with open(file_path) as file:
            return json.load(file)
