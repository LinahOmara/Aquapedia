import pandas as pd
import numpy as np
from pandas import datetime
from pandas import DataFrame
import time

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/leakagetrial.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
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
        row = a[i].tail(1)
        date = str(row.index[0])[:10]
        a[i]=a[i][date]  
        checkleakage=0 in set(a[i])
        i=i+1
        if checkleakage==False:
            print("user_id",':',k,',',"alerts",':',"Leakage")                        
    except :
        print("Error")

