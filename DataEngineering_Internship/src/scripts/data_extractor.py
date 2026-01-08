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
