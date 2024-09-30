import telebot
from config import token
from orm import Person


bot = telebot.TeleBot(token)
users = {}

@bot.message_handler(commands=['start'])
def welcome(message) -> None:
    chat_id = message.chat.id
    mess = (f'Добро пожаловать в бота! '
            f'Введите ваше имя для передачи в ORM')
    bot.send_message(chat_id, mess)
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_text)

def save_text(message) -> None:
    chat_id = message.chat.id
    user_name = message.text
    users[chat_id] = user_name
    bot.send_message(chat_id,
                     f'Отлично, ваше имя передано в ORM, {user_name}')

    names = Person(name=user_name)
    names.save()
    bot.send_message(chat_id, f'Запись в БД прошла успешно!')
    for i in Person:
        print(i.name)