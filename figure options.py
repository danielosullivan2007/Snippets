# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:17:15 2019

@author: Daniel
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.pyplot as plt

plt.rc('font', family='monospace') 
plt.rc('font', serif='courier') 




a4_dims = (11.7, 8.27)




font = {'family': 'courier',
        'color':  'green',
        'weight': 'normal',
        'size': 16,
        }


data = pd.read_csv('C:\\Users\\Daniel\\Desktop\\1.csv')
data = data.head(20)
data.Date = pd.to_datetime(data.Date)
data.Average[data['Average']==-99.99] = np.nan


fig, ax = plt.subplots(figsize=a4_dims)
sns.lineplot(data=data, x='Date', y='Average', ax = ax)
sns.set_style("ticks")
#Set Dates Scale: Interval Goes Between brackets
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator(6)  # every month
years_fmt = mdates.DateFormatter('%b %Y')

ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

ax.set_xlabel('TEST', fontsize = 16, color = 'gray')
ax.set_ylabel("Test Y", fontsize =14,fontdict=dict(weight='bold', color ='gray'))
#plt.xticks(rotation=90, fontname = "Courier")
ax.tick_params(labelsize = 14)
colors = ['b', 'r', 'g']# Can use this to cycle colors if you like

for xtick in  ax.get_xticklabels():
    xtick.set_color('black')
for ytick in  ax.get_yticklabels():
    ytick.set_color('gray')   
plt.title('Test Title',pad = 100, loc = 'left', fontdict=dict(weight='bold', color ='gray',size =22))
sns.despine()    