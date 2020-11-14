# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:57:54 2020

@author: masou
"""
# SECOND PART is the completed viwe of the top solution
import pandas as pd
#from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import xlrd
import tkinter as tk
from tkinter import filedialog
import numpy as np
import re
import xlsxwriter
from scipy import polyfit , polyval

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
        #print(i) # if put SMN, the console shows all datas of each sheet, but I shows the name of sheets, after the last name if you close the key, so plot is ready
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
        # x0 is the time for the maximum fly
        popt,pcov = curve_fit(gauss,x,y,p0=[0,mean,sigma])
        plt.figure(1)
        #print(gauss)
        plt.plot(x,y,label=i)
        plt.plot(x,gauss(x,*popt),color='black',linewidth=2)
        plt.legend()
        #print(popt) # This is the gauss coefficients for calculations
        t = popt[1] # time of the peak (micro second)
        delta_t = np.sqrt(np.log(4))*2*popt[2] # nirmalizaionm of mean drift by FWHM (micro second)
        d = 3 # samle lenght (centimeter)
        Area = popt[0]*2*popt[2]*np.sqrt(np.pi/2) # (v micro s)
        I = [float(smn) for smn in re.findall(r'-?\d+\.?\d*', i)]
        c = len(I)
        for SMN in range(c):
            E_s = I[SMN]/d # scale is voltage per centimeter
        D = 0.35 # laser shot distance from conector
        V_d = D*1e6/t # scale is (cm/s)
        mu = V_d/E_s # and easily scale is (cm^2/v*s)
        lnA = np.log(Area)
        myList = [I[SMN],t,delta_t,Area,E_s,V_d,mu,lnA]

# As import data from each loop and put them in the relevant index of the excel file, we need to create the if statement and check when the datasheet changes, the index number should be changed too.        
        
        if I[SMN]==14.4:
            workbook = xlsxwriter.Workbook('D:/analyses.xlsx') #you can choose any name 
            worksheet_analyses=workbook.add_worksheet('analyses') #you can choose any name
            for j in range(8):
                worksheet_analyses.write(1,j,myList[j])
        elif I[SMN]==20.9:
            for j in range(8):
                worksheet_analyses.write(2,j,myList[j])
        elif I[SMN]==28.1:
            for j in range(8):
                worksheet_analyses.write(3,j,myList[j])
        elif I[SMN]==36.4:
            for j in range(8):
                worksheet_analyses.write(4,j,myList[j])
        elif I[SMN]==44.7:
            for j in range(8):
                worksheet_analyses.write(5,j,myList[j])
        elif I[SMN]==50:
            for j in range(8):
                worksheet_analyses.write(6,j,myList[j])
        else:
            pass
        print(I[SMN])
    worksheet_analyses.write('A1','V(v)')
    worksheet_analyses.write('B1','t (\u03BC s)')
    worksheet_analyses.write('C1','delta_t(\u03BC s)')
    worksheet_analyses.write('D1','A(v \u03BC s)')
    worksheet_analyses.write('E1','E_s(v/cm)')
    worksheet_analyses.write('F1','V_d(cm/s)')
    worksheet_analyses.write('G1','mu(cm^2/vs)')
    worksheet_analyses.write('H1','lnA')
    workbook.close()
    plt.show()
    
"""
Now we finish it by closing the key.
for showing the plots and fits after complete calculation close the key
"""
browseButton_Excel = tk.Button(text='Select Excel File', command=getExcel, bg='blue', fg='yellow', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)
root.mainloop() 

# now the useful normalized data is in a new excel file and we can plot any part which we need
# one of the most important plot is the logarithmic area depends on the time

analyses = pd.read_excel(r'D:/analyses.xlsx','analyses') #you can choose any name
time = analyses['t (\u03BC s)']
lnA = analyses['lnA']
plt.figure(2)
plt.scatter(time,lnA,color='g',marker='*',alpha=0.6,s=100)
plt.xlabel('Time (\u03BC s)')
plt.ylabel('lnA')
plt.grid()
sMn = polyfit(time,lnA,1)
plt.plot(time,polyval(sMn,time))
plt.show()

