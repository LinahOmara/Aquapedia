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

def history(userID,Year):
    
    BlockT = [94,252,281,352,484,661,716,739,781,865]
    BlockC = [1103,1180,1192,1283,1314,1464,1507,1589,1697,1714,1718,2034]
    BlockG = [2064,2094,2129,2449,2461,2925,2945,3110,3147,3310]
    BlockA = [3367,3413,3482,3723,3773,3893,4031,4213,4297,4732,6910]
    userID = str(userID)
    Year = str(Year)
    ####### Determine Block ########
    ref = ''
    if int(userID) in BlockA:
        ref = '/home/aya/Desktop/Aquapedia/Datasets/blockA.csv'
    elif int(userID) in BlockC:
        ref = '/home/aya/Desktop/Aquapedia/Datasets/blockC.csv'
    elif int(userID) in BlockG:
        ref = '/home/aya/Desktop/Aquapedia/Datasets/blockG.csv'
    elif int(userID) in BlockT:
        ref = '/home/aya/Desktop/Aquapedia/Datasets/blockT.csv'
    else:
        return None
    ###### read data & prepare data #######
    try:
        dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
        data = pd.read_csv(ref , parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
    except:
        return None

    group = data.groupby('dataid')
    user = group.get_group(int(userID))['meter_value']
    userdata = user.resample('M').sum()
    userdat = userdata.interpolate(method='linear')
    try:
        Liters = [0 for x in range(len(userdat[Year]))]
        i=0
        for y in range(len(Liters)):
            Liters[i] = userdat[Year][i]
            i=i+1
        return Liters
    except:
        print ("hello1")
        return None
#Liters = history('484','2014')

Liters = eval(sys.argv[1])
print 'History=' , Liters
