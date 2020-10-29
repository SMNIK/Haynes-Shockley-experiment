# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:18:51 2020

@author: masou
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 200, bg = 'lightgrey')
canvas1.pack()

def getExcel ():
    global SMN
    
    import_file_path = filedialog.askopenfilename()
    df1 = pd.read_excel (import_file_path, sheet_name='14.4v')
    print(df1)
    df1 = df1.iloc[250:4238] # set row
    plt.plot(df1['x1'],df1['y1']) # set plot (chooses columns)
    
    df2 = pd.read_excel (import_file_path, sheet_name='20.9v')
    print(df2)
    df2 = df2.iloc[250:4238]
    plt.plot(df2['x2'],df2['y2'])
    
    df3 = pd.read_excel (import_file_path, sheet_name='28.1v')
    print(df3)
    df3 = df3.iloc[250:4238]
    plt.plot(df3['x3'],df3['y3'])
    
    df4 = pd.read_excel (import_file_path, sheet_name='36.4v')
    print(df4)
    df4 = df4.iloc[250:4238] 
    plt.plot(df4['x4'],df4['y4'])
    
    df5 = pd.read_excel (import_file_path, sheet_name='44.7v')
    print(df5)
    df5 = df5.iloc[250:4238]
    plt.plot(df5['x5'],df5['y5'])
    
    df6 = pd.read_excel (import_file_path, sheet_name='50v')
    print(df6)
    df6 = df6.iloc[250:4238]
    plt.plot(df6['x6'],df6['y6'])
    
    # set lables
    plt.xlabel('Time (t) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
    plt.ylabel('Voltage (v)')
    plt.title('non-fit')
    plt.legend(["14.4v", "20.9v", "28.1v", "36.4v", "44.7v", "50v"], fontsize=10, loc='upper right')

# set directory    
browseButton_Excel = tk.Button(text='Select Excel file', command=getExcel, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)

root.mainloop()

