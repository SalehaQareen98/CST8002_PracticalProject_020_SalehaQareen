"""
CST8002 Programming Language Research - Practical Project Part 1
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda 
Date: 2026-02-01

Dataset: Pacific Rim Native Amphibians (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Y. Zharikov, “Black Oystercatcher Population – Pacific Rim – Open Government Portal,” Canada.ca. [Online]. Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02 [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (2024, Dec. 15). Python Documentation Contents. Python 3.13.11 Documentation. [Online]. Available: https://docs.python.org/3.13/contents.html [Accessed: Jan. 30, 2026].
[3] Python Software Foundation. (2024, Dec. 15). Built-in Functions and Methods. Python Standard Library. [Online]. Available: https://docs.python.org/3/library/functions.html [Accessed: Jan. 30, 2026].
[4] Python Software Foundation. (2024, Dec. 15). Data Types That Support Iterators. Python HOWTO – Functional Programming. [Online]. Available: https://docs.python.org/3/howto/functional.html [Accessed: Jan. 30, 2026].
[5] Python Software Foundation. (2024, Dec. 15). Input and Output. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/inputoutput.html [Accessed: Jan. 30, 2026].
[6] Python Software Foundation. (2024, Dec. 15). Exceptions. Python Language Reference. [Online]. Available: https://docs.python.org/3.11/reference/executionmodel.html#exceptions [Accessed: Jan. 30, 2026].
[7] Python Software Foundation. (2024, Dec. 15). The Python Standard Library. Python Standard Library Reference. [Online]. Available: https://docs.python.org/3.11/library/ [Accessed: Jan. 30, 2026].
[8] Python Software Foundation. (2024, Dec. 15). array — Efficient Arrays of Numeric Values. Python Standard Library. [Online]. Available: https://docs.python.org/3/library/array.html [Accessed: Jan. 30, 2026].
[9] Python Software Foundation. (2024, Dec. 15). Reading and Writing Files. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files [Accessed: Jan. 29, 2026].

"""
import csv
from oystercatcher_record import OystercatcherRecord

print("\n=== Saleha Qareen - Practical Project 1 ===")

"""
csv_path:
Constant that stores the absolute file path to the CSV dataset.
"""
csv_path = r"C:\Users\saleh\Documents\Level 6\python\CST8002_PracticalProject_020_SalehaQareen\pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"

"""
records:
List (array) used to store OystercatcherRecord objects.
"""
records = []  # array / list to store record objects

# Implement exception handling for missing or inaccessible dataset file
try:
    """
    Opens the CSV file and reads dataset contents using File-I/O.
    """
    with open(csv_path, newline="", encoding="latin-1") as file:
        reader = csv.DictReader(file)

        """
        Loop used to process the first few records from the dataset.
        """
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
    """
    Handles missing or inaccessible dataset files.
    """
    print("Error: Dataset file not found or inaccessible.")

except KeyError as e:
    """
    Handles missing or incorrect column names in the dataset.
    """
    print(f"Error: Missing expected column in dataset: {e}")

"""
Loop used to output record data to the screen.
"""
for record in records:
    print(record)
