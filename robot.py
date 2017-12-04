import telebot

TOKEN = '477128503:AAHp2W9ofm2BDCObfwF-V_hd9ieuDk4UnVc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
	bot.register_next_step_handler(sent, hello)

def hello(message):
	bot.send_message(
		message.chat.id,
		'Привет, {name}. Ты чертов красавчик!'.format(name=message.text))
		
bot.polling()