import pandas as pd
import numpy as np
import warnings
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from pandas.tools.plotting import autocorrelation_plot
from pandas import datetime
from pandas import DataFrame
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
from pandas import Series
import time
import itertools
from datetime import datetime, date, time, timedelta

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
data = pd.read_csv('Downloads/dataport.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
i=0
group = data.groupby('dataid')
Matrixleakage = [0 for x in range(2)]
Matrixsuddenstop = [0 for x in range(2)]
lstleakage=[]
lstsuddenstop=[]
checkSuddenstop=False
count=0
a = [0 for x in range(len(group))] 
for k , t in group:
    a[i] = group.get_group(k)
    a[i]=a[i]['meter_value']
    a[i]=a[i].resample("Min").sum()
    a[i].dropna(inplace=True)
try:   
    a[i]=a[i]['2013-09-01'] 
    while count< len(a[i]) and checkSuddenstop==False:
                    if a[i].iloc[count] ==0 :
                        count =count+1
                        print(count)
                        
                    else :
                         checkSuddenstop==True
    if checkSuddenstop==False :
                    Matrixsuddenstop[0]="Sudden Stop"
                    Matrixsuddenstop[1]=k
                    lstsuddenstop.append(np.asarray(Matrixsuddenstop))
                    
except :
        print("Error")
      