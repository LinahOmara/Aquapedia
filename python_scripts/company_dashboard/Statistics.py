import pandas as pd
import numpy as np
from pandas import datetime
from pandas import DataFrame
import time
import sys

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/dataport.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)


def Geographic_statistic(interval):
    group = data.groupby('block')
    Matrix = [0 for x in range(2)]
    a = [0 for x in range(len(group))] 
    lst=[]
    i=0
    for k , t in group:
        a[i] = group.get_group(k)
    #a[i]=a[i]['meter_value']
    #print(a[i])
        a[i] = a[i].resample(interval).sum() 
        a[i].dropna(inplace=True)
    #print(a[i])
        d = {}
        d['use']= a[i].iloc[len(a[i])-1]['meter_value']
        d['place']= k
        lst.append(d)

        i=i+1
    return lst


#R = Geographic_statistic('M')
result = eval(sys.argv[1])
print "Statistics= ", result
   