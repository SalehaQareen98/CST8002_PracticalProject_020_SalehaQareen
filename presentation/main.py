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

from business.record_manager import RecordManager
from model.oystercatcher_record import OystercatcherRecord

def display_full_name():
 print("\n=== Saleha Qareen - Practical Project 2 ===")

def main():
    manager = RecordManager()
    csv_path = r"data/pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"

    while True:
        display_full_name()
        print("=== Black Oystercatcher Data Management ===")
        print("1. Reload dataset")
        print("2. Save dataset to new CSV (UUID)")
        print("3. Display a single record")
        print("4. Display all records")
        print("5. Add new record")
        print("6. Edit a record")
        print("7. Delete a record")
        print("8. Exit")

        choice = input("Select an option (1-8): ")
        # Reload dataset from CSV file and handle exceptions for missing or inaccessible files
        if choice == "1":
            try:
                manager.reload_data(csv_path)
                print("Dataset reloaded successfully.")
            except Exception as e:
                print(f"Error reloading dataset: {e}")
                
        elif choice == "2":
            # Persist in-memory data to new CSV file using UUID for filename and handle exceptions for file writing issues
            filename = manager.save_data()
            print(f"Data saved to new file: {filename}")

        elif choice == "3":
            # TODO: select and display single record
            print("[Placeholder] Display single record functionality")

        elif choice == "4":
            # TODO: select and display multiple records
            print("[Placeholder] Display all records functionality")

        elif choice == "5":
            # TODO: create new record
            print("[Placeholder] Add new record functionality")

        elif choice == "6":
            # TODO: edit a record
            print("[Placeholder] Edit record functionality")

        elif choice == "7":
            # TODO: delete a record
            print("[Placeholder] Delete record functionality")

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please select 1-8.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
