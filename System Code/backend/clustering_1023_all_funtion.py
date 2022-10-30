import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#######################


def cluster_decision(p_des,hour,minute):
    ##############
    # time integration
    ##############
    p_time=(int(hour)-17)*60+int(minute)
    
    ########################
    # import origin datasert
    ########################
    
    num_Rows_Read = None
    taxi_stand = pd.read_csv('taxistop_SG_rename.csv', delimiter=',', nrows = num_Rows_Read)
        
        # def __init__(self):
        #     # self 
        #     return None
        #clean function
        # def clean_null(df):#clean null rows
    def clean_null(df):#clean null rows
        df = df.dropna(how = 'any', axis = 'rows')
        return df
    taxi_stand_all=clean_null(taxi_stand)
        
        #############################
        ### latlon separate
        ##############################
        #获取经纬度信息
    jwd=pd.DataFrame()
    jwd['lat']=taxi_stand_all['lat']
    jwd['lon']=taxi_stand_all['lon']
    #将经纬度信息转换成numpy.ndarray以便算法实施
    jwdnp=jwd.values
        
        
        ###########################
        # clustering
        ############################
    map=plt.imread('SGmap.png')
    from matplotlib.image import Bbox
    Bbox = (103.6048, 104.035, 1.2090, 1.4751)
    def plot_on_map(jwdnp,BB,map,s=10,alpha=0.2,c='c',dic=1):
        fig,axs=plt.subplots(1,figsize=(16,10))
        scatter1=plt.scatter(jwdnp[:,1],jwdnp[:,0],c=c,cmap='tab10',zorder=1,alpha=alpha,s=s)# s：标记大小，以平方磅为单位的标记面积,c:标记颜色,zorder：图层：1为最上层，alpha：透明度，1不透明
        axs.set_xlim((BB[0],BB[1]))#longtitude limit
        axs.set_ylim((BB[2],BB[3]))#latitude limit
        axs.set_title('Kmeans')
        plt.colorbar(scatter1)#legend for each class
        axs.imshow(map, zorder=0, extent=BB)#extent为原点位置
            
        ############
        # kmeans
        ############
    from sklearn.cluster import KMeans
        
    kmeans_jwd2 = KMeans(n_clusters=10, random_state=2).fit_predict(jwdnp)
        # plt.scatter(jwdnp[:,1],jwdnp[:,0],c=kmeans_jwd2,cmap='tab10')
        # plt.colorbar()
    # plot_on_map(jwdnp,Bbox,map,s=50,alpha=1,c=kmeans_jwd2,dic=18)
        
        # print(metrics.calinski_harabasz_score(jwdnp,kmeans_jwd2))
        
        ############
        # change wrong clusters
        ############
        
        #  append cluster tag
        
    taxi_stand_all=taxi_stand_all.drop(['No.','tags'],axis=1)
    taxi_stand_all['cluster']=pd.DataFrame(kmeans_jwd2)
        
        # change wrong cluster tag
        
    taxi_stand=taxi_stand_all
        # clementi
    taxi_stand.loc[taxi_stand['id']==1559274111,'cluster']=3
        # bukit timah
    taxi_stand.loc[taxi_stand['id']==1579304828,'cluster']=6
    taxi_stand.loc[taxi_stand['id']==3800199447,'cluster']=6
        
        # redraw clustering map
    # plot_on_map(jwdnp,Bbox,map,s=50,alpha=1,c=taxi_stand['cluster'],dic=18)
        
        ############
        # put clusters into a bigger cluster
        ############
        
    taxi_stand.loc[taxi_stand['cluster']==6,'cluster']=2
    taxi_stand.loc[taxi_stand['cluster']==9,'cluster']=1
    taxi_stand.loc[taxi_stand['cluster']==5,'cluster']=4
    taxi_stand.loc[taxi_stand['cluster']==7,'cluster']=4
    taxi_stand.loc[taxi_stand['cluster']==8,'cluster']=4
        
        
        ############
        # append direction information
        ############
    taxi_stand['direction']=taxi_stand['cluster']
    taxi_stand.loc[taxi_stand['cluster']==0,'direction']='Harbourfront'
    taxi_stand.loc[taxi_stand['cluster']==1,'direction']='Punggol'
    taxi_stand.loc[taxi_stand['cluster']==2,'direction']='Woodlands'
    taxi_stand.loc[taxi_stand['cluster']==3,'direction']='Joo Koon'
    taxi_stand.loc[taxi_stand['cluster']==4,'direction']='Changi Airport'
    # plot_on_map(jwdnp,Bbox,map,s=50,alpha=1,c=taxi_stand['cluster'],dic=18)
    
    #     # save to csv
    # path = 'cluster_result.csv'
    # taxi_stand.to_csv(path,index=False)   
        ###########
        # load 26 destinations
        ###########
    taxi_terminal_all = pd.read_csv('terminal_1.csv', delimiter=',')
    taxi_term=pd.DataFrame(taxi_terminal_all)
    taxi_term.drop(taxi_term.index[(taxi_term['name'] == 'University town')], inplace=True)
        
        ###########
        # destination name change and cluster append
        ###########
    for i in range(len(taxi_term)):
        ida=taxi_term.iloc[i]['id']
        namea=taxi_stand[taxi_stand['id']==ida]['name'].values[0]
        clua=taxi_stand[taxi_stand['id']==ida]['cluster'].values[0]
        directiona=taxi_stand[taxi_stand['id']==ida]['direction'].values[0]
        taxi_term.loc[taxi_term['id']==ida,'direction']=directiona
        taxi_term.loc[taxi_term['id']==ida,'name']=namea
        taxi_term.loc[taxi_term['id']==ida,'cluster']=clua
         
        
    
    
        
        ###########
        # Virtual customer
        ###########
        
        # # generate time from 17pm to 24pm
        # list_time=[]
        # for i in range(7*60):
        #     list_time.append(i)
        
        # # generate destination
        # list_destination=[]
        # list_destination=taxi_stand['name'].tolist()
        
        # # generate all destination in different hour
        # # numpy.random.randint(low, high=None, size=None, dtype=‘l')
        # # np.random.randint(0, len(taxi_stand), size=len(taxi_stand))
        # v=np.random.randint(0, len(taxi_stand), size=420).tolist()
        # name_list=taxi_stand['name'].tolist()
        # d=[]
        # t=[]
        # for i in range(len(v)):
        #     d.append(name_list[v[i]])
        #     t.append(i)
            
            
        # #  generate 26 destination in different hour
        # v_d=np.random.randint(0, len(taxi_term), size=420*len(taxi_term)).tolist()
        # name_list_des=taxi_term['name'].tolist()
        # d_d=[]
        # t_d=[]
        # for i in range(len(v_d)):
        #     d_d.append(name_list_des[v_d[i]])
        #     t_d.append(i//len(taxi_term))
            
        # # concat to new features
        # user1 = pd.DataFrame(t, columns=['time'])
        # user1['destination']=pd.DataFrame(d)
        
        # user2 = pd.DataFrame(t_d, columns=['time'])
        # user2['destination']=pd.DataFrame(d_d)
    
        # user = pd.concat([user1,user2],axis=0)
        
        # # reset user set index and set name
        # user = user.sort_values(by='time',ascending=True)
        # user = user.reset_index(drop=True)
        # user_list=user.index.values
        # user['user id'] = pd.DataFrame(user_list)
        
        # # save virtual user dataset
        # path = 'user_dataset.csv'
        # user.to_csv(path,index=False)
        
        
        
        ############
        # taxi share rules
        ############
        
    ########
    # import passenger
    ########
    pas_dic_v = pd.read_csv('user_dataset.csv', delimiter=',', nrows = num_Rows_Read)
    # pas_dic_len=len(pas_dic_v)
    # p_name = (pas_dic_v['user id'][11100])
    # p_des = str(pas_dic_v['destination'][5500])#5600 share true
    # p_time = (pas_dic_v['time'][5500])#5600 share true
    def time_ind(p_time):
        time_index=pas_dic_v[pas_dic_v['time']==p_time]['user id'].to_list()
        return time_index
    
    def taxi_share_check(p_des,p_time,pas_dic_v,taxi_stand):
        pas_dic_len=len(pas_dic_v)
        p_clu=taxi_stand[taxi_stand['name']==p_des]['cluster'].values[0]
        #########
        # rules set
        #########
        # def share_decide(time,des,dataset,taxi_stand_all):
         
        
        num=0
        des_t=[]
        # example cluster
        timestart=0 # starting time of dataset
        timestop=419
        
        if (p_time-timestart>30) & (timestop-p_time>30):#time between >30
          for i in range(time_ind(p_time+29)[-1]-time_ind(p_time-30)[0]+1):#time range
            aa0=pas_dic_v.iloc[time_ind(p_time-30)[0]+i]['destination']# i destination
            aa1=taxi_stand[taxi_stand['name']==aa0]['cluster'].values[0]#i cluster
        
            if num < 3:      #people in
                if p_clu == aa1:
                      num+=1
                      des_t.append(aa0)
            else:
                break
            
        if (p_time-timestart<=30) :#time before>30
          for i in range(time_ind(p_time+29)[-1]+1):#time range
            aa0=pas_dic_v.iloc[i]['destination']# i destination
            aa1=taxi_stand[taxi_stand['name']==aa0]['cluster'].values[0]#i cluster
        
            if num < 3:      #people in
                if p_clu == aa1:
                      num+=1
                      des_t.append(aa0)
            else:
                break
        
        if (timestop-p_time<=30) :#time before>30
          for i in range(pas_dic_len-time_ind(p_time-30)[0]+1):#time range
            aa0=pas_dic_v.iloc[time_ind(p_time-30)[0]+i]['destination']# i destination
            aa1=taxi_stand[taxi_stand['name']==aa0]['cluster'].values[0]#i cluster
        
            if num < 3:      #people in
                if p_clu == aa1:
                      num+=1
                      des_t.append(aa0)
            else:
                break
        return des_t
    #######
    share=taxi_share_check(p_des,p_time,pas_dic_v,taxi_stand)
    
    ##################
    # destination calculation
    ##################
    def distance(lat2,lon2):
        lat1=1.3061645
        lon1=103.7739761
        p = 0.017453292519943295 # Pi/180
        a = 0.5 - np.cos((lat2 - lat1) * p)/2 + np.cos(lat1 * p) * np.cos(lat2 * p) * (1 - np.cos((lon2 - lon1) * p)) / 2
        return 0.6213712 * 12742 * np.arcsin(np.sqrt(a))
    def destination_find(p_des,share):
        passenger_all_des=[p_des]+share
        # print(passenger_all_des)
        lat=taxi_stand[taxi_stand['name']==passenger_all_des[0]]['lat'].values[0]
        lon=taxi_stand[taxi_stand['name']==passenger_all_des[0]]['lon'].values[0]
        
        lat1=taxi_stand[taxi_stand['name']==passenger_all_des[1]]['lat'].values[0]
        lon1=taxi_stand[taxi_stand['name']==passenger_all_des[1]]['lon'].values[0]
        
        lat2=taxi_stand[taxi_stand['name']==passenger_all_des[2]]['lat'].values[0]
        lon2=taxi_stand[taxi_stand['name']==passenger_all_des[2]]['lon'].values[0]
        
        lat3=taxi_stand[taxi_stand['name']==passenger_all_des[3]]['lat'].values[0]
        lon3=taxi_stand[taxi_stand['name']==passenger_all_des[3]]['lon'].values[0]
        
        dis0=distance(lat,lon)
        dis1=distance(lat1,lon1)
        dis2=distance(lat2,lon2)
        dis3=distance(lat3,lon3)
        dis=[dis0,dis1,dis2,dis3]
        # print(dis)
        a=0
        b=0
        for i in range(len(dis)):
            if dis[i]>a:
                a=dis[i]
                b=i
        return passenger_all_des[b]
    des = destination_find(p_des,share) 
    ##################
    # taxi share route catch
    ##################
    def route_generate(taxi_term,p_des,share,des):
        dest=[]
        term=taxi_term['name'].tolist()
        passenger_all_des=[p_des]+share
        for i in range(len(passenger_all_des)):
            if passenger_all_des[i] not in term:
                # print('Function still unfinished')
                dest='Function still unfinished'
                break          
            else:
                dest=p_des              
        return dest
    # print(list(taxi_stand))
    direction=taxi_stand[taxi_stand['name']==des]['direction'].values[0]
    return [route_generate(taxi_term,p_des,share,des),direction,len(share)]
  
    
# ####js print result
#     const cluster_decision_result=cluster_decision(p_des,hour,minute)
#     console.log(
#         "Dear user, you will share your trip with",cluster_decision_result[2],"other passengers in the direction of ",cluster_decision_result[1],
#         "the destination will be",cluster_decision_result[0]
#         );

#     console.log("Number of taxi sharing passengers: "cluster_decision_result[2],"; Trip direction: ",cluster_decision_result[1],"; Trip destination: ",cluster_decision_result[0]);
#     console.log("The route map is still under development");          


        




