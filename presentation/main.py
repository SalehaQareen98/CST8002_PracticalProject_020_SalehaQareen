"""
CST8002 Programming Language Research - Practical Project Part 3
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda
Due Date: 2026-03-29

Dataset: Black Oystercatcher Population – Pacific Rim (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Parks Canada. (Oct 1, 2017). Black Oystercatcher Population – Pacific Rim. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02  [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (n.d). Python Documentation Contents. Python 3.13.11 Documentation. [Online]. Available: https://docs.python.org/3.13/contents.html [Accessed: Jan. 30, 2026].
[3] Python Software Foundation. (n.d). Built-in Functions and Methods. Python Standard Library. [Online]. Available: https://docs.python.org/3/library/functions.html [Accessed: Jan. 30, 2026].
[4] Python Software Foundation. (n.d). Data Types That Support Iterators. Python HOWTO – Functional Programming. [Online]. Available: https://docs.python.org/3/howto/functional.html [Accessed: Jan. 30, 2026].
[5] Python Software Foundation. (n.d). Input and Output. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/inputoutput.html [Accessed: Jan. 30, 2026].
[6] Python Software Foundation. (n.d). Exceptions. Python Language Reference. [Online]. Available: https://docs.python.org/3.11/reference/executionmodel.html#exceptions [Accessed: Jan. 30, 2026].
[7] Python Software Foundation. (n.d). The Python Standard Library. Python Standard Library Reference. [Online]. Available: https://docs.python.org/3.11/library/ [Accessed: Jan. 30, 2026].
[8] Python Software Foundation. (n.d). Reading and Writing Files. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files [Accessed: Jan. 29, 2026].
[9] Python Software Foundation. (n.d). Built-in Types — list. docs.python.org. [Online]. Available: https://docs.python.org/3/library/stdtypes.html#list [Accessed: Feb. 20, 2026].
"""

from business.record_manager import RecordManager
from model.oystercatcher_record import OystercatcherRecord

def display_full_name():
    """
    Displays the program author's full name.

    This ensures the student's name remains visible during
    user interaction and program output, as required in
    Practical Project Part 2 documentation guidelines.
    """
    print("\n=== Saleha Qareen - Practical Project 4 ===")

def main():
    """
    Main entry point of the Presentation Layer.

    Responsibilities:
    - Displays interactive menu options
    - Handles user input
    - Calls Business Layer methods
    - Displays results to the user

    All file operations and data storage logic are delegated
    to the appropriate layers to maintain N-Layered architecture.
    """
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
        print("8. Sort records using multiple columns")
        print("9. Exit")

        choice = input("Select an option (1-9): ")
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
            # Select and display a single record by index, handling invalid index input
            try:
                index = int(input("Enter record index: "))
                record = manager.get_record(index)

                if record is not None:
                    print("\nRecord found:")
                    print(record)
                else:
                    print("Invalid index. Record not found.")

            except ValueError:
                print("Please enter a valid integer index.")
                
        elif choice == "4":
            # Select and display multiple records
            records = manager.get_all_records()

            if len(records) == 0:
                print("No records in memory. Reload dataset first.")
            else:
                for i, record in enumerate(records):
                    if i % 10 == 0:
                        display_full_name()  # keeps your name visible in long outputs
                    print(f"[{i}] {record}")
                        
        elif choice == "5":
            visit_date = input("Enter Visit date:[DD/MM/YYYY] ")
            site_identification = input("Enter Site identification: ")
            species = input("Enter Species: ")
            total_black_oystercatcher_adults = input("Enter Total Black oystercatcher adults: ")

            new_record = OystercatcherRecord(
                visit_date=visit_date,
                site_identification=site_identification,
                species=species,
                total_black_oystercatcher_adults=total_black_oystercatcher_adults
            )

            manager.add_record(new_record)
            print("New record added to memory.")

        elif choice == "6":
            try:
                index = int(input("Enter record index to edit: "))
                existing = manager.get_record(index)

                if existing is None:
                    print("Invalid index. Record not found.")
                else:
                    print("Enter new values:")

                    visit_date = input(f"Visit date [{existing.visit_date}]: ")
                    site_identification = input(f"Site identification [{existing.site_identification}]: ")
                    species = input(f"Species [{existing.species}]: ")
                    total_adults = input(f"Total Black oystercatcher adults [{existing.total_black_oystercatcher_adults}]: ")
                    
                    updated_record = OystercatcherRecord(
                        visit_date = visit_date,
                        site_identification = site_identification,
                        species = species,
                        total_black_oystercatcher_adults = total_adults
                    )

                    success = manager.edit_record(index, updated_record)
                    if success:
                        print("Record updated successfully.")
                    else:
                        print("Record update failed.")

            except ValueError:
                print("Please enter a valid integer index.")

        elif choice == "7":
            try:
                index = int(input("Enter record index to delete: "))
                success = manager.delete_record(index)

                if success:
                    print("Record deleted successfully.")
                else:
                    print("Invalid index. Record not found.")

            except ValueError:
                print("Please enter a valid integer index.")

        elif choice == "8":
            print("\nSort by selecting two columns from the dataset:")
            print("1. Visit date")
            print("2. Site identification")
            print("3. Species")
            print("4. Total Black oystercatcher adults")

            column_map = {
                "1": "Visit date",
                "2": "Site identification",
                "3": "Species",
                "4": "Total Black oystercatcher adults"
            }

            primary_choice = input("Select primary sort column (1-4): ")
            secondary_choice = input("Select secondary sort column (1-4): ")

            primary_column = column_map.get(primary_choice)
            secondary_column = column_map.get(secondary_choice)

            if primary_column is None or secondary_column is None:
                print("Invalid column selection. Please choose options 1-4.")
            else:
                try:
                    sorted_records = manager.sort_records(primary_column, secondary_column)

                    if len(sorted_records) == 0:
                        print("No records in memory. Reload dataset first.")
                    else:
                        print(f"\nRecords sorted by {primary_column} and then {secondary_column}:\n")
                        for i, record in enumerate(sorted_records):
                            if i % 10 == 0:
                                display_full_name()
                            print(f"[{i}] {record}")

                except ValueError as e:
                    print(f"Sorting error: {e}")

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please select 1-9.")

if __name__ == "__main__":
    main()
