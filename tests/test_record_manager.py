"""
CST8002 Programming Language Research - Practical Project Part 2
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda 
Due Date: 2026-02-22

Dataset: Black Oystercatcher Population – Pacific Rim (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Parks Canada. (Oct 1, 2017). Black Oystercatcher Population – Pacific Rim. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02  [Accessed: Jan. 29, 2026].
[2] E. Sales De Andrade. (2023,Dec. 06). Python Unit Testing Best Practices. pytest-with-eric.com. [Online]. Available: https://pytest-with-eric.com/introduction/python-unit-testing-best-practices/ [Accessed: Feb. 13, 2026].
[3] W3Tutorials(n.d). Using Python’s pytest Framework for Unit Testing. w3tutorials.net. [Online]. Available: https://www.w3tutorials.net/python-tutorial/using-pythons-pytest-framework-for-unit-testing/ [Accessed: Feb. 13, 2026].
[4] pytest development team(n.d). pytest Documentation. docs.pytest.org. [Online]. Available: https://docs.pytest.org/en/stable/ [Accessed: Feb. 20, 2026].
"""

from business.record_manager import RecordManager
from model.oystercatcher_record import OystercatcherRecord


def test_add_record():
    """
    Unit test to verify that a new record can be added
    to the sequential data structure in memory.

    This test confirms:
    - A record is successfully inserted into the list.
    - The stored record fields match the expected values.
    """
    # Create instance of Business Layer (sequential data structure stored here)
    manager = RecordManager()

    # Create a new record object (Model Layer)
    record = OystercatcherRecord(
        visit_date="01/01/2025",
        site_identification="99",
        species="Test Species",
        total_black_oystercatcher_adults="5"
    )

    # "Create a new record and store it in the simple data structure in memory"
    manager.add_record(record)

    # Verify record was added to sequential data structure (list)
    # Checking list size increased to 1
    assert len(manager.get_all_records()) == 1

    # Retrieve stored record from memory
    stored_record = manager.get_record(0)

    # Verify data was placed into correct fields of record object
    assert stored_record.visit_date == "01/01/2025"
    assert stored_record.site_identification == "99"
    assert stored_record.species == "Test Species"
    assert stored_record.total_black_oystercatcher_adults == "5"