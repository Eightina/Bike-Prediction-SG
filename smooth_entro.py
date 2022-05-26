import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression 
from alive_progress import alive_bar

data=pd.read_csv('0_removed.csv')


sg_map=pd.read_csv('sg_map.csv')


sg_map_xy=sg_map.set_index(['xmin','xmax','ymin','ymax'])

find0_entro_o=data['entro_o'].values
find0_entro_d=data['entro_d'].values
ass=[0 for i in range(194661)]
is0_entro_o=(ass==find0_entro_o)
is0_entro_d=(ass==find0_entro_d)

coord=[]
result=[]
data_index_ori=data.set_index('ori')
sg_map_index_id=sg_map.set_index('id',drop=False)

with alive_bar(len(is0_entro_o)) as bar:
    for i in range(len(is0_entro_o)):
        neighbour_num=0
        neighbour_entro=0
        if is0_entro_o[i]:
            ori_id=data.loc[i]['ori']
            coord=list(sg_map_index_id.loc[ori_id][2:6])
            try:
                # upper=[coord[0],coord[1],coord[2]+0.0001,coord[3]+0.0001]
                nid=sg_map_xy.loc[coord[0],coord[1],round(coord[2]+300.0001,4),round(coord[3]+300.0001,4)]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_o'].values[0]
            except:
                pass
            try:
                # lower=[coord[0],coord[1],coord[2]-0.0001,coord[3]-0.0001]
                nid=sg_map_xy.loc[coord[0],coord[1],round(coord[2]-300.0001,4),round(coord[3]-300.0001,4)]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_o'].values[0]
            except:
                pass
            try:
                # left=[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]
                nid=sg_map_xy.loc[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_o'].values[0]
            except:
                pass
            try:
                # right=[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]
                nid=sg_map_xy.loc[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_o'].values[0]
            except:
                pass
            if not neighbour_num==0:
                result.append(neighbour_entro/neighbour_num)
            else:
                result.append(0)
        else:
            result.append(0)
        bar()
data['smooth_entro_o']=result+data['entro_o']




coord=[]
result=[]
data_index_dst=data.set_index('dst')
sg_map_index_id=sg_map.set_index('id',drop=False)
with alive_bar(len(is0_entro_d)) as bar:
    for i in range(len(is0_entro_d)):
        neighbour_num=0
        neighbour_entro=0
        if is0_entro_d[i]:
            dst_id=data.loc[i]['dst']
            coord=list(sg_map_index_id.loc[dst_id][2:6])
            try:
                # upper=[coord[0],coord[1],coord[2]+0.0001,coord[3]+0.0001]
                nid=sg_map_xy.loc[coord[0],coord[1],round(coord[2]+300.0001,4),round(coord[3]+300.0001,4)]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_d'].values[0]
            except:
                pass
            try:
                # lower=[coord[0],coord[1],coord[2]-0.0001,coord[3]-0.0001]
                nid=sg_map_xy.loc[coord[0],coord[1],round(coord[2]-300.0001,4),round(coord[3]-300.0001,4)]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_d'].values[0]
            except:
                pass
            try:
                # left=[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]
                nid=sg_map_xy.loc[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_d'].values[0]
            except:
                pass
            try:
                # right=[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]
                nid=sg_map_xy.loc[coord[0]-0.0001,coord[1]-0.0001,coord[2],coord[3]]['id']
                neighbour_num+=1
                neighbour_entro+=data_index_ori.loc[nid]['entro_d'].values[0]
            except:
                pass
            if not neighbour_num==0:
                result.append(neighbour_entro/neighbour_num)
            else:
                result.append(0)
        else:
            result.append(0)
        bar()

data['smooth_entro_d']=result+data['entro_d']
data.to_csv('smooth_entro.csv')