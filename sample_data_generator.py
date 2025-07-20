import csv
import os

DATA_FOLDER = "data"
INPUT_CSV = os.path.join(DATA_FOLDER, "customers.csv")

def generate_sample_csv():
    """
    Creates a sample customer CSV file with 10 fields.
    """
    os.makedirs(DATA_FOLDER, exist_ok=True)
    sample_data = [
        ["CustomerID", "FirstName", "LastName", "Email", "Phone", "Address", "City", "State", "ZipCode", "Country"],
        ["1", "John", "Doe", "john.doe@example.com", "1234567890", "123 Elm St", "New York", "NY", "10001", "USA"],
        ["2", "Jane", "Smith", "jane.smith@example.com", "2345678901", "456 Oak St", "Los Angeles", "CA", "90001", "USA"],
        ["3", "Alice", "Brown", "alice.brown@example.com", "3456789012", "789 Pine St", "Chicago", "IL", "60601", "USA"]
    ]
    with open(INPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    print(f"Sample CSV file created at {INPUT_CSV}")
    