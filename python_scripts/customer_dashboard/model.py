import pandas as pd
import numpy as np
from matplotlib.pylab import rcParams
from pandas import datetime
from pandas import DataFrame
from matplotlib import pyplot
import time
import itertools
from datetime import datetime, date, time, timedelta
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import sys

def predict(ts_day_log):
    import statsmodels.api as sm
    from statsmodels.tsa.arima_model import ARIMA
    from sklearn.metrics import mean_squared_error
    X = ts_day_log.values
    predictions = list()
    model = ARIMA(X, order=(10, 0, 1))
    model_fit = model.fit(transparams=True,trend='c',disp=False)
    predictions = model_fit.forecast(30)[0]
    return np.exp(predictions)

def Bill_expected(userID):    
    BlockT = [94,252,281,352,484,661,716,739,781,865]
    BlockC = [1103,1180,1192,1283,1314,1464,1507,1589,1697,1714,1718,2034]
    BlockG = [2064,2094,2129,2449,2461,2925,2945,3110,3147,3310]
    BlockA = [3367,3413,3482,3723,3773,3893,4031,4213,4297,4732,6910]
    
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
    user_data = user.resample('D').sum()
    userdata = user_data.interpolate(method='linear')
    userdata.dropna(inplace=True)
    userdata = userdata[userdata>0]
    ############ get log of data ########
    try:
        data_log = np.log(userdata)
        ts_log = data_log.replace([np.inf, -np.inf], np.nan)
        ts_day_log = ts_log.interpolate(method='linear')
        #### expected usage ######
        predictions =  predict(ts_day_log)
    except:
         predictions = []
    #### current month #######
    user_bill = user.resample('M').sum()
    user_bill = user_bill[user_bill>0]
    try:
        current_user_bill= user_bill[str(user_bill.tail(1).index[0])[:7]]
    except:
        current_user_bill = 0 
    i=1
    with open("/home/aya/Desktop/Aquapedia/Datasets/predictions/predictions.csv", "a") as myfile:
        for item in predictions:
            if len(str(i))==1:
                myfile.write(str(userdata.tail(1).index[0])[:7]+'-0'+str(i))
            else:
                myfile.write(str(userdata.tail(1).index[0])[:7]+'-'+str(i))
            myfile.write(',%d,%d' % (int(userID),current_user_bill))
            myfile.write(",%d " % item)
            i+=1
            myfile.write('\n')
eval(sys.argv[1])