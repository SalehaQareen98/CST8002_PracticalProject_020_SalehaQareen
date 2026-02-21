"""
CST8002 Programming Language Research - Practical Project Part 2
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda 
Date: 2026-02-20

Dataset: Black Oystercatcher Population – Pacific Rim (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Parks Canada. (Oct 1, 2017). Black Oystercatcher Population – Pacific Rim. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02  [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (n.d). Python Documentation Contents. docs.python.org. [Online]. Available: https://docs.python.org/3.13/contents.html [Accessed: Jan. 30, 2026].
[3] Python Software Foundation. (n.d). Built-in Functions and Methods. docs.python.org. [Online]: https://docs.python.org/3/library/functions.html [Accessed: Jan. 30, 2026].
[4] Python Software Foundation. (n.d). Data Types That Support Iterators. docs.python.org. [Online]. Available: https://docs.python.org/3/howto/functional.html [Accessed: Jan. 30, 2026].
[5] Python Software Foundation. (n.d). Built-in Types — list. docs.python.org. [Online]. Available: https://docs.python.org/3/library/stdtypes.html#list [Accessed: Feb. 20, 2026].

"""
from persistence.file_handler import FileHandler
from model.oystercatcher_record import OystercatcherRecord
from typing import List, Optional


class RecordManager:
    """
    Business Layer for managing OystercatcherRecord objects in memory.

    Responsibilities:
    - Store records in a sequential data structure (list)
    - Provide operations to reload, select, add, edit, and delete records
    - Work with Persistence Layer for file operations
    """

    def __init__(self):
        self.records: List[OystercatcherRecord] = []
        self.file_handler = FileHandler()

    def reload_data(self, file_path: str) -> None:
        """
        Reloads data from CSV file using Persistence Layer, replacing current records.
        """
        self.records = self.file_handler.load_records(file_path)

    def get_all_records(self) -> List[OystercatcherRecord]:
        """
        Returns all records in memory.
        """
        return self.records

    def get_record(self, index: int) -> Optional[OystercatcherRecord]:
        """
        Returns a single record by index, or None if index is invalid.
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

    def add_record(self, record: OystercatcherRecord) -> None:
        """
        Adds a new record to the in-memory list.
        """
        self.records.append(record)

    def edit_record(self, index: int, updated_record: OystercatcherRecord) -> bool:
        """
        Updates an existing record at the given index.
        Returns True if successful, False if index is invalid.
        """
        if 0 <= index < len(self.records):
            self.records[index] = updated_record
            return True
        return False

    def delete_record(self, index: int) -> bool:
        """
        Deletes a record at the given index.
        Returns True if successful, False if index is invalid.
        """
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        return False

    def save_data(self) -> str:
        """
        Saves current in-memory records to a new CSV file using Persistence Layer.
        Returns the filename generated.
        """
        return self.file_handler.save_records(self.records)
