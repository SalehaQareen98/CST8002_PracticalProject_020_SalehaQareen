"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 29, 2026
Author: Saleha Qareen

References:
[1] GeeksforGeeks. (2024, Jan. 10). Linked List Data Structure. geeksforgeeks.org [Online]. 
    Available: https://www.geeksforgeeks.org/data-structures/linked-list/
    [Accessed: Mar. 11, 2026].

[2] Python Software Foundation. (n.d.). Built-in Types — list. docs.python.org. [Online].
    Available: https://docs.python.org/3/library/stdtypes.html#list
    [Accessed: Mar. 11, 2026].

[3] Python Software Foundation. (n.d.). Data Structures. docs.python.org. [Online].
    Available: https://docs.python.org/3/tutorial/datastructures.html
    [Accessed: Mar. 11, 2026].

[4] GeeksforGeeks. (2025, Jul. 15). Types of Linked List. geeksforgeeks.org [Online].
    Available: https://www.geeksforgeeks.org/dsa/types-of-linked-list/
    [Accessed: Mar. 11, 2026].
"""

from __future__ import annotations
from typing import Optional
from model.oystercatcher_record import OystercatcherRecord
from .node import Node


class SinglyLinkedList:
    """
    Represents a singly linked list used to store OystercatcherRecord objects.

    This data structure replaces the Python list previously used for
    in-memory record storage in the project.
    """

    def __init__(self) -> None:
        """
        Initializes an empty singly linked list.
        """
        self.head: Optional[Node] = None
        self.size: int = 0

    def append(self, data: OystercatcherRecord) -> None:
        """
        Adds a new record to the end of the linked list.

        Args:
            data: The OystercatcherRecord object to add.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.size += 1

    def get_all(self) -> list[OystercatcherRecord]:
        """
        Traverses the linked list and returns all stored records.

        Returns:
            A list of all OystercatcherRecord objects in the linked list.
        """
        records: list[OystercatcherRecord] = []
        current = self.head

        while current is not None:
            records.append(current.data)
            current = current.next

        return records

    def get_at_index(self, index: int) -> OystercatcherRecord:
        """
        Retrieves the record stored at the specified index.

        Args:
            index: The zero-based index of the record to retrieve.

        Returns:
            The OystercatcherRecord object at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Record index out of range.")

        current = self.head
        current_index = 0

        while current is not None:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        raise IndexError("Record index out of range.")

    def set_at_index(self, index: int, data: OystercatcherRecord) -> None:
        """
        Replaces the record at the specified index.

        Args:
            index: The zero-based index of the record to replace.
            data: The new OystercatcherRecord object.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Record index out of range.")

        current = self.head
        current_index = 0

        while current is not None:
            if current_index == index:
                current.data = data
                return
            current = current.next
            current_index += 1

        raise IndexError("Record index out of range.")

    def delete_at_index(self, index: int) -> None:
        """
        Deletes the record at the specified index.

        Args:
            index: The zero-based index of the record to delete.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Record index out of range.")

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        previous: Optional[Node] = None
        current = self.head
        current_index = 0

        while current is not None:
            if current_index == index:
                previous.next = current.next
                self.size -= 1
                return

            previous = current
            current = current.next
            current_index += 1

        raise IndexError("Record index out of range.")

    def clear(self) -> None:
        """
        Removes all records from the linked list.
        """
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        """
        Returns the number of records stored in the linked list.

        Returns:
            The number of records in the linked list.
        """
        return self.size