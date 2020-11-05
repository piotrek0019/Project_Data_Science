#reading the excel file

import pandas as pd
import numpy as np
class Main:
     def __init__(self):
            self.file = pd.read_excel ('./Data/Data_Collection.xlsx')