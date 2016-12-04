import requests
import json
import csv
import time
import pickle
import traceback
import api
from datetime import datetime as dt
#https://api.telegram.org/bot<token>/METHOD_NAME


def save_config(last_id,last_update):
    config['last_id'] = last_id
    config['last_update'] = last_update
    
    with open('config.pkl','wb') as cfg_fl:
        pickle.dump(config,cfg_fl, pickle.HIGHEST_PROTOCOL)
    
def load_config():
    with open('config.pkl','rb') as cfg_fl:
        return pickle.load(cfg_fl)

    
def api_request(method, args):

    print("Sending ",method,", args",args)    
    r = requests.post('https://api.telegram.org/bot{0}/{1}'.format(token,method), json = args)

    if r.status_code!=200:
        print("Request failed with a ",r.status_code)
        return False

    resp = json.loads(r.text)
    
    return resp



def feed(up_json,l_id):
    up_id = l_id
    msg_count = 0
    if up_json['ok']:
        for update in up_json['result']:
            up_id = update['update_id']
            msg_count = msg_count + 1 if feed_corpus(update) else 0            
    else:
        print('Falha na requisição')
    return up_id,msg_count        
       

def feed_corpus(update):
    
    if 'message' not in update.keys():
        return False

    msg = update['message']

    if 'from' not in msg.keys() or 'text' not in msg.keys():
        return False
    
    usr = msg['from']['first_name']
    text = msg['text'].replace('\n',' ')
    
    crp_wr.writerow([usr,text])
         
    return True
   
token='265272545:AAGYjDVv2Ci_Cg4WOeekuuNo6MFybpAzi04'
corpus = open("telegram_corpus.csv",'a')
crp_wr = csv.writer(corpus)

def load_config_defaults():
    c = dict()
    c['last_id'] = 0
    c['last_update_tick'] = dt.min

    return c

try:
    config = load_config()
except:
    print("Loading config defaults...")    
    config = load_config_defaults()
   

print("Loaded Configs:",config)

last_up_id = config['last_id']
last_update_tick = config['last_update_tick']
#Gera updates a cada 10s
update_tick = 10

while(True):
    if (dt.now() - last_update_tick).total_seconds() > update_tick:
        print("Sending request...")      
        args = {'timeout':10,'offset':last_up_id+1}

        print("Sending getUpdates", ", args", args)
        resp = api_request('getUpdates', args)
        if not resp:
            continue
        
        try:
            print("Feeding the corpus")
            last_up_id,msg_count = feed(resp, last_up_id)
            print(msg_count," messages were saved.")
        except:
            traceback.print_exc()
            print("Error while feeding csv, continuing loop")
            continue

        last_update_tick = dt.now()        
        print("Saving status:",last_up_id,',',last_update_tick)
        save_config( last_up_id, last_update_tick )
        print("Processing done")
    else:
        print("Resting some seconds...")
        #Verifica a cada 10s
        time.sleep(10)
   
        

        


    

