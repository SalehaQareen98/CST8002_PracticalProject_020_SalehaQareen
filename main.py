# main.py
# Author: Saleha Qareen

import csv
from oystercatcher_record import OystercatcherRecord

print("Program Author: Saleha Qareen\n")

csv_path = r"C:\Users\saleh\Documents\Level 6\python\CST8002_PracticalProject_020_SalehaQareen\pacific_rim_npr_coastalmarine_black_oystercatcher_population_nesting_counts_2008-2017_data.csv"

records = []  # array / list to store record objects

with open(csv_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

