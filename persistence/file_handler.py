# persistence/file_handler.py
"""
@author: Saleha Qareen (041161192)
@date: 2026-02-15
Handles file reading and writing for OystercatcherRecord objects.
References:
[1] Y. Zharikov, “Black Oystercatcher Population – Pacific Rim – Open Government Portal,” Canada.ca. [Online]. Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02 [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (2026, Feb. 14). uuid — UUID objects according to RFC 4122. docs.python.org. [Online]. Available: https://docs.python.org/3/library/uuid.html [Accessed: Feb. 15, 2026].
[3] Python Software Foundation. (2024, Dec. 15). Reading and Writing Files. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files [Accessed: Jan. 29, 2026].
"""

import csv
import uuid
from model.oystercatcher_record import OystercatcherRecord

class FileHandler:
    """Class responsible for loading and saving dataset records."""

    def load_records(self, file_path: str) -> list[OystercatcherRecord]:
        """
        Reads dataset CSV and returns a list of OystercatcherRecord objects.

        Only handles FileNotFoundError as required.

        Parameters:
            file_path (str): Path to the CSV dataset file.

        Returns:
            List[OystercatcherRecord]: List containing up to 100 records.
        """
        records = []
        # Implement exception handling for missing or inaccessible dataset file
        try:
            with open(file_path, newline="", encoding="latin-1") as file:
                reader = csv.DictReader(file)
                # Skip the French header row
                for row in reader:
                    if row["Visit date"] == "Date de la visite":
                        continue

                    record = OystercatcherRecord(
                        visit_date=row["Visit date"],
                        site_identification=row["Site identification"],
                        species=row["Species"],
                        total_black_oystercatcher_adults=row["Total Black oystercatcher adults"]
                    )
                    records.append(record)
                    # Store record objects in an array or list data structure and limit to 100 records
                    if len(records) >= 100:
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

        return records

    def save_records(self, records: list[OystercatcherRecord]) -> str:
        """
        Saves a list of OystercatcherRecord objects to a new CSV file with a UUID filename.

        Returns the filename; no print statements are included here to stay strictly
        compliant with layered architecture requirements.
        """
        filename = f"oystercatcher_output_{uuid.uuid4()}.csv"

        with open(filename, "w", newline="", encoding="latin-1") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Visit date",
                "Site identification",
                "Species",
                "Total Black oystercatcher adults"
            ])
            for record in records:
                writer.writerow([
                    record.visit_date,
                    record.site_identification,
                    record.species,
                    record.total_black_oystercatcher_adults
                ])

        # Return filename to presentation layer 
        return filename
