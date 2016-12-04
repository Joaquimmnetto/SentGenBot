import csv

corpus = open("telegram_corpus.csv",'a')
crp_wr = csv.writer(corpus)


def feed_corpus(update):
	if 'message' not in update.keys():
		return False

	msg = update['message']

	if 'from' not in msg.keys() or 'text' not in msg.keys():
		return False

	usr = msg['from']['first_name']
	text = msg['text'].replace('\n', ' ')

	crp_wr.writerow([usr, text])

	return True