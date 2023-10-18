# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:59:32 2023

@author: woa8uh
"""

import pandas as pd

data_statewise = pd.read_csv("statewise.csv")

data_districtwiase = pd.read_csv("districtwise.csv")

data_level3 = pd.read_csv("levelwise.csv")

data_statewise['Level No'] = 1
data_districtwiase['Level No'] = 2
data_level3['Level No'] = 3