# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:57:54 2020

@author: masou
"""
# if we want to use the base data as CSV

import numpy as np
import csv
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
import tkinter as tk
import tkinter as filedialog
import pandas as pd

# Import csv file and save as the new table
root = tk.Tk()
canvas1 = tk.Canvas(root, width=200, height=200, bg='lightgrey')
canvas1.pack()


def getCsv():
    global SMN
    import_file_path = filedialog.askopenfilename()
    CSV = csv.open_workbook(import_file_path, on_demand=True)
    SMN = pd.read.csv(import_file_path,CSV.sheet_names())
        
    with open(root.mainloop(),"r") as i:
        rawdata=list(csv.reader(i,delimiter=","))
        
    data = np.array(rawdata[19:],dtype=np.float)
    x = data[19:,0]
    y =data[19:,1]
    plt.figure(1,dpi=120)
    plt.title("simple testing")
    plt.x(rawdata[0][0])
    plt.y(rawdata[0][1])
    #plt.xlim(3,60) # control x-axis duration or range
    #plt.ylim(-0.006,0.09) # control y-axis range 
    #plt.xscale("log")
    #plt.yscale("log")
    plt.plot(x,y,lable="time over voltage")

browseButton_Excel = tk.Button(text='Select Excel File', command=getCsv, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)
root.mainloop()




