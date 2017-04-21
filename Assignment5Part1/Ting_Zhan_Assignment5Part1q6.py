import numpy as np
import pandas as pd
from pandas import DataFrame
APPLD = pd.read_csv('/Users/zhanting/Apple_stock_detail.csv')

daterange='\nRange of dates processed: {0} to {1}.'.format(min(APPLD['Date']),max(APPLD['Date']))
list(daterange)
adjcloserange = '\nThe highest adjusted close: {0}. \nThe lowest adjusted close: {1}.'.format(min(APPLD['Adj Close']),max(APPLD['Adj Close']))
list(adjcloserange)

maxgain=max(APPLD['Delta_Change'])
maxloss=min(APPLD['Delta_Change'])
for i,j in enumerate(APPLD['Delta_Change']):
	if j == maxgain:
		dailygain='\nBiggest daily gain (based on % Change): {0} on {1}'.format(maxgain, APPLD['Date'][i])

	if j == maxloss:
		dailyloss='\nBiggest daily loss (based on % Change): {0} on {1}'.format(maxloss, APPLD['Date'][i])
list(dailygain)
list(dailyloss)

hvolatility='\nHighest daily "Volatility": {0}'.format(max(APPLD['Volatility']))
list(hvolatility)

averadjclose='\nAverage (arithmetic mean) of adjusted closing prices: {0}'.format(np.mean(APPLD['Adj Close']))
list(averadjclose)

avervolume='\nAverage daily trading volume: {0}'.format(np.mean(APPLD['Volume']))
list(avervolume)


Apple_stock_summary=daterange + adjcloserange + dailygain + dailyloss + hvolatility + averadjclose + avervolume


file=open("Apple_stock_summary.txt",'w')
file.write(Apple_stock_summary)
file.close()

