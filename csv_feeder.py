import csv

corpus = open("telegram_corpus.csv",'a')
crp_wr = csv.writer(corpus)


def feed_corpus(bot, update):

	usr_id = update.message.from_user.id
	fname = update.message.from_user.first_name
	chat_id = update.message.chat_id
	usrname = update.message.from_user.username
	text = update.message.text

	crp_wr.writerow([usr_id, chat_id, fname, usrname, text])
