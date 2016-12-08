import csv_feeder
import commands
import sentence_generator as sentgen

from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
import logging

token='265272545:AAGYjDVv2Ci_Cg4WOeekuuNo6MFybpAzi04'

print("Load sentence generation models...")
sentgen.load_models('users.pkl','sent_models/')

print("Starting python-telegram-api server...")
updater = Updater(token=token)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

dispatcher.add_handler(CommandHandler('hellow',commands.hello, pass_args=True))
dispatcher.add_handler(CommandHandler('sentence',commands.sentence, pass_args=True))
#dispatcher.add_handler(CommandHandler('newguess',commands.guess_sentence, pass_args=True))
#dispatcher.add_handler(CommandHandler('guesswho',commands.respond_guess, pass_args=True))
#dispatcher.add_handler(CommandHandler('guessresp',commands.get_guess_response, pass_args=True))
dispatcher.add_handler(MessageHandler(Filters.text,csv_feeder.feed_corpus))
#TODO: collective mind

updater.start_polling()


        


    

