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

def predict(ts_day_log , orde):
    X = ts_day_log.values
    model = ARIMA(X, order=orde)
    model_fit = model.fit(transparams=True,trend='c',disp=False)
    predictions = model_fit.forecast(12)[0]
    return np.exp(predictions)

def company(block):
    dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
    i=0
    a = [0 for x in range(len(block))]
    for item in block:
            a[i] = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/block'+item[0]+'.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
            block_data = pd.DataFrame(a[i])
            
            com_d = block_data.resample('2H').sum()
            com_data = com_d.interpolate(method='linear')['meter_value']
            com_data.dropna(inplace=True)
            
            com_d_log = np.log(com_data)
            com_log = com_d_log.replace([np.inf, -np.inf], np.nan)
            com_log.dropna(inplace=True)
            
            if item == 'Tanta':
                order = (10, 1, 0)
            elif item == 'Cairo':
                order = (0, 1, 1)
            elif item == 'Gize':
                order = (8, 0, 2)
            else:
                order = (1, 0, 1)
                
            
            predictions =  predict(com_log, order)
            current = str(com_data.tail(1).index[0])[:10]
            x=0
            with open("/home/aya/Desktop/Aquapedia/Datasets/predictions/company_prediction.csv", "a") as myfile:
                for item_p in predictions:
                    if len(str(x))==1:
                        myfile.write(current+'-0'+str(x))
                    else:
                        myfile.write(current+'-'+str(x))
                    myfile.write(','+item)
                    myfile.write(",%d " % item_p)
                    x+=2
                    myfile.write('\n')
            i+=1

company(['Tanta','Giza', 'Alex', 'Cairo'])