# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:57:54 2020

@author: masou
"""

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_excel(r'C:\Users\masou\Documents\GitHub\Haynes-Shockley-experiment\total-datas.xlsx','14.4v')
file = file.iloc[1000:4000]
x=file['x']
y=file['y']
print (x,y)
