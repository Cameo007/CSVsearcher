#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The official CSVsearcher program, for finding all rows in a csv file matching a regular expression in a specified column.
"""

__author__ = "Pascal Dietrich"
__copyright__ = 'Copyright 2022, CSVsearcher'
__credits__ = ["Pascal Dietrich"]
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Pascal Dietrich"
__email__ = "pascal.1.dietrich@hotmail.com"
__status__ = "Release"

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon

import os

import CSVsearcherLib


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 200))
        self.setWindowIcon(QIcon("CSVsearcher.png"))
        self.setWindowTitle("CSVsearcher")

        self.filename = ""

        layout = QVBoxLayout()

        buttonSelectFile = QPushButton("CSV-Datei öffnen")
        buttonSelectFile.clicked.connect(self.selectFile)
        layout.addWidget(buttonSelectFile)

        self.inputCol = QLineEdit()
        self.inputCol.setPlaceholderText("Spalte")
        layout.addWidget(self.inputCol)

        self.inputRegex = QLineEdit()
        self.inputRegex.setPlaceholderText("Regex")
        layout.addWidget(self.inputRegex)

        buttonExec = QPushButton("Ausführen")
        buttonExec.clicked.connect(self.exec)
        layout.addWidget(buttonExec)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def selectFile(self):
        self.filename = QFileDialog.getOpenFileName(self, "CSV-Datei auswählen", os.getcwd(), "Textdateien (*.csv)")[0]

    def exec(self):
        col = self.inputCol.text()
        regex = self.inputRegex.text()

        #Exec
        CSVsearcherLib.searchObjByColName(self.filename, col, regex)

        #Reset
        self.inputCol.setText("")
        self.inputRegex.setText("")
app = QApplication()
app.setStyle("Fusion")

window = Window()
window.show()

app.exec()
