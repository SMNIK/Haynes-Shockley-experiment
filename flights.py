# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:02:06 2020

@author: masou
"""

import pandas as pd
import matplotlib.pyplot as plt

# set directory
first = pd.read_excel(r'./total-datas.xlsx', '14.4v')
second = pd.read_excel(r'./total-datas.xlsx', '20.9')
third = pd.read_excel(r'./total-datas.xlsx', '28.1')
fourth = pd.read_excel(r'./total-datas.xlsx', '36.4')
fifth = pd.read_excel(r'./total-datas.xlsx', '44.7')
sixth = pd.read_excel(r'./total-datas.xlsx', '50')

# set row
first = first.iloc[250:4238]
second = second.iloc[250:4238]
third = third.iloc[250:4238]
fourth = fourth.iloc[250:4238]
fifth = fifth.iloc[250:4238]
sixth = sixth.iloc[250:4238]

# set plot
plt.plot(first['x'], first['y'])
plt.plot(second['x'], second['y'])
plt.plot(third['x'], third['y'])
plt.plot(fourth['x'], fourth['y'])
plt.plot(fifth['x'], fifth['y'])
plt.plot(sixth['x'], sixth['y'])

# set lable
plt.xlabel('Time (\u03BC s) \n Set of pulses collected at constant d=0.35cm, by varying the sweeping voltage $V_{s}$')
plt.ylabel('Voltage (v)')
plt.title('non-fit')
plt.legend(["14.4v", "20.9v", "28.1v", "36.4v", "44.7v", "50v"], fontsize=10, loc='upper right')
