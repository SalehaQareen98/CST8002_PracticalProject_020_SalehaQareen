# main.py
# Author: Saleha Qareen
# Testing OystercatcherRecord class

from oystercatcher_record import OystercatcherRecord

# Display your full name
FULL_NAME = "Saleha Qareen"
print(f"Program Author: {FULL_NAME}\n")

# Create a sample record object manually
sample_record = OystercatcherRecord(
    visit_date="29/05/2008",
    site_identification="1",
    species="Haematopus bachmani",
    total_black_oystercatcher_adults="6"
)

# Print the object to verify it works
print("Sample Record:")
print(sample_record)
