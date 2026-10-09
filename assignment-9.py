import csv
import json

input_file = "input.csv"
output_file = "output.json"

# Read data from the CSV file
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Write data to the JSON file
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV data converted to JSON successfully.")
