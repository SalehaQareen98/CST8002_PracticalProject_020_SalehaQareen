from business.record_manager import RecordManager
from model.oystercatcher_record import OystercatcherRecord


def test_add_record():
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