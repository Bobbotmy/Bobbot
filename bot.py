python
import telebot

TOKEN = 6282194881:AAH7-SAEWqpfOY8FgkvT9YQbxvN6mU2_wok

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет, я ChatGPT бот! Я могу отвечать на ваши вопросы и помочь вам в различных темах. Что бы вы хотели узнать?')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'Извините, я не понимаю вашего запроса. Пожалуйста, задайте другой вопрос.')

bot.polling()
