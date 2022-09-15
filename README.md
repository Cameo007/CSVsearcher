# CSVsearcher
The official CSVsearcher program, for finding all rows in a csv file matching a regular expression in a specified column.

## Usage
### Dependencies:
- Python3
- PySide6

Run `CSVsearcher.pyw`
## Library Usage example
Run `searchObjByColName("exaple-file.csv", "email", "(.*)firm(1|2)")`

In `example-file-found.csv` are the matching rows.  
In `example-file-rest.csv` are the other rows.
