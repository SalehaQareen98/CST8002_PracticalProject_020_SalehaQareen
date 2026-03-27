"""
CST8002 Programming Language Research - Practical Project Part 3
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda
Due Date: 2026-03-29

Dataset: Black Oystercatcher Population – Pacific Rim (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Parks Canada. (Oct. 1, 2017). Black Oystercatcher Population – Pacific Rim. open.canada.ca.[Online].Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02 [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (n.d.). Python Documentation Contents. docs.python.org. [Online]. Available: https://docs.python.org/3.13/contents.html [Accessed: Jan. 30, 2026].
[3] Python Software Foundation. (n.d.). Built-in Functions and Methods. docs.python.org. [Online]. Available: https://docs.python.org/3/library/functions.html [Accessed: Jan. 30, 2026].
[4] Python Software Foundation. (n.d.). Data Types That Support Iterators. docs.python.org. [Online]. Available: https://docs.python.org/3/howto/functional.html [Accessed: Jan. 30, 2026].
[5] Python Software Foundation. (n.d.). Built-in Types — list. docs.python.org. [Online]. Available: https://docs.python.org/3/library/stdtypes.html#list [Accessed: Feb. 20, 2026].
[6] GeeksforGeeks. (2024, Jan. 10). Linked List Data Structure. geeksforgeeks.org [Online].Available: https://www.geeksforgeeks.org/data-structures/linked-list/ [Accessed: Mar. 11, 2026].
[7] Python Software Foundation. (n.d.). Data Structures. docs.python.org. [Online]. Available: https://docs.python.org/3/tutorial/datastructures.html [Accessed: Mar. 11, 2026].
[8] GeeksforGeeks. (2025, Jul. 15). Types of Linked List. geeksforgeeks.org [Online]. Available: https://www.geeksforgeeks.org/dsa/types-of-linked-list/ [Accessed: Mar. 11, 2026].
"""

from persistence.file_handler import FileHandler
from model.oystercatcher_record import OystercatcherRecord
from business.singly_linked_list import SinglyLinkedList
from typing import Optional


class RecordManager:
    """
    Business Layer for managing OystercatcherRecord objects in memory.

    Responsibilities:
    - Store records in a custom singly linked list
    - Provide operations to reload, select, add, edit, and delete records
    - Work with Persistence Layer for file operations
    """

    def __init__(self) -> None:
        """
        Initializes the RecordManager with an empty singly linked list
        and a file handler.
        """
        self.records = SinglyLinkedList()
        self.file_handler = FileHandler()

    def reload_data(self, file_path: str) -> None:
        """
        Reloads data from a CSV file using the Persistence Layer,
        replacing the current records in memory.

        Args:
            file_path: The path to the CSV file.
        """
        loaded_records = self.file_handler.load_records(file_path)
        self.records.clear()

        for record in loaded_records:
            self.records.append(record)

    def get_all_records(self) -> list[OystercatcherRecord]:
        """
        Returns all records currently stored in memory.

        Returns:
            A list of OystercatcherRecord objects.
        """
        return self.records.get_all()

    def get_record(self, index: int) -> Optional[OystercatcherRecord]:
        """
        Returns a single record by index, or None if the index is invalid.

        Args:
            index: The zero-based index of the record.

        Returns:
            The OystercatcherRecord at the given index, or None if invalid.
        """
        try:
            return self.records.get_at_index(index)
        except IndexError:
            return None

    def add_record(self, record: OystercatcherRecord) -> None:
        """
        Adds a new record to the in-memory linked list.

        Args:
            record: The OystercatcherRecord to add.
        """
        self.records.append(record)

    def edit_record(self, index: int, updated_record: OystercatcherRecord) -> bool:
        """
        Updates an existing record at the given index.

        Args:
            index: The zero-based index of the record to update.
            updated_record: The new OystercatcherRecord data.

        Returns:
            True if successful, False if the index is invalid.
        """
        try:
            self.records.set_at_index(index, updated_record)
            return True
        except IndexError:
            return False

    def delete_record(self, index: int) -> bool:
        """
        Deletes a record at the given index.

        Args:
            index: The zero-based index of the record to delete.

        Returns:
            True if successful, False if the index is invalid.
        """
        try:
            self.records.delete_at_index(index)
            return True
        except IndexError:
            return False

    def save_data(self) -> str:
        """
        Saves current in-memory records to a new CSV file using the Persistence Layer.

        Returns:
            The generated filename.
        """
        return self.file_handler.save_records(self.records.get_all())