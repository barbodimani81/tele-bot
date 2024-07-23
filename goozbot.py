import telebot
from telebot import types

bot = telebot.TeleBot('7147798305:AAGr1DtOuJhTP6X3o_LqVwElSXHUntm0y64')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to gooz bot my friend")


@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("درباره ما")
    item2 = types.KeyboardButton("تماس با ما")
    item3 = types.KeyboardButton("<-")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "انتخاب کنبد", reply_markup=markup)


@bot.message_handler(commands=['membership'])
def send_memberships(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("یک ساله")
    item2 = types.KeyboardButton("سه ماهه")
    item3 = types.KeyboardButton("<-")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "انتخاب کنبد", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def other_messages(message):
    if message.text == "درباره ما":
        bot.send_message(message.chat.id, "Developed by Barbod")
    elif message.text == "تماس با ما":
        email = "gooz@gmail.com"
        website = "gooz.com"
        info = f"email: {email}\n website: {website}"
        bot.send_message(message.chat.id, info)
    elif message.text == "سه ماهه":
        bot.send_message(message.chat.id, "3 months of gooz for you <3")
    elif message.text == "یک ساله":
        bot.send_message(message.chat.id, "1 year of gooz for you <3")
    elif message.text == "<-":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "returned to main menu", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "invalid")


if __name__ == '__main__':
    bot.polling()
