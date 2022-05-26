'''
Filename: c:\python\bike_prediciton\reomove_nonsense0.py
Path: c:\python\bike_prediciton
Created Date: Friday, May 21st 2021, 12:46:04 am
Author: SEELE a317

Copyright (c) 2021 625, 7, Youyuan
'''

import pandas as pd
import math
import time
from alive_progress import alive_bar
import numpy
shapefile = pd.read_csv('sg_map.csv')
shapefile.set_index('id')

good0_data = pd.read_csv('1.csv')


def distance(id1, id2):
    Lat_A = shapefile.loc[id1]['Lat']
    Lon_A = shapefile.loc[id1]['Lon']
    Lat_B = shapefile.loc[id2]['Lat']
    Lon_B = shapefile.loc[id2]['Lon']
    C = math.sin(Lat_A)*math.sin(Lat_B)*math.cos(Lon_A-Lon_B) + \
        math.cos(Lat_A)*math.cos(Lat_B)
    return 6371.004*math.acos(C)*math.pi/180

global full
full = len(good0_data)

# with alive_bar(len(good0_data)) as bar:
#     for i in range(len(good0_data)):
#         try:
#             if good0_data.loc[i]['trip_m6_wd_pm']==0:
#                 id1=good0_data.loc[i]['ori']
#                 id2=good0_data.loc[i]['dst']
#                 dis=distance(id1,id2)
#                 print(dis)
#                 if dis>=3.5:
#                     good0_data=good0_data.drop([i])
#         except:
#             continue
#         bar()

# with alive_bar(len(good0_data)) as bar:
#     for i in range(len(good0_data)):
#         row = good0_data.iloc[i]
#         if row['trip_m6_wd_pm'] == 0:
#             dis = row['dist_km']
#             if dis >= 3.5:
#                 good0_data.drop([i],inplace=True)
#         bar()

processed=pd.DataFrame(columns=('ori','dst','dist_km','fsize_m6_wd_pm','trip_m6_wd_pm',
                                'community_m6','mrt_km_o','entro_o','cycle_km_o',
                                'far_hdb_o','far_priv_o','far_comm_o','mrt_km_d',
                                'entro_d','cycle_km_d','far_hdb_d','far_priv_d','far_comm_d'))
zeros=numpy.zeros(full)
limit=numpy.array([3.5 for i in range(full)])
print(type(limit), type(zeros))

def drop_0row(i,trip,dis):
    print(type(i),type(trip),type(dis))
    tar1=trip==zeros
    tar2=dis>=limit
    return tar1,tar2
index=[]
def func(tar1,tar2):
    with alive_bar(full) as bar:
        for x in range(len(tar1)):
            if tar1[x] and tar2[x]:
                pass
            else:
                index.append(x)
            bar()
    return numpy.array(index)
    
    
tar1,tar2=drop_0row(range(len(good0_data)),good0_data['trip_m6_wd_pm'].values,good0_data['dist_km'].values)

processed=good0_data.loc[func(tar1,tar2)]

processed.to_csv(path_or_buf='0_removed.csv')

