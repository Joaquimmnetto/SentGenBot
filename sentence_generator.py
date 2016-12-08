import numpy
import os
import pickle
import scipy.io

words = dict()
first_words = dict()
neigh = dict()

#usr_id -> (usrname,name)
users = dict()
#usrname -> (usr_id,name)
usrnames = dict()



def load_models(users_path,model_path):
	with open(users_path,'rb') as usrs_fl:
		users.update(pickle.load(usrs_fl))

	usrnames.update( dict( (usrname.lower(),(usr_id,name)) for usr_id,(name,usrname) in users.items() ) )

	for file in os.listdir(model_path):
		usr_id = file.split('.')[0]
		print("Loading model for ",usr_id)
		with open(model_path+'/'+file, 'rb') as data_fl:
			if "words.pkl" in file:
				words[usr_id] = pickle.load(data_fl)
			elif "fw.pkl" in file:
				first_words[usr_id] = pickle.load(data_fl)
			elif "neigh.spy" in file:
				neigh[usr_id] = scipy.io.mmread(data_fl)



def get_sentence(usrname_usrid):
	if usrname_usrid in usrnames.keys():
		usr_id = str(usrnames[usrname_usrid.lower()][0])
	else:
		usr_id = str(usrname_usrid)

	return generate(first_words[usr_id],words[usr_id],neigh[usr_id])


def generate(first_words,words,neigh):
	sentence_size = numpy.random.choice(range(4,12))
	initial = ""
	while len(initial) < 3:
		initial = numpy.random.choice(list(first_words))

	result = [initial]
	current = initial
	for j in range(1,sentence_size):
		current_index = words.index(current)
		prob_dist = neigh.getrow(current_index).toarray()[0] / numpy.sum(neigh.getrow(current_index).toarray()[0])
		current = numpy.random.choice(words,p=prob_dist)

		result.append(current)

	return ' '.join(result)


def unload_model(usr_id):
	del words[usr_id]
	del first_words[usr_id]
	del neigh[usr_id]


def unload_models():
	words.clear()
	first_words.clear()
	neigh.clear()