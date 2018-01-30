import pandas as pd
import numpy as np
from pandas import datetime
from pandas import DataFrame
from pandas import Series
import time
import itertools
from datetime import datetime, date, time, timedelta
import sys

def analyze(block , year):
    block_data = block[year]['meter_value']
    block_day = block_data.resample('M').sum()
    block_day= block_day[block_day>= 0]
    Block = block_day.interpolate(method='linear')

    b = [0 for x in range(12)]
    i = int(str(Block.index[0])[5:7])-1
    for t in range(len(Block)):
        b[i]= Block[t]
        i=i+1
    return b

import json

def place():
    block = ['Tanta','Cairo','Giza','Alex']
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    i=0
    lst = []
    for item in block:
        data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/block'+item[0]+'.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
        block_data = data['meter_value']
        bloc_data = block_data.resample('A').sum()
        for block_item in bloc_data.index.values:
            year = str(block_item)[:4]
            d_final = analyze(data,year)
            i+=1 
            d = {}
            d['year']= year
            d['place']= item
            d['use'] = d_final
            lst.append(d)
    return lst

#result = place()
result = eval(sys.argv[1])
print "Analysis=" , result