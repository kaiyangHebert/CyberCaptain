from asyncio.windows_events import NULL
from flask import Flask,request,jsonify,send_file,url_for
from flask_cors import CORS
from MyGoogleMap import GoogleMaps
import datetime
import json
import sqlite3
import base64
from PIL import Image
from DIJKSTRAS_Shortpath import DIJKSTRAS_Shortpath
from clustering_1023_all_funtion import cluster_decision
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import pandas as pd
import yaml
import numpy as np
import os

app = Flask(__name__)
CORS(app)

carpool_chatbot = ChatBot('Carpool system ChatBot')
carpool_trainer = ChatterBotCorpusTrainer(carpool_chatbot)
obtain_path = os.path.dirname(os.path.abspath(__file__))
library_path = os.path.join(obtain_path, 'carpool_chatbot_libary')
carpool_trainer.train('carpool_chatbot_libary')

@app.route("/login",methods = ["POST"])
def login():
    req = request.get_json(silent=False, force=True)
    name = req['name']
    password = req['password']
    conn = sqlite3.connect('uberdb.db')
    print('Connected to the database.')
    cursor = conn.cursor()
    res = cursor.execute(
        "SELECT name,destination FROM userprofile WHERE name is ? AND password is ?"
        ,(name,password))
    data = res.fetchall()
    cursor.close()
    conn.close()
    print(data)
    return jsonify(data)

@app.route("/register",methods = ["POST"])
def register():
    req = request.get_json(silent=False, force=True)
    name = req['name']
    password = req['password']
    destination = req['destination']
    conn = sqlite3.connect('uberdb.db')
    print('Connected to the database.')
    cursor = conn.cursor()
    check = cursor.execute(
        "SELECT * FROM userprofile WHERE name is ?"
        ,(name,))
    checkData = check.fetchall()
    if len(checkData) > 0:
        cursor.close()
        conn.close()
        return jsonify(False)
    else:
        cursor.execute(
        "INSERT INTO userprofile (name, destination, password) VALUES (?, ?, ?)"
        ,(name,destination,password))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(True)
    
@app.route("/updateDestination",methods = ["POST"])
def updateDestination():
    req = request.get_json(silent=False, force=True)
    name = req['name']
    destination = req['destination']
    conn = sqlite3.connect('uberdb.db')
    print('Connected to the database.')
    cursor = conn.cursor()
    res = cursor.execute(
        "UPDATE userprofile SET destination = ? WHERE name is ?"
        ,(destination,name))
    data = res.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(data)

def fun(destination,hour,minute):
    return "string"

@app.route("/map",methods = ["POST"])
def map():
    req = request.get_json(silent=False, force=True)
    destination = req['destination']
    hour=req['hour'] 
    minute = req['minute']
    print(destination)
    print(hour)
    print(minute)
    # str = fun(destination,hour,minute)
    cluster_decision_result=cluster_decision(destination,hour,minute)
    print(len(cluster_decision_result))
    encoded_string=None
    if cluster_decision_result[0]=='Function still unfinished':
        filepath = DIJKSTRAS_Shortpath('University town',cluster_decision_result[0])
        with open('sg_route_map_background.png', "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return jsonify(
            [encoded_string.decode('utf-8'),
            "Number of taxi sharing passengers: "+str(cluster_decision_result[2])+
            "\n"+
            "\nTrip direction: "+str(cluster_decision_result[1])+
            "\n"+
            "\nOptimal path length: "+str(filepath[1])+"km"+
            "\n"+
            "\nPassing stations: "+str(filepath[2])+
            "\n"+
            "\nThe route map is still under development"])
    else:
        filepath = DIJKSTRAS_Shortpath('University town',cluster_decision_result[0])
        with open(filepath[0], "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        print(encoded_string)
        return jsonify([encoded_string.decode('utf-8'),
        "Number of taxi sharing passengers: "+str(cluster_decision_result[2])+
        "\n"+
        "\nTrip direction: "+str(cluster_decision_result[1])+
        "\n"+
        "\nOptimal path length: "+str(filepath[1])+"km"+
        "\n"+
        "\nPassing stations: "+str(filepath[2])])

    #return jsonify({"imgUrl":'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/800px-Image_created_with_a_mobile_phone.png'})


@app.route("/chatbot",methods = ["POST"])
def chatbot():
    req = request.get_json(silent=False, force=True)
    name = req['name']
    context = req['context']
    tag1 = req['tag1']
    tag2 = req['tag2']
    tag3 = req['tag3']
    tag4 = req['tag4']
    print(context)
    print(tag1)
    print(tag2)
    print(tag3)
    print(tag4)
    # print(tag3)
    carpool_chatbot = ChatBot('Carpool system ChatBot')
    carpool_trainer = ChatterBotCorpusTrainer(carpool_chatbot)
    obtain_path = os.path.dirname(os.path.abspath(__file__))
    library_path = os.path.join(obtain_path, 'carpool_chatbot_libary')
    carpool_trainer.train('carpool_chatbot_libary/user_data.yml')

    google_maps = GoogleMaps()
    res = ['',NULL,NULL,NULL,NULL]
    my_train_list=[]
    
    if tag1 == False and tag2 == True and tag3 == False and tag4 == False:
        if context.upper() in ['YES','NOT','NO','Y','N']:
            if context.upper() in ['NO','NOT','N']:
                res = ['Ok, Please go to the home page to input your drop-off location and select your pick-up time. Hence, taxi share routing being generated for you.',True,True,False,False]
            else:
                res = ['Please input your drop-off location.',False,False,False,False]
        else:
            res = ['Your input message format is wrong. Please re-input.',False,True,False,False]
    elif tag1 == False and tag2 == False and tag3 == False and tag4 == False:   
        
        result_recommendation_list = google_maps.obtain_address_recommendation(query= context)
        
        # 修改：result_recommendation_list[0]["formatted_address"]变为result_recommendation_list[0]
        
        obj = json.dumps(result_recommendation_list[0]['formatted_address'],indent=1)
        string1 = 'I get you want to go to {}.'.format(obj) + '\n' + '\n' + 'Are you satisfied with this result? (Please input yes or not)'
        res = [string1,True,False,False,False]
    elif tag1 == True and tag2 == False and tag3 == False and tag4 == False:
        if context.upper() in ['YES','NOT','NO','Y','N']:
            if context.upper() in ['YES','Y']:
                res = ['Ok, Please go to the home page to input your drop-off location and select your pick-up time. Hence, taxi share routing being generated for you.',True,True,False,False]
            else:
                res = ['Please re-input your drop-off location.',False,False,False,False]
        else:
            res = ['Your input message format is wrong. Please re-input.',True,False,False,False]
    elif tag1 == True and tag2 == True and tag3 == False and tag4 == False:
        res = ['Do you have any questions? I will try my best to answer.(88 out)',True,True,True,False]
        # carpool_chatbot = ChatBot('Carpool system ChatBot')
        # carpool_trainer = ChatterBotCorpusTrainer(carpool_chatbot)
        # obtain_path = os.path.dirname(os.path.abspath(__file__))
        # library_path = os.path.join(obtain_path, 'carpool_chatbot_libary')
        # carpool_trainer.train('carpool_chatbot_libary')
    elif tag1 == True and tag2 == True and tag3 == True and tag4 == False:
        
        if context == "88":
            res = ['88',True,True,True,True]
        else:
            # res = ['Wait a minute',False,False,True,True]
            # if tag1 == False and tag2 == False and tag3 == True and tag4 == True:
            # my_train_list = []
            if context in my_train_list:
                for i in range(len(my_train_list)):
                    if i/2 == 0:
                        if context == my_train_list[i]:
                            string2 = my_train_list[i+1]
                            res = [string2,True,True,True,False]
            else:
                string3 = str(carpool_chatbot.get_response(context))
                my_train_list.append('- - '+context)
                with open(r'carpool_chatbot_libary/user_data.yml','a') as file:
                    for line in my_train_list:
                        file.write(line+'\n')
                print(type(string3))
                print(str(string3))
                res = [string3 + '\n' + 'Whether the answer is good or not?',False,False,True,True]
    
    elif tag1 == False and tag2 == False and tag3 == True and tag4 == True:
        if context.upper() in ['GOOD','OK','NO PROBLEM','NP']:
            res = ['Great.',True,True,True,False]
        else:
            # my_train_list.append('- - '+context)
            # with open(r'carpool_chatbot_libary/user_data.yml','a') as file:
            #     for line in my_train_list:
            #         file.write(line+'\n')
            #         # file.write(line)
            res = ['Sorry. I did not give you satisfied answer. Could you retype your wanted answer.',False,True,True,False]
    elif tag1 == False and tag2 == True and tag3 == True and tag4 == False:
        # my_train_list.append('- - '+context)
        my_train_list.append('  - '+context)
        with open(r'carpool_chatbot_libary/user_data.yml','a') as file:
            for line in my_train_list:
                file.write(line+'\n')
        res = ['Captain has learned it. You can try again.',True,True,True,False]
                # else:
                #     res = ['The format entered is not correct, please re-type',False,False,True,False]
            # else:
            #     res = ['',False,False,True,True]
    else:
        res = ['',True,True,True,False]
                            
    table_name = name.replace(' ','_')+"_history"
    conn = sqlite3.connect('uberdb.db')
    print('Connected to the database.')
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS '+table_name+' (date TEXT,name TEXT,context TEXT)'
        )
    cursor.execute('INSERT INTO '+table_name+' (date, name, context) VALUES (?, ?, ?)',(datetime.datetime.now(),"user",context))
    cursor.execute('INSERT INTO '+table_name+' (date, name, context) VALUES (?, ?, ?)',(datetime.datetime.now(),"bot",res[0]))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(res)
if __name__ == "__main__":
    app.run(debug=True)


# flask run
# flask run --host=0.0.0.0
