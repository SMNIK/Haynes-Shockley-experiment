# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:57:46 2020

@author: masou
"""

import pandas as pd 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar, exp
import xlrd 
import tkinter as tk
from tkinter import filedialog

"""
The key needs to show by the graphical user interfaces (GUI), which here, 
as shown below, the main lib is tkinter.
"""
root = tk.Tk()
canvas1 = tk.canvas(root, width=200, height=200, bg='lightgrey')
canvas1.pack()

""" Now for reading the excel file we use def as a defined function.
In this code, my data is in 2-D and I say to the function, any file with a different 
sheets name can be generalized as x-y data.
"""
def getExcel():
    global SMN
    import_file_path = filedialog.askopenfilename()
    xls = xlrd.open_workbook(import_file_path, on_demand=True)
    sheetNams = xls.sheet_names()
    for i in sheetNams:
        SMN = pd.read_excel(import_file_path, i)
        SMN = SMN.iloc[400:3700] # inside the reader function we can order to code just read any rows that we need 
        print (i) # by this command, outline print the name of each sheet after finishing the reading datas
""" Now for labeling the plot and ploting the datas, we use below commands."""
        plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
        plt.ylabel('Voltage (v)')
        plt.title('Fit by Gaussian function (black curve)' )
        plt.legend(sheetNames, fontsize=10, loc='upper right')
""" I difined the column's names as below, you can change them. """
        x = ar(SMN['x'])
        y = ar(SMN['y'])
""" The fitting GaussAmp function could be use as below. """
        n = len(x) # the number of data
        mean = sum(x*y)/n # 
        sigma = sum(y*(x-mean**2))/n
        def gaus