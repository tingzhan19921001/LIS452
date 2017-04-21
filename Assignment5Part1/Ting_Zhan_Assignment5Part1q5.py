#q5
import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
APPL = pd.read_csv('/Users/zhanting/Documents/coursework/LIS452/week5 assignment/Apple_Stock.csv')

#APPL["Daily_Change"]="{0:.3f}".format(APPL["High"]-APPL["Low"])
change = np.array(APPL["Adj Close"]) 
volume = np.array(APPL["Volume"])

APPL["Delta_Change"] = 0
APPL["Volatility"] = 0


for i,j in enumerate(change):
    APPL.ix[i,"Daily_Change"] = "{0:.3f}".format((APPL["High"]-APPL["Low"])[i])
    if i == len(change)-1:
        break
    a = change[i]
    b = change[i+1]
   
    APPL.ix[i,"Delta_Change"]="{0:.2f}%".format((a/b-1) * 100)
    APPL.ix[i,"Volatility"] = int(abs(a/b-1)*APPL["Volume"][i])
    
d = APPL[['Date','Open','High','Low','Close','Volume',"Adj Close",'Daily_Change','Delta_Change',"Volatility"]]
d.to_csv('Apple_stock_detail.csv',index = None)
APPLD = pd.read_csv('Apple_stock_detail.csv')
print(APPLD)
