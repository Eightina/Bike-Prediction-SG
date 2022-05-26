'''
Filename: c:\python\bike_prediciton\preprocessor.py
Path: c:\python\bike_prediciton
Created Date: Thursday, May 20th 2021, 8:54:45 am
Author: SEELE a317

Copyright (c) 2021 625, 7, Youyuan
'''
import pandas as pd
from alive_progress import alive_bar

og_data=pd.read_csv('0_removed.csv')


og_data=og_data.sort_values(by='ori')
og_datax=og_data
use_cnt={}
with alive_bar(len(og_datax)) as bar:
    for i in range(len(og_datax)):
        row=og_datax.iloc[i]
        if not use_cnt.get(row['ori']):
            use_cnt[row['ori']]=[row['trip_m6_wd_pm'],row['fsize_m6_wd_pm']]
        else:

            use_cnt[row['ori']][0]+=row['trip_m6_wd_pm']
        bar()

# og_data=og_data.sort_values(by='dst')
# og_datay=og_data
# arrival_cnt={}

# with alive_bar(len(og_datay)) as bar:
#     for i in range(len(og_datay)):
#         row=og_datay.iloc[i]
#         if not arrival_cnt.get(row[1]):
#             arrival_cnt[row[1]]=[row[4],row[3]]
#         else:
#             use_cnt[row[0]][0]+=row[4]
#             bar()

new_data={'ori':[],'trip':[],'f_size':[]}
with alive_bar(len(use_cnt)) as bar:
    for ori in use_cnt:
        new_data['ori'].append(ori)
        new_data['trip'].append(use_cnt[ori][0])
        new_data['f_size'].append(use_cnt[ori][1])
        bar()
        
n_data=pd.DataFrame(new_data).sort_values(by='ori')

n_data.to_csv(path_or_buf='new_data.csv')

