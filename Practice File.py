# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:57:54 2020

@author: masou
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


file = pd.read_excel(r'C:\Users\masou\Documents\GitHub\Haynes-Shockley-experiment\total-datas.xlsx','14.4v')
file = file.iloc[1000:4000]
x=file['x']
y=file['y']
print (x,y)

def GaussAmp(x,y,a,b,c,d):
    return (a+(b*exp(-(x-c)**2/(2*d**2))))

popt,pcov = curve_fit(GaussAmp,x,y,p0=[0,d])
plt.plot(x,y,label=i)
plt.plot(x,GaussAmp(x,*popt),color='black',linewidth=2)
plt.legend()