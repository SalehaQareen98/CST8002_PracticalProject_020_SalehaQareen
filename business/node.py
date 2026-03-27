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


class Node:
    """
    Represents a single node in a singly linked list.

    A node stores one OystercatcherRecord object and a reference
    to the next node in the linked list.
    """

    def __init__(self, data: OystercatcherRecord) -> None:
        """
        Initializes a Node object with record data.

        Args:
            data: The OystercatcherRecord object to store in the node.
        """
        self.data: OystercatcherRecord = data
        self.next: Optional[Node] = None