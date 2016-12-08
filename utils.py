import traceback
from threading import Thread

def load_chat_users(bot,chat_id,users):

	resp = list()
	for usr_id, (name,usrname) in users.items():
		try:
			bot.getChatMember(chat_id,usr_id)
			resp.append(usr_id)
		except:
			traceback.print_exc()

	return resp






