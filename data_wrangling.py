"""Converting our .csv file to a dict."""

from __future__ import annotations
from csv import DictReader
import math

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return dict."""
    output: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        output.append(row)
    file_handle.close()
    return output

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of movies in the header year of the MCU."""
    output: list[str] = []
    for elem in table: 
        output.append(elem[header])
    return output 

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headres as keys."""
    output: dict[str, list[str]] = {}
    first_row: dict[str, list[str]] = table[0]
    for key in first_row:
        output[key] = column_vals(table, key)
    return output

filename: str = "data/mcu_timeline.csv"
table: list[dict[str, str]] = read_csv_rows(filename)
# print(filename)
# print(column_vals(table, "MCU_Year"))
print(columnar(table))