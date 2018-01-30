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

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
Matrix1 = [0 for x in range(2)]
Matrix2 = [0 for x in range(2)]
Matrix3= [0 for x in range(2)]
Biglist=[]
i=0
v=0
num=1
minlist=[]
def NeighbourComparison(customerid):
        global data
        global num
        global minlist

        if  94 <= customerid and customerid <= 865 :
            data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockT.csv',parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
        elif 1103 <= customerid and customerid <= 2034 :
            data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockC.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
        elif 2064 <= customerid and customerid <= 3310 :
            data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockG.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
        elif 3367 <= customerid and customerid <= 6910 :
            data = pd.read_csv('/home/aya/Desktop/Aquapedia/Datasets/blockA.csv', parse_dates= ['localminute'], index_col='localminute',date_parser=dateparse)
    

        group = data.groupby('dataid')
        a = [0 for x in range(12)] 
        user2 = group.get_group(int(customerid))
        user = group.get_group(int(customerid))['meter_value']
        userdata = user.resample('M').sum()
        userdata=userdata[userdata>= 0]
        userdat = userdata.interpolate(method='linear')
        row = userdat.tail(1)
        date = str(row.index[0])[:4]
        Ncustomers=len(group)        
        Liters = [0 for x in range(12)]
        i=0
        num=1

        while num <=12:
            
            try:
                    if num >=1 and num <= 9 :   
                            Liters[i]=userdat['%d-0%d' %(int(date), num)][0]
                            num=num+1
                            i=i+1          
                    else :
                            Liters[i]=userdat['%d-%d' %(int(date), num)][0]
                            num=num+1
                            i=i+1
                        
            except:
                Liters[i]=0
                num=num+1
                i=i+1
                
        Matrix1[0]="You"
        Matrix1[1]=Liters
        Biglist.append(Matrix1)
            
        dataresa=data['meter_value']
        dataresa = dataresa.resample('M').sum()
        dataresa.dropna(inplace=True)
        dataresa=dataresa[dataresa>= 0]
    
        i=0
        num=1
        LitersNeigbours = [0 for x in range(12)]
        while num <=12:
            Ncustomers=len(group)  
            for k , t in group:
                nuser=group.get_group(k)['meter_value']
                nuser = nuser.resample('M').sum()
                nuser = nuser.interpolate(method='linear')    
                try :
                    if num >=1 and num <= 9 :
                        nuser= nuser['%d-0%d' %(int(date), num)]
           
                    else:
                        nuser=nuser['%d-%d' %(int(date), num)][0]
                    
                except:
                     Ncustomers=Ncustomers-1
                    
            try:
                    if num >=1 and num <= 9 :   
                            LitersNeigbours[i]=dataresa['%d-0%d' %(int(date), num)][0]
                            LitersNeigbours[i]=LitersNeigbours[i]/Ncustomers
                            num=num+1
                            i=i+1    
                    else :
                            LitersNeigbours[i]=dataresa['%d-%d' %(int(date), num)][0]
                            LitersNeigbours[i]=LitersNeigbours[i]/Ncustomers
                            num=num+1
                            i=i+1
                        
            except:
                LitersNeigbours[i]=0
                i=i+1
                num=num+1
            
        Matrix2[0]="Nearest neighbours"
        Matrix2[1]=LitersNeigbours
        Biglist.append(Matrix2)
        
        num=1
        while num <= 12:
            w=[]
            for k , t in group: 
                i=0
                if k!=customerid:
                    try:   
                        a[i]=group.get_group(k)['meter_value']
                        a[i] = a[i].resample('M').sum()
                        a[i].dropna(inplace=True)
                        a[i]=a[i][a[i] >= 0]
                        a[i] = a[i].interpolate(method='linear')
                        if num >=1 and num <= 9 :   
                            a[i]=a[i]['%d-0%d' %(int(date), num)][0]
                        else :
                            a[i]=a[i]['%d-%d' %(int(date), num)][0]
                        w.append(a[i])
                        i=i+1
                    except:
                        q=0
                    

            try:
                
                minlist.append(min(w))
            except:
                minlist.append(0)
                
            
            num=num+1
      

        Matrix3[0]="Efficient neighbours"
        Matrix3[1]=minlist
        Biglist.append(Matrix3)
        return Matrix1, Matrix2, Matrix3

You, Neighbours, Efficient= eval(sys.argv[1])
#myRoundedList = [ round(elem, 2) for elem in consumption[0]['You'] ]
print 'You=' , You[1]
print 'Neighbours=' , Neighbours[1]
print 'Efficient Neighbours=' , Efficient[1]