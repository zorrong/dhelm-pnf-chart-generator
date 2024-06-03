# -*- coding: utf-8 -*-
"""
    **Column.py**
    - Copyright (c) 2019, KNC Solutions Private Limited.
    - License: 'Apache License, Version 2.0'.
    - version: 1.0.0

    This module contains the implementation of the Column class, which represents a column in a data table.
"""

class Column:
    def __init__(self):
        """
        Initializes a new instance of the Column class.

        Attributes:
            bottom (int): The index of the bottom row in the column. Default is -1, indicating that the column is empty.
            top (int): The index of the top row in the column. Default is -1, indicating that the column is empty.
            type (str): The data type of the column. Default is 'NA', indicating that the data type has not been set.
            timestamp (str): The timestamp associated with the creation or modification of the column. Default is 'NA'.
            columnAdded (int): A flag indicating whether the column has been added to the data table. Default is 0, indicating that the column has not been added.
        """
        self.bottom = -1
        self.top = -1
        self.type = 'NA'
        self.timestamp = 'NA'
        self.columnAdded = 0
