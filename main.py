import os
import json
import csv
import argparse
from sample_data_generator import generate_sample_csv

DATA_FOLDER = "data"
INPUT_CSV = os.path.join(DATA_FOLDER, "customers.csv")
OUTPUT_JSON = os.path.join(DATA_FOLDER, "output.json")

def read_csv_file(file_path, filter_column=None, filter_value=None):
    """
    Reads a CSV file into a list of dictionaries.
    If filter_column and filter_value are provided, only matching rows are returned.
    """
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    if filter_column and filter_value:
        filtered = [
            row for row in data
            if row.get(filter_column, "").lower() == filter_value.lower()
        ]
        print(f"Filtered {len(filtered)} records by {filter_column} = {filter_value}")
        return filtered

    print(f"Read {len(data)} records from {file_path}")
    return data

def write_json_file(data, file_path):
    """
    Writes list of dictionaries to a JSON file.
    """
    with open(file_path, mode='w') as file:
        json.dump(data, file, indent=4)
    print(f"Output written to JSON at {file_path}")

def parse_arguments():
    """
    Set up CLI arguments and return parsed args.
    """
    parser = argparse.ArgumentParser(description="Process customer CSV to JSON")
    parser.add_argument("--generate", action="store_true", help="Generate sample CSV file")
    parser.add_argument("--read", action="store_true", help="Read CSV file")
    parser.add_argument("--write", action="store_true", help="Write data to JSON file")
    parser.add_argument("--filter-column", type=str, help="Column name to filter by")
    parser.add_argument("--filter-value", type=str, help="Value to filter on")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    customers = []

    if args.generate:
        generate_sample_csv()

    if args.read:
        if not os.path.exists(INPUT_CSV):
            print(f"Error: {INPUT_CSV} not found. Use --generate to create a sample file.")
        else:
            customers = read_csv_file(
                INPUT_CSV,
                filter_column=args.filter_column,
                filter_value=args.filter_value
            )

    if args.write:
        if not customers:
            print("Error: No data to write. Use --read and optionally --filter-column and --filter-value.")
        else:
            write_json_file(customers, OUTPUT_JSON)
