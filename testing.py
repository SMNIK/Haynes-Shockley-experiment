# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:57:54 2020

@author: masou
"""
# SECOND PART is the completed viwe of the top solution
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import xlrd
import tkinter as tk
from tkinter import filedialog
import numpy as np
import re
""" 
In this file, we can import an Excel file by the key, and at the end
Create a fit function for each figure.
"""

root = tk.Tk()
# provide the window size and background-color of the key
canvas1 = tk.Canvas(root, width=200, height=200, bg='lightgrey')
canvas1.pack()

"""
we continue to code as the 'Button' file until the browser read all
excel sheets and plot them.
"""
# command def to clear the file by the key
def getExcel():
    global SMN
    # let the machine choose a file and import it as the excel file
    import_file_path = filedialog.askopenfilename()
    xls = xlrd.open_workbook(import_file_path, on_demand=True)
    # for a file with different sheets and note on the plot 
    sheetNames = xls.sheet_names()
    # read each sheet separately and plot them together
    for i in sheetNames:
        SMN = pd.read_excel(import_file_path, i)
        # I separate useful data from useless noises (declare rows)
        SMN = SMN.iloc[400:3700]
        print(i) # if put SMN, the console shows all datas of each sheet, but I shows the name of sheets, after the last name if you close the key, so plot is ready
        #plt.plot(SMN['x'], SMN['y'])
        plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
        plt.ylabel('Voltage_s (v)')
        plt.title('fit-black curve (Gaussian)')
        #plt.legend(sheetNames, fontsize=10, loc='upper right')
    

# Now the top def and loop read each sheet and plot, so now we just need to call the data of each sheet as x and y column to create fit. the match a fit function and its coefficients. 

        x = SMN['x']
        y = SMN['y']
        # for nomalize the data we need the number of data and mean
        n = len(x)    
        # mean should be include the sum of time multiply by its voltage                     
        mean = sum(x*y)/n 
        # and the sigma coefficient is the total normalization coefficient for each drift              
        sigma = sum(y*(x-mean)**2)/n  
        # now use the Gaussian function and the coefficients to fit with the figures
        def gauss(x,a,x0,sigma):
            return (a*np.exp(-0.5*((x-x0)/sigma)**2))
        # x0 is the time of the maximum fly
        popt,pcov = curve_fit(gauss,x,y,p0=[0,mean,sigma])
        #print(gauss)
        plt.plot(x,y,label=i)
        plt.plot(x,gauss(x,*popt),color='black',linewidth=2)
        plt.legend()
        t = popt[1]
        FWHM = np.sqrt(np.log(4))*2*popt[2]
        d = 3
        Area = popt[0]*2*popt[2]*np.sqrt(np.pi/2)
        I = [float(z) for z in re.findall(r'-?\d+\.?\d*', i)]
        c = len(I)
        for z in range(c):
            E_s = I[z]/d
        print(t,FWHM,Area,E_s) # This is the gauss coefficients for calculations

"""
Now we finish it with closing the key.
for showing the plots and fits after coplete calculation close the key
"""
browseButton_Excel = tk.Button(text='Select Excel File', command=getExcel, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)
root.mainloop() 
