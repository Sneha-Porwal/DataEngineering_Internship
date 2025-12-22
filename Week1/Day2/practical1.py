import csv
import json

class DataExtractor:
    def read_csv(self, file_path):
        data = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def read_json(self, file_path):
        with open(file_path, mode='r') as file:
            data = json.load(file)
        return data


# Object creation
extractor = DataExtractor()

# Correct file names
csv_data = extractor.read_csv("restaurants.csv")
json_data = extractor.read_json("restaurants.json")

print("CSV Data:")
print(csv_data)

print("\nJSON Data:")
print(json_data)
