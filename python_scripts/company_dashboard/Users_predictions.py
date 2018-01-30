import pandas as pd
import numpy as np
from pandas import datetime
from pandas import DataFrame
import time

def get_predictions_company(block):
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d-%H')
    usersdata = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/predictions/company_prediction.csv' , parse_dates= ['date'], index_col='date',date_parser=dateparse)
    group = usersdata.groupby('block')
    lst = []
    for k , t in group:
        data_predict = group.get_group(k)
        arr=[0 for x in range(len(data_predict))]
        for item in range(len(data_predict)):
            arr[item] = data_predict['predictions'][item]
        d = {}
        d['use'] = arr
        d['place']= k
        lst.append(d)
    return lst

result = get_predictions_company(['T','G','A','C'])
print "Predictions=", result
