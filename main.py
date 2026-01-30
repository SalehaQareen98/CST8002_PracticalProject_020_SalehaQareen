"""
CST8002 Programming Language Research - Practical Project Part 1
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda 
Date: 2026-02-01

Dataset: Pacific Rim Native Amphibians (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]
[1]Y. Zharikov, “Black Oystercatcher Population - Pacific Rim - Open Government Portal,” Canada.ca, 2024. https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02. [Accessed: Jan. 29, 2026].

References:
[1]Python Software Foundation, “7. Input and Output,” Python documentation, Jan. 29, 2026. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files [accessed Jan. 29, 2026].

"""
import csv
from oystercatcher_record import OystercatcherRecord

print("\n=== Saleha Qareen - Practical Project 1 ===")


csv_path = r"C:\Users\saleh\Documents\Level 6\python\CST8002_PracticalProject_020_SalehaQareen\pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"

records = []  # array / list to store record objects

# Implement exception handling for missing or inaccessible dataset file
try:
    # Implement File I/O to open and read the CSV dataset at program startup
    with open(csv_path, newline="", encoding="latin-1") as file:
        reader = csv.DictReader(file)

        # Initialize only first 5 records 
        for i, row in enumerate(reader):
            # Skip the French header row
            if row["Visit date"] == "Date de la visite":
                continue

            record = OystercatcherRecord(
                row["Visit date"],
                row["Site identification"],
                row["Species"],
                row["Total Black oystercatcher adults"]
            )
            # Store record objects in an array or list data structure
            records.append(record)

            if i == 5:  # stop after first 5 data rows
                break

except FileNotFoundError:
    print("Error: Dataset file not found or inaccessible.")
except KeyError as e:
    print(f"Error: Missing expected column in dataset: {e}")

# Loop to output record data on screen
for record in records:
    print(record)
