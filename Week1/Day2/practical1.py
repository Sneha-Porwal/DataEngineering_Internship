import csv
import json

class DataExtractor:

    def read_csv(self, file_path):
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = []

            for row in reader:
                data.append(row)

        return header, data

    def read_json(self, file_path):
        with open(file_path) as f:
            return json.load(f)


# Example usage
extractor = DataExtractor()
header, data = extractor.read_csv("restaurants.csv")
print(header)
print(data[0])
