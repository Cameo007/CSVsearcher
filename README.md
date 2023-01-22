# CSVsearcher
A program, for finding all rows in a csv file matching a regular expression in a specified column.

## Usage
### Dependencies:
- Python3
- PySide6

Run `CSVsearcher.pyw`
## Library Usage example
Run `searchObjByColName("exaple-file.csv", "email", "(.*)firm(1|2)")`

The matching rows are in `example-file-found.csv` and the other rows are in `example-file-rest.csv`.
