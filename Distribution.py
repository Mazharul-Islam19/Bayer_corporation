# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

global df1
global df2

data1 = pd.read_csv('Pre-finish.csv')

site1 = list(pd.unique(data1['Site']))
size1 = list(pd.unique(data1['Size']))
flavor1 = list(pd.unique(data1['Flavor']))
processing_rate1 = list(pd.unique(data1['Processing_Rate']))

df1 = pd.DataFrame(columns=['Site', 'Size', 'Flavor','Mean','Std'])

l = 0
for i in site1:
    for j in size1:
        for k in flavor1:
            temp = data1[(data1['Site']==i) & (data1['Size']==j) & (data1['Flavor']==k)]
            mu = temp['Processing_Rate'].mean()
            std = temp['Processing_Rate'].std()
            df1.loc[l,'Site'] = i
            df1.loc[l,'Size'] = j
            df1.loc[l,'Flavor'] = k
            df1.loc[l,'Mean'] = mu
            df1.loc[l,'Std'] = std
            l += 1
    plt.hist(data1['Processing_Rate'].where(data1['Site']==i), bins=100, label=i)
    plt.legend()
    plt.show()


data2 = pd.read_csv('Packaging.csv')

site2 = list(pd.unique(data2['Site']))
size2 = list(pd.unique(data2['Size']))
Packaging = list(pd.unique(data2['Packaging_Type']))
processing_rate2 = list(pd.unique(data2['Processing_Rate']))

df2 = pd.DataFrame(columns=['Site', 'Size', 'Packaging','Mean','Std'])

l = 0
for i in site2:
    for j in size2:
        for k in Packaging:
            temp = data2[(data2['Site']==i) & (data2['Size']==j) & (data2['Packaging_Type']==k)]
            mu = temp['Processing_Rate'].mean()
            std = temp['Processing_Rate'].std()
            df2.loc[l,'Site'] = i
            df2.loc[l,'Size'] = j
            df2.loc[l,'Packaging'] = k
            df2.loc[l,'Mean'] = mu
            df2.loc[l,'Std'] = std
            l += 1
    plt.hist(data2['Processing_Rate'].where(data2['Site']==i), bins=100, label=i)
    plt.legend()
    plt.show()

