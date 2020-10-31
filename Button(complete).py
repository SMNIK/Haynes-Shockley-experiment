# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:08:31 2020

@author: masou
"""

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
canvas1 = tk.Canvas(root, width=200, height=200, bg='lightgrey')
canvas1.pack()

def getExcel():
    global SMN
    import_file_path = filedialog.askopenfilename()
    xls = xlrd.open_workbook(import_file_path, on_demand=True)
    sheetNames = xls.sheet_names()
    for i in sheetNames:
        SMN = pd.read_excel(import_file_path, i)
        SMN = SMN.iloc[250:4238]
        print(i) # if put SMN, the console shows all datas of each sheet, but I shows the name of sheets, after the last name if you close the key, so plot is ready
        plt.plot(SMN['x'], SMN['y'])
        plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
        plt.ylabel('Voltage (v)')
        plt.title('non-fit')
        plt.legend(sheetNames, fontsize=10, loc='upper right')
        
browseButton_Excel = tk.Button(text='Select Excel File', command=getExcel, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)
root.mainloop()
