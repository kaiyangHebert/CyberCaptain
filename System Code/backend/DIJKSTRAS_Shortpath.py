# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:08:47 2022

@author: 233
"""

import pandas as pd
import geopy.distance
# pip install Image
# pip install matplotlib
import matplotlib.pyplot as plt
from PIL import Image
start_point='University town'
end_point='Sengkang Station G18'

def DIJKSTRAS_Shortpath(start_point,end_point):
  
  
  # singapore_img = Image.open(r"C:\Users\lenovo\Desktop\singapore-map-4.png")
  
  ########
  # 
  singapore_img = Image.open("./sg_route_map_background.png")
  # df5 = pd.read_csv('C:\Users\lenovo\Desktop\ad_taxistop.csv',sep=',', encoding='latin-1')
  # df5 = pd.read_csv( r"C:\Users\lenovo\Desktop\ad_taxistop.csv",sep=',', encoding='latin-1')
  # df5 = pd.read_csv( r"C:\Users\lenovo\Desktop\ad_sg.csv",sep=',', encoding='latin-1')
  df5 = pd.read_csv( "./ad_sg.csv",sep=',', encoding='latin-1')
  # df = pd.read_csv(r"C:\Users\lenovo\Desktop\terminal.csv", sep=',', encoding='latin-1')
  df = pd.read_csv("./terminal.csv", sep=',', encoding='latin-1')
  #显示所有列
  # pd.set_option('display.max_columns', None)
  # #显示所有行
  # pd.set_option('display.max_rows', None)
  # df5.head(100)
  # print(df5)
  str1=start_point
  str2=end_point
  index1 = df[df.name == str1].index.tolist()[0]  
  index2 = df[df.name == str2].index.tolist()[0]  
  start=int(index1)
  end=int(index2)
  index4=start+end
  print(index4)
  ad=df5.values.tolist()

  # ad[1][2]=1
  # ad[1][9]=1
  # ad[9][10]=1
  # ad[2][4]=1
  # ad[2][5]=1
  # ad[3][4]=1
  # ad[0][6]=1
  # ad[6][7]=1
  # ad[7][8]=1
  # ad[8][11]=1
  # ad[7][11]=1
  # ad[11][12]=1
  # ad[12][13]=1
  # ad[12][16]=1
  # ad[12][17]=1
  # ad[12][14]=1
  # ad[14][17]=1
  # ad[17][20]=1
  # ad[17][15]=1
  # ad[15][20]=1
  # ad[15][18]=1
  # ad[15][19]=1
  # ad[20][21]=1
  # ad[14][21]=1
  # ad[21][24]=1
  # ad[21][23]=1
  # ad[23][24]=1
  # ad[24][25]=1
  # ad[23][26]=1
  # ad[14][22]=1
  # ad[5][10]=1
  # ad[2][9]=1
  # ad[6][9]=1
  # ad[8][14]=1
  # ad[13][16]=1
  # ad[16][17]=1
  # ad[16][18]=1
  # ad[18][19]=1
  # ad[0][11]=1
  # ad[11][14]=1
  # ad[2][3]=1
  # ad[4][5]=1
  # ad[22][21]=1
  # ad[22][23]=1
  # ad[22][26]=1
  # ad[25][26]=1
  # ad[0][13]=1
  # for i in range(len(ad)):
  #   for j in range(len(ad)):
  #       if (i!=j) &(ad[i][j]==1):
  #         ad[j][i]=ad[i][j]
  # df6=pd.DataFrame(ad)
  # PATH=r'C:\Users\lenovo\Desktop\ad1.csv'
  # df6.to_csv(path_or_buf=PATH, sep=',', na_rep='', float_format=None, columns=None, 
  #               header=False, index=False, index_label=None, mode='w', encoding=None, 
  #              compression=None, quoting=None, quotechar='"', line_terminator='\n', 
  #             )
  ad_dist=ad
  distances=ad
  # print(ad)
  # print(df5)
  for i,row in df.iterrows(): # A
      a = row.lat, row.lon
      
      for j,row2 in df.iterrows(): 
        if ad_dist[i][j]==1:
          b = row2.lat, row2.lon
          distances[i][j]=geopy.distance.geodesic(a, b).km
          distances[j][i]=geopy.distance.geodesic(a, b).km

  for i in range(len(distances)):
    for j in range(len(distances)):
          distances[i][j]=round(distances[i][j],2)

  for i in range(len(distances)):
    for j in range(len(distances)):
        if i==j:
          distances[i][j]=1

  import numpy as np
  for  i in range(len(distances)):
      for j in range(len(distances)):
        if distances[i][j] ==0.00:
                distances[i][j] =np.inf

  for i in range(len(distances)):
    for j in range(len(distances)):
        if i==j:
          distances[i][j]=0.00
  df7=pd.DataFrame(distances)
  # print(df7)
  # print(distances)
  # dist = geopy.distance.geodesic((1.306164, 103.773976), (1.314730, 103.765150)).km
  # path_or_buf : 文件路径，如果没有指定则将会直接返回字符串的 json
  #   sep : 输出文件的字段分隔符，默认为 “,”
  #   na_rep : 用于替换空数据的字符串，默认为''
  #   float_format : 设置浮点数的格式（几位小数点）
  #   columns : 要写的列
  #   header : 是否保存列名，默认为 True ，保存
  #   index : 是否保存索引，默认为 True ，保存
  # # ————————————————

  ad_matrix=distances
  # print(ad_matrix)
  # for  i in range(6):
  #     for j in range(6):
  # 	    if ad_matrix[i][j] ==-1:
  #               ad_matrix[i][j] =np.inf
  # print(ad_matrix)
  def takeSecond(elem):
      return elem[1]
  rel=[]
  node_cost = [[np.inf for i in range(0, 3)] for i in range(0, 27)]
  # print(node_cost)
  for i in range(0, 27):
      node_cost[i][0] = i

  outloop=False
  node0=int(start)
  for i in range(0, 27):
      if ad_matrix[int(node0)][i] < node_cost[i][1]:
          node_cost[i][2] = node0
          node_cost[i][1] = ad_matrix[int(node0)][i]
  rel.append(int(node0))
  # print(node_cost)
  while outloop==False:
      node_cost = np.array(node_cost)  # 将node_cost从list转换成array
      open_list = list(set(node_cost[:, 0].tolist()) - set(rel))  # 建立一个open_list放入没有被遍历的点
      # print(open_list)
      final_list = []
      for i in open_list:
          final_list.append(node_cost[int(i)].tolist())
      final_list.sort(key=takeSecond)
      node0=final_list[0][0]
      node0=int(node0)
      # print(node_cost)
      for i in range(0, 27):
          if ad_matrix[node0][i] + node_cost[node0][1] < node_cost[i][1]:
              node_cost[i][2] = node0
              node_cost[i][1] = ad_matrix[node0][i] + node_cost[node0][1]
      # print(node_cost)
      rel.append(node0)
      # print(rel)
      if end in rel:
        outloop=True
  # print(node_cost)
  xn = int(end)
  x0 = int(start)
  destination_list = [xn]
  print("最短的路径代价为:", node_cost[xn][1])
  cost=node_cost[xn][1]
  cost=round(cost,2)
  while x0 not in destination_list:
      xn = int(node_cost[xn][2])
      destination_list.append(xn)
  print("最短路径为：", destination_list)
  destination_ls=[]
  for i in range(len(destination_list)):
      index3=destination_list[i]
      destination_ls.append(df['name'][index3])
  # print(destination_ls)
  
  # 
  ax = df.plot.scatter(
      x="lon", 
      y="lat", 
      figsize=(20,14),
      c='b',
      s=90,
      colorbar=False, 
      alpha=0.8,
      zorder=2
      
  )
  for i in range(len(destination_list)-1):
    a=df.iloc[destination_list[len(destination_list)-(i+1)],3]
    c=df.iloc[destination_list[len(destination_list)-(i+2)],3]
    b=df.iloc[destination_list[len(destination_list)-(i+1)],2]
    d=df.iloc[destination_list[len(destination_list)-(i+2)],2]
    # 
    plt.plot([a, c], [b, d], c='r', linewidth=7,linestyle='solid',alpha=1,zorder=1)

  # use our map with it's bounding coordinates
  # 
  extent=[103.6804, 103.9986, 1.2613, 1.4023]
  plt.imshow(singapore_img, extent=[103.6804, 103.9986, 1.2613, 1.4023], alpha=0.6,zorder=0) 
  # plt.imshow(singapore_img, extent=[103.5,104,1.15, 1.50], alpha=0.5)           
  # add axis labels
  plt.ylabel("Latitude", fontsize=20)
  plt.xlabel("Longitude", fontsize=20)
  # set the min/max axis values - these must be the same as above
  # 
  plt.ylim(extent[2], extent[3])
  plt.xlim(extent[0], extent[1])
  # 
  plt.xticks([]) 
  plt.yticks([]) 
  plt.legend(fontsize=20)
  plt.axis("off")
  plt.savefig('./Dij_shortpath%(index1)s%(index2)s.png'% {'index1': index1,'index2': index2}, bbox_inches='tight', pad_inches=0.0)
  
  path='./Dij_shortpath%(index1)s%(index2)s.png'% {'index1': index1,'index2': index2}

  destination_sequence=''
  for i in range(len(destination_ls)):
      destination_sequence = destination_sequence+destination_ls[-1-i]+" → "
  destination_sequence=destination_sequence[0:-2]
  
  return [path,cost,destination_sequence]




print(DIJKSTRAS_Shortpath(start_point,end_point))