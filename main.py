# main.py
# Author: Saleha Qareen

import csv
from oystercatcher_record import OystercatcherRecord

print("Program Author: Saleha Qareen\n")

csv_path = r"C:\Users\saleh\Documents\Level 6\python\CST8002_PracticalProject_020_SalehaQareen\pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"

records = []  # array / list to store record objects

# Implement exception handling for missing or inaccessible dataset file
try:
    # Implement File I/O to open and read the CSV dataset at program startup
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        # Parse dataset records into individual data fields
        for row in reader:
            record = OystercatcherRecord(
                row["Visit date"],
                row["Site identification"],
                row["Species"],
                row["Total Black oystercatcher adults"]
            )
            # Store record objects in an array or list data structure
            records.append(record)

except FileNotFoundError:
    print("Error: Dataset file not found or inaccessible.")
except KeyError as e:
    print(f"Error: Missing expected column in dataset: {e}")


