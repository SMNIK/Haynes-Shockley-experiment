# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:34:05 2020

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
    
    names = ["14.4v","20.9v","28.1v","36.4v","44.7v","50v"]
    for x in names:
        SMN = pd.read_excel (import_file_path, sheet_name= x)
        SMN = SMN.iloc[250:4238] # set row
        print(SMN)
        plt.plot(SMN['x'],SMN['y']) # set plot (chooses columns)
    
    # set lables
    plt.xlabel('Time (t) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
    plt.ylabel('Voltage (v)')
    plt.title('non-fit')
    plt.legend(["14.4v", "20.9v", "28.1v", "36.4v", "44.7v", "50v"], fontsize=10, loc='upper right')

# set directory    
browseButton_Excel = tk.Button(text='Select Excel file', command=getExcel, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)

root.mainloop()