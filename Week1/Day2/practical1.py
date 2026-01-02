import pandas as pd

class DataExtractor:
    def read_file(self, filename):
        if filename.endswith(".csv"):
            return pd.read_csv(filename)
        elif filename.endswith(".json"):
            return pd.read_json(filename)
        else:
            raise ValueError("Unsupported file format")

    def csv_to_json(self, data, json_file):
        data.to_json(json_file, orient="records", indent=4)

    def sort_data(self, data, column):
        return data.sort_values(by=column)


extractor = DataExtractor()
csv_data = extractor.read_file("restaurants.csv")
extractor.csv_to_json(csv_data, "restaurants.json")
json_data = extractor.read_file("restaurants.json")
sorted_data = extractor.sort_data(csv_data, "restaurant_name")

print("CSV Data:")
print(csv_data)

print("\nSorted Data:")
print(sorted_data)

print("\nJSON Data:")
print(json_data)


'''import pandas as pd

class DataExtractor:
    def process_data(self, csv_file, json_file, sort_column):
        # Read CSV
        csv_data = pd.read_csv(csv_file)

        # Sort data
        sorted_data = csv_data.sort_values(by=sort_column)

        # Convert to JSON
        sorted_data.to_json(json_file, orient="records", indent=4)

        # Read JSON
        json_data = pd.read_json(json_file)

        return csv_data, sorted_data, json_data

# Object creation
extractor = DataExtractor()

csv_data, sorted_data, json_data = extractor.process_data(
    "restaurants.csv",
    "restaurants.json",
    "restaurant_name"
)

# Output
print("CSV Data:")
print(csv_data)

print("\nSorted Data:")
print(sorted_data)

print("\nJSON Data:")
print(json_data) '''
