#q2
import pandas as pd
import numpy as np
from pandas import DataFrame
APPL = pd.read_csv('/Users/zhanting/Documents/coursework/LIS452/week5 assignment/Apple_Stock.csv')

APPL["Daily_Change"]=APPL["High"]-APPL["Low"]
type(APPL)
#d=pd.DataFrame({"Pricerange":np.array(APPL["Price_Range"])},index = APPL["Date"])
#d = []
#d.append(APPL["Date"]).append(APPL["Price_Range"])
d=APPL[['Date','Daily_Change']] #to build a new dataframe
print(d)
