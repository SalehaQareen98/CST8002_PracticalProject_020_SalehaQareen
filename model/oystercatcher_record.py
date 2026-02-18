"""
CST8002 Programming Language Research - Practical Project Part 1
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda 
Date: 2026-02-01

Dataset: Pacific Rim Native Amphibians (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Y. Zharikov, “Black Oystercatcher Population – Pacific Rim – Open Government Portal,” Canada.ca. [Online]. Available: https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02 [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (2024, Dec. 15). Classes. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/classes.html [Accessed: Jan. 30, 2026].
[3] Python Software Foundation. (2024, Dec. 15). Class Objects. The Python Tutorial. [Online]. Available: https://docs.python.org/3/tutorial/classes.html#class-objects [Accessed: Jan. 30, 2026].
[4] Python Software Foundation. (2024, Dec. 15). Basic Customization (__str__). Python Data Model. [Online]. Available: https://docs.python.org/3/reference/datamodel.html#object.__str__ [Accessed: Jan. 30, 2026].

"""

class OystercatcherRecord:
    """
    Record object representing a single row from the
    Black Oystercatcher Population dataset.

    This class stores dataset fields as instance variables
    and provides a string representation for display.
    """

    def __init__(self, visit_date, site_identification, species, total_black_oystercatcher_adults):
        """
        Constructor for the OystercatcherRecord class.

        Parameters:
            visit_date (str): Date of site visit
            site_identification (str): Site identifier
            species (str): Species name
            total_black_oystercatcher_adults (str): Adult oystercatcher count
        """
        self.visit_date = visit_date
        self.site_identification = site_identification
        self.species = species
        self.total_black_oystercatcher_adults = total_black_oystercatcher_adults

    def __str__(self):
        """
        Returns a formatted string representation of the record.

        Returns:
            str: String record output
        """
        return (f"Date: {self.visit_date}, Site Identification: {self.site_identification}, "
                f"Species: {self.species}, Total Black oystercatcher adults: {self.total_black_oystercatcher_adults}")
