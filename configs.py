import pickle
from datetime import datetime as dt


def save_config(cfg):
	with open('config.pkl', 'wb') as cfg_fl:
		pickle.dump(cfg, cfg_fl, pickle.HIGHEST_PROTOCOL)

def load_config():
	cfg = load_config_defaults()
	try:
		cfg = load_file_config()
	except:
		print("Loading config defaults...")

	return cfg


def load_file_config():
	with open('config.pkl', 'rb') as cfg_fl:
		return pickle.load(cfg_fl)


def load_config_defaults():
    cfg = lambda:None
    cfg.last_id = 0
    cfg.last_update_tick = dt.min

    return cfg


