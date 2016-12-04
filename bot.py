
import requests
import json
import csv
import time
import pickle
import traceback
import configs
import api
import csv_feeder
from datetime import datetime as dt
#https://api.telegram.org/bot<token>/METHOD_NAME


def feed(up_json,l_id):
    up_id = l_id
    msg_count = 0
    if up_json['ok']:
        for update in up_json['result']:
            up_id = update['update_id']
            msg_count = msg_count + 1 if csv_feeder.feed_corpus(update) else 0
    else:
        print('Falha na requisição')
    return up_id,msg_count        


cfg = configs.load_config()

token='265272545:AAGYjDVv2Ci_Cg4WOeekuuNo6MFybpAzi04'
print("Loaded Configs:",cfg.__dict__)
#Gera updates a cada 10s
update_tick = 10

while(True):
    if (dt.now() - cfg.last_update_tick).total_seconds() > update_tick:
        print("Sending request...")      
        args = {'timeout':10,'offset':cfg.last_up_id+1}

        print("Sending getUpdates", ", args", args)
        resp = api.api_request('getUpdates', args)
        if not resp:
            continue
        
        try:
            print("Feeding the corpus")
            cfg.last_up_id, msg_count = feed(resp, cfg.last_up_id)
            print(msg_count," messages were saved.")
        except:
            traceback.print_exc()
            print("Error while feeding csv, continuing loop")
            continue

        cfg.last_update_tick = dt.now()
        print("Saving status:",cfg.last_up_id,',',cfg.last_update_tick)

        configs.save_config(cfg)
        print("Processing done")
    else:
        print("Resting some seconds...")
        #Verifica a cada 10s
        time.sleep(10)
   
        

        


    

