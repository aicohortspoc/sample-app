import os
import json
from main import read_csv_file, write_json_file, INPUT_CSV, OUTPUT_JSON
from sample_data_generator import generate_sample_csv

def test_generate_and_process_csv():
    generate_sample_csv()
    assert os.path.exists(INPUT_CSV), "Sample CSV was not created"

    data = read_csv_file(INPUT_CSV)
    assert isinstance(data, list) and len(data) > 0, "Data not read correctly from CSV"

    write_json_file(data, OUTPUT_JSON)
    assert os.path.exists(OUTPUT_JSON), "JSON output file was not created"

    with open(OUTPUT_JSON) as f:
        json_data = json.load(f)
    assert json_data[0]["FirstName"] == "John", "JSON content not written properly"
