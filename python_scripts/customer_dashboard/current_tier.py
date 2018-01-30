import pandas as pd
import numpy as np
import warnings
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from pandas.tools.plotting import autocorrelation_plot
from pandas import datetime
from pandas import DataFrame
import time
import itertools
from datetime import datetime, date, time, timedelta
import sys

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
LastMonth='2013-09'

def Tier(customerid):
    if  94 <= customerid and customerid <= 865 :
         data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockT.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
    elif 1103 <= customerid and customerid <= 2034 :
         data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockC.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
    elif 2064 <= customerid and customerid <= 3310 :
         data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockG.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
    elif 3367 <= customerid and customerid <= 6910 :
         data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockA.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)

    group = data.groupby('dataid')
    customer= group.get_group(customerid)
    customerTier=customer['meter_value']
    customerTier=customerTier.resample("M").sum()

    customerTier.dropna(inplace=True)
    customerTier.to_frame()
    try:
        return customerTier[LastMonth][0]
    except:
        print("No data")
        return 0
    
currentTier = eval(sys.argv[1])

print(currentTier)

