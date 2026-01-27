# Author: Saleha Qareen

class OystercatcherRecord:
    def __init__(self, visit_date, site_identification, species, total_black_oystercatcher_adults):
        self.visit_date = visit_date
        self.site_identification = site_identification
        self.species = species
        self.total_black_oystercatcher_adults = total_black_oystercatcher_adults

    def __str__(self):
        return (f"Date: {self.visit_date}, Site ID: {self.site_identification}, "
                f"Species: {self.species}, Total Adults: {self.total_black_oystercatcher_adults}")
