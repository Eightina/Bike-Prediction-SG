'''
Filename: c:\python\bike_prediciton\margin_effect.py
Path: c:\python\bike_prediciton
Created Date: Thursday, May 20th 2021, 4:23:56 pm
Author: SEELE a317

Copyright (c) 2021 625, 7, Youyuan
'''
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import pandas as pd
import torch
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



# n_data = pd.read_csv('new_data.csv')

# n_data=n_data[n_data['trip']!=0]

# trip = n_data['trip']
# f_size = n_data['f_size']

# cal = []

columns=['ori','dst','dist_km','fsize_m6_wd_pm','trip_m6_wd_pm',
                                'community_m6','mrt_km_o','entro_o','cycle_km_o',
                                'far_hdb_o','far_priv_o','far_comm_o','mrt_km_d',
                                'entro_d','cycle_km_d','far_hdb_d','far_priv_d','far_comm_d']


# sns.lmplot(x="f_size", y="trip", data=n_data)

# for i in range(len(n_data)):
#     cal.append(trip.iloc[i]/f_size.iloc[i])
# plt.plot(cal, f_size, 'ro')
# plt.show()

def avg_cost():
    good0_data=pd.read_csv('0_removed.csv')
    
    y=good0_data['trip_m6_wd_pm']
    columns.remove('trip_m6_wd_pm')
    X=good0_data[columns]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
    good0_data=pd.concat([X_test,y_test],axis=1)
    
    trip2 = good0_data['trip_m6_wd_pm']
    f_size2 = good0_data['fsize_m6_wd_pm']
    for i in range(len(good0_data)):
        cal.append(trip2.iloc[i]/f_size2.iloc[i])
    cal_dic={'cal':cal}
    cal=pd.DataFrame(cal_dic)
    good0_data=pd.concat([good0_data,cal],axis=1)
    sns.lmplot(x="fsize_m6_wd_pm", y='cal', data=good0_data, hue='community_m6')


def group_cal0():
    good0_data=pd.read_csv('0_removed.csv').sort_values('fsize_m6_wd_pm')
    
    y=good0_data['trip_m6_wd_pm']
    columns.remove('trip_m6_wd_pm')
    X=good0_data[columns]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
    good0_data=pd.concat([X_test,y_test],axis=1)
    
    good0_data=good0_data.sort_values('fsize_m6_wd_pm')
    
    f_size=good0_data['fsize_m6_wd_pm'].values
    trip=good0_data['trip_m6_wd_pm'].values
    mr=[]
    
    for i in range(1,len(f_size)):
        mr.append((trip[i]-trip[i-1])/(f_size[i]-f_size[i-1]))
    mr.append(0)


def sample(data,ratio):
    y=data['trip_m6_wd_pm']
    columns.remove('trip_m6_wd_pm')
    X=data[columns]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=ratio)
    return (pd.concat([X_test,y_test],axis=1))
    
    
    
def group_cal():
    good0_data=pd.read_csv('0_removed.csv').sort_values('fsize_m6_wd_pm')
    good0_data.index=range(len(good0_data))
    f_size=good0_data['fsize_m6_wd_pm'].values
    trip=good0_data['trip_m6_wd_pm'].values
    scheckpoint=[]
    trip_data=[]
    for i in range(len(good0_data)):
        if f_size[i]!=f_size[i-1]:
            scheckpoint.append(i)
    for i in range(len(scheckpoint)):
        p=scheckpoint[i]
        clip=np.array(range(scheckpoint[i-1],p))
        avg_trip=sum(trip[scheckpoint[i-1]:p])/(p-scheckpoint[i-1]+1)
        trip_data+=[avg_trip for i in clip]
    good0_data.index=range(len(good0_data))
    good0_data=good0_data[0:194528]
    good0_data['avg_trip']=trip_data

    f_size=good0_data['fsize_m6_wd_pm']
    avg_trip=good0_data['avg_trip']
    mr=[]
    f_size2=[]
    for i in range(1,len(f_size)):
        if f_size[i]!=f_size[i-1]:
            mr.append((trip[i]-trip[i-1])/(f_size[i]-f_size[i-1]))
            f_size2.append(f_size[i-1])

    plt.plot(f_size2, mr,'bo')
    good0_data.to_csv('fuck.csv')


# good0_data=pd.read_csv('0_removed.csv').sort_values('fsize_m6_wd_pm')
# good0_data.index=range(len(good0_data))
# f_size=good0_data['fsize_m6_wd_pm'].values
# trip=good0_data['trip_m6_wd_pm'].values




columns=['ori','dst','dist_km','fsize_m6_wd_pm','trip_m6_wd_pm',
                                'community_m6','mrt_km_o','entro_o','cycle_km_o',
                                'far_hdb_o','far_priv_o','far_comm_o','mrt_km_d',
                                'entro_d','cycle_km_d','far_hdb_d','far_priv_d','far_comm_d']
good0_data=pd.read_csv('0_removed.csv').sort_values('fsize_m6_wd_pm')
good0_data.index=range(len(good0_data))
# f_size=good0_data['fsize_m6_wd_pm'].values
# trip=good0_data['trip_m6_wd_pm'].values

def group_plot(data,groupby,ratio):
    # data=sample(data,ratio)
    cut_tar=data[groupby].values
    bins=[-0.1]+list(data[groupby].describe()[4:8])
    # cut_res=pd.cut(cut_tar,bins=bins,labels=['a','b','c','d'])
    cut_res=pd.cut(cut_tar,bins=bins,labels=['a','b','c','d'])
    data['cat_var'+groupby]=cut_res
    sns.lmplot(data=data,x='fsize_m6_wd_pm',y='trip_m6_wd_pm',col='cat_var'+groupby,col_wrap=2)

#按分位数看不出来就聚类
    
def land_use():
    x1=good0_data['far_hdb_o'].values
    x1+=good0_data['far_priv_o'].values
    x1+=good0_data['far_comm_o'].values
    x1+=good0_data['far_hdb_d'].values
    x1+=good0_data['far_priv_d'].values
    x1+=good0_data['far_comm_d'].values
    good0_data['land_use']=x1

land_use()
group_plot(good0_data,'dist_km',0.5)