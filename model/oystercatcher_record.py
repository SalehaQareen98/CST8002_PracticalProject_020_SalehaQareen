"""
CST8002 Programming Language Research - Practical Project Part 3
Author: Saleha Qareen (041161192)
Professor: Stanley Pieda
Due Date: 2026-03-29

Dataset: Black Oystercatcher Population – Pacific Rim (Open Government Licence - Canada)
License: Black Oystercatcher Population - Pacific Rim [1]

References:
[1] Parks Canada. (Oct 1, 2017). Black Oystercatcher Population – Pacific Rim. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02  [Accessed: Jan. 29, 2026].
[2] Python Software Foundation. (n.d). Classes. docs.python.org. [Online]. Available: https://docs.python.org/3/tutorial/classes.html [Accessed: Jan. 30, 2026].
[3] Python Software Foundation. (n.d). Class Objects. docs.python.org. [Online]. Available: https://docs.python.org/3/tutorial/classes.html#class-objects [Accessed: Jan. 30, 2026].
[4] Python Software Foundation. (n.d). Basic Customization (__str__). docs.python.org. [Online]. Available: https://docs.python.org/3/reference/datamodel.html#object.__str__ [Accessed: Jan. 30, 2026].
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
