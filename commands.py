import sentence_generator as sentgen
import random
import utils

current_update = None


def hello(bot, update, args):
	resp = random.choice(['Hiya', 'Hi~', '안녕!'])
	bot.sendMessage(chat_id=update.message.chat_id, text=resp)

def sentence(bot, update, args):
	print("Sentence chamado com args ",args)
	if args is None or len(args) == 0:
		args = update.message.from_user.id

	sent = sentgen.get_sentence(args[0] if isinstance(args,list) else args)

	bot.sendMessage(chat_id=update.message.chat_id,reply_to_message_id=update.message.message_id, text=sent)
	return True


def guess_sentence(bot, update, args):
	print("NewGuess chamado com args ", args)
	usr_id = utils.load_chat_users(bot, update.message.chat_id,sentgen.users)

	global guess_anwser
	guess_anwser = sentgen.users[usr_id]

	sentence(bot, update, usr_id)
	bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="Quem falaria esta frase? Responda com /guess.")

	return True


def respond_guess(bot, update, args):
	print("GuessWho chamado com args ", args)
	usr_response = '_'.join(args).lower()

	if guess_anwser == None:
		bot_response = 'A sentença já foi respondida ou ninguém pediu por uma. Peça uma sentença com /newguess'

	elif usr_response == guess_anwser[0].strip().lower() or usr_response == guess_anwser[1].strip().lower():
		global guess_anwser
		guess_anwser = None
		bot_response = 'Parabéns '+update.message.from_user.first_name+', você acertou!'
	else:
		bot_response = 'Você errou, tente novamente.'

	bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=bot_response)

def get_guess_response(bot, update, args):
	print("GuessResp chamado com args ", args)
	response = 'A reposta é '+guess_anwser+', seu arregão!'
	bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=response)
	global guess_anwser
	guess_anwser = None



