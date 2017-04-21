#q4
import pandas as pd
import numpy as np
from pandas import DataFrame
APPL = pd.read_csv('/Users/zhanting/Documents/coursework/LIS452/week5 assignment/Apple_Stock.csv')

APPL["Daily_Change"]=APPL["High"]-APPL["Low"]
change = np.array(APPL["Adj Close"]) 
volume = np.array(APPL["Volume"])

APPL["Delta_Change"] = 0
for i,j in enumerate(change):
    if i == len(change)-1:
        break
    a = change[i]
    b = change[i+1]
   
    APPL.ix[i,"Delta_Change"]=abs(a/b-1)
    
    
APPL["Volatility"]=APPL["Volume"]*APPL["Delta_Change"]

d=APPL[['Date','Volatility']]
print(d)
