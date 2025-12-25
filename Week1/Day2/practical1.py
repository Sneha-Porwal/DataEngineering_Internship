import pandas as pd

class DataExtractor:
    def read_csv(self, filename):
        return pd.read_csv(filename)

    def csv_to_json(self, data, json_file):
        data.to_json(json_file, orient="records", indent=4)

    def read_json(self, filename):
        return pd.read_json(filename)


# Object creation
extractor = DataExtractor()
csv_data = extractor.read_csv("restaurants.csv")
extractor.csv_to_json(csv_data, "restaurants.json")
json_data = extractor.read_json("restaurants.json")

# Output
print("CSV Data:")
print(csv_data)

print("\nJSON Data:")
print(json_data)
