import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
from datetime import datetime, date, time, timedelta
import sys

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')

def Leakage(customerid):
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
    customerTier=customerTier.resample("Min").sum()
    customerTier.dropna(inplace=True)
    #print(customerTier)
  
    try:
        row = customerTier.tail(1)
        date = str(row.index[0])[:10]
        #print(dat)
        #return (dat , row[0])
        customerTier=customerTier[date]  
        checkleakage=0 in set(customerTier)
        if checkleakage==False :
 
                return "leakage dected at"+ date
        else :

               return "No leakage detected at " + date
            
                                   
    except :
        print("No data for this customer in this day ")


checkleakage= eval(sys.argv[1])
print "Leakage updates=" , checkleakage