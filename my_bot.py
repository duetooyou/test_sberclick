import telebot
import logging

TOKEN = '1769323348:AAE_NgEV5FS7vTKRBRIDDd5cIBiOU3ge8mA'

bot = telebot.TeleBot(TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(content_types=['text'])
def bot_commands(message):
    bot.send_message(message.chat.id, message)


bot.polling()
