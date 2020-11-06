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
    
    SMN1 = pd.read_excel (import_file_path, sheet_name='14.4v')
    print(SMN1)
    SMN1 = SMN1.iloc[250:4238] # set row
    plt.plot(SMN1['x'],SMN1['y']) # set plot (chooses columns)
    
    SMN2 = pd.read_excel (import_file_path, sheet_name='20.9v')
    print(SMN2)
    SMN2 = SMN2.iloc[250:4238]
    plt.plot(SMN2['x'],SMN2['y'])
    
    SMN3 = pd.read_excel (import_file_path, sheet_name='28.1v')
    print(SMN3)
    SMN3 = SMN3.iloc[250:4238]
    plt.plot(SMN3['x'],SMN3['y'])
    
    SMN4 = pd.read_excel (import_file_path, sheet_name='36.4v')
    print(SMN4)
    SMN4 = SMN4.iloc[250:4238] 
    plt.plot(SMN4['x'],SMN4['y'])
    
    SMN6 = pd.read_excel (import_file_path, sheet_name='44.7v')
    print(SMN6)
    SMN6 = SMN6.iloc[250:4238]
    plt.plot(SMN6['x'],SMN6['y'])
    
    # set lables
    plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
    plt.ylabel('Voltage (v)')
    plt.title('non-fit')
    plt.legend(["14.4v", "20.9v", "28.1v", "36.4v", "44.7v"], fontsize=10, loc='upper right')

# set directory    
browseButton_Excel = tk.Button(text='Select Excel file', command=getExcel, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)

root.mainloop()

