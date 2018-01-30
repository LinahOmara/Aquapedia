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

def bill(userID):

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
    userd = user.resample('M').sum()
    userdata = userd.interpolate(method='linear')
    userdata = userdata[userdata>0]

    user_day = user.resample('D').sum()
    userday = user_day.interpolate(method='linear')
    userday= userday[userday>0]
    
    try:
        if int(str(userdata.tail(1).index[0])[8:10]) == int(str(userday.tail(1).index[0])[8:10]):
            row = userdata.tail(1)
        else:
            row = userdata.tail(2)
        cubic = row[0] * .00378541
        msg = ""
        #########################Tier##################################################################################################################
        if cubic <= 10:
            bill = cubic * 0.30
            tier = 1
            diff = 10 - cubic
            msg = 'your are ' + str(round(diff * 1000,1)) + ' Litre away from entering the HIGHST tier take cares and show tips to reduce your consumption'     
        elif cubic > 10 and cubic <= 20:
            bill = cubic * 0.70
            tier = 2
            diff = 20 - cubic
            if diff > 5:
                msg = 'Good, your are '+ round(diff * 1000,1) + ' Litre away from entering the LOWEST tier show tips to reduce your consumption'
            elif diff < 5:
                msg = 'Bad, your are ' + round(diff * 1000,1) + ' Litre away from entering the HIGHST tier take cares and show tips to reduce your consumption'
        elif cubic > 20 and cubic <= 40:
            bill = cubic * 1.05
            tier = 3
            diff = 40 - cubic
            if diff > 10:
                msg = 'Good, your are ' + round(diff * 1000,1) + ' Litre away from entering the LOWEST tier show tips to reduce your consumption'
            elif diff < 10:
                msg = 'Bad, your are ' + round(diff * 1000,1) + ' Litre away from entering the HIGHST tier take cares and show tips to reduce your consumption'
        else:
            bill = cubic * 1.55
            tier = 4
            diff = cubic - 40
            msg = 'you are in the highst tier, but by reducing your consumption by' + round(diff* 1000,1) + 'you will enter the LOWEST tier'
        ######################################################################################################################################################
        dat = str(row.index[0])[:10]
        return [dat, round(bill,1), tier, cubic], msg
    except:
        return None


arr, msg = eval(sys.argv[1])
print 'Bill=' , arr[1]
print 'Due to=' , arr[0]
print 'Current tier=', arr[2]
print 'Consumption in liters=' , arr[3]* 1000
print 'Tier Updates=' , msg

#date , use = bill('484') #liters
