import csv

usr_corpora = dict()


corpus_rd = csv.reader(open('telegram_corpus.csv','r'))


for line in corpus_rd:
    user = line[0]
    message = ' '.join(line[1:])

    if user not in usr_corpora.keys():
        usr_corpora[user] = open('corpora/'+user+'.corpus','r')
        
    usr_corpora[user].write(messsage.replace('\n','')+'\n')
    

    
        
    
