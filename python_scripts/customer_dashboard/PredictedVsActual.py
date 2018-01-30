import pandas as pd
import numpy as np
from pandas import datetime
from pandas import DataFrame
from pandas import Series
import datetime
from datetime import timedelta, date,datetime
import itertools
from datetime import datetime, date, time, timedelta
import sys

def calculate_bill(cubic):
    if cubic <= 10:
        bill = cubic * 0.30
    elif cubic > 10 and cubic <= 20:
        bill = cubic * 0.70  
    elif cubic > 20 and cubic <= 40:
        bill = cubic * 1.05  
    else:
        bill = cubic * 1.55
    return bill
def get_predictions(userID):
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
    usersdata = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/predictions/predictions.csv' , parse_dates= ['date'], index_col='date',date_parser=dateparse)
    group = usersdata.groupby('userid')
    arr=[]
    try:
        data_user = group.get_group(int(userID))
        for item in range(len(data_user)):
            arr.append(data_user['Predictions'][item])

        return [data_user['actual'][0],calculate_bill(sum(arr) * 0.001) , sum(arr)]
    except:
        return [0,calculate_bill(sum(arr)*0.001)]
results , arr = get_predictions('252')


def get_actual_predicted(userID):
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
    usersdata = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/predictions/actual_expected.csv' , parse_dates= ['date'], index_col='date',date_parser=dateparse)
    group = usersdata.groupby('userid')   
    try:
        data_user = group.get_group(int(userID))
        return [data_user['actual'][0],data_user['predicted'][0]]
    except:
        return [0,0]
    
Liters = eval(sys.argv[1])
Actual, Expected_bill, Expected = eval(sys.argv[2])
print 'Actual Vs Expected=' , Liters
if Liters[0] > Liters[1]:
    msg = 'Bad, you consumed more than we expected yesterday'
elif Liters[0] == Liters[1]:
    msg = 'Good, you consumed exactly what is expected'
else:
    msg = 'Very good, you consumed less than we expected'

print 'msg= ' , msg
print 'Expected bill=' , Expected_bill
print 'Actual till now=' , (Actual/Expected)*100
