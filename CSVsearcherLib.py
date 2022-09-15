#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The official CSVsearcher library, for finding all rows in a csv file matching a regular expression in a specified column.
"""

__author__ = "Pascal Dietrich"
__copyright__ = 'Copyright 2022, CSVsearcher'
__credits__ = ["Pascal Dietrich"]
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Pascal Dietrich"
__email__ = "pascal.1.dietrich@hotmail.com"
__status__ = "Release"

import csv, re

def getDialect(filename):
    with open(filename, "r") as file:
        dialect = csv.Sniffer().sniff(file.read(1024))
        return dialect
        
def getLines(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file, getDialect(filename))
        return list(reader)

def searchObjByColName(filename, col, regex):
    dialect = getDialect(filename)
    
    pattern = re.compile(regex)
    
    data = getLines(filename)
    colindex = data[0].index(col)

    fileFound = open(f"{filename.split('.')[0]}-found.csv", "w", newline="")
    fileRest = open(f"{filename.split('.')[0]}-rest.csv", "w", newline="")
    
    writerFound = csv.writer(fileFound, dialect)
    writerRest = csv.writer(fileRest, dialect)
        
    writerFound.writerow(data[0])
    writerRest.writerow(data.pop(0))
        
    for row in data:
        if pattern.match(row[colindex]):
            writerFound.writerow(row)
        else:
            writerRest.writerow(row)
    
    fileFound.close()
    fileRest.close()