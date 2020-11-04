# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:46:21 2020

@author: masou
"""

import pandas as pd
import matplotlib as plt
from scipy import asarray as ar, exp
import xlrd
import tkinter as tk
from tkinter import filedialog

""" 
In this file, we can import an Excel file by the key, and at the end
Create a fit function for each figure.
"""

root = tk.Tk()
canvas1 = tk.canvas(root, width=200, height=200, bg="lightgrey")
canvas1.pack()

"""
we continue to code as the 'Button' file until the browser read all
excel sheets and plot them.
"""
# command def to clear the file by the key
def getExcel():
    global SMN
    import_file_path = filedialog.askopenfilename()
    xls = xlrd.open_workbook(import_file_path, on_demand=True)
    sheetNames = xls.sheet_names()
    for i in sheetNames:
        SMN = pd.read_excel(import_file_path, i)
        SMN = SMN.iloc[400:3700]
        print(i) # if put SMN, the console shows all datas of each sheet, but I shows the name of sheets, after the last name if you close the key, so plot is ready
        #plt.plot(SMN['x'], SMN['y'])
        plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
        plt.ylabel('Voltage (v)')
        plt.title('fit-black curve (Gaussian)')
        plt.legend(sheetNames, fontsize=10, loc='upper right')
    
"""
Now the top def and loop read each sheet and plot, so now we just need
to call the data of each sheet as x and y column to create fit.
the match a fit function and its coefficients.
"""
x = SMN['x']
y = SMN['y']

n = len(x)
mean = sum(x*y)/n
c = sum(y*(x-mean)**2)/n
def gauss(x,a,x0,c):
    return (a*exp(-(x-x0)**2/(2*c**2)))
popt, pcov = curve_fit(gauss,x,y,p0=[0,mean,c])
plt.plot(x,y,label=i)
