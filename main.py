import os
import json
import csv
import argparse
from sample_data_generator import generate_sample_csv

DATA_FOLDER = "data"
INPUT_CSV = os.path.join(DATA_FOLDER, "customers.csv")
OUTPUT_JSON = os.path.join(DATA_FOLDER, "output.json")

def read_csv_file(file_path, filters=None):
    customers = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if filters:
                if not all(row.get(k) == v for k, v in filters.items()):
                    continue
            customers.append(row)
    return customers

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
