"""Converting our .csv file to a dict."""

from csv import DictReader
import math

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return dict."""
    output: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader: DictReader = DictReader(file_handle)
    for row in csv_reader:
        output.append(row)
    file_handle.close()
    return output

filename: str = "MCU_Timeline.csv"
x = read_csv_rows(filename)
print(x)