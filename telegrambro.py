import telebot
from telebot import types
from update_currency.sxrt import main
from track_package.formatting import formatted_packages_list, gsheet_package
from decouple import config

BOT_TOKEN=config('BOT_TOKEN')

macbrobot = telebot.TeleBot(BOT_TOKEN)

@macbrobot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} </b>, привет!\nВыбери действие"
  rep_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup.add(types.KeyboardButton('/rates'))
  rep_markup.add(types.KeyboardButton('/pack'))
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=rep_markup)

@macbrobot.message_handler(commands=['rates'])
def ratesBot(message):
  first_mess = f"<b>{message.from_user.first_name} </b>, привет!\nКурс обновлен"

  main()
  
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')


@macbrobot.message_handler(commands=['pack'])
def packBot(message):
  first_mess = "Какая неделя интересует?"
  rep_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup2.add(types.KeyboardButton('/current'))
  rep_markup2.add(types.KeyboardButton('/next'))
  rep_markup2.add(types.KeyboardButton('/sheets'))
  rep_markup2.add(types.KeyboardButton('/start'))
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html',reply_markup=rep_markup2)

@macbrobot.message_handler(commands=['current'])
def currentBot(message):
  first_mess = "Формат?"
  rep_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup2.add(types.KeyboardButton('/twoparts'))
  rep_markup2.add(types.KeyboardButton('/onepart'))
  rep_markup2.add(types.KeyboardButton('/pack'))

  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html',reply_markup=rep_markup2)

@macbrobot.message_handler(commands=['onepart'])
def currentOneBot(message):
  info = formatted_packages_list()
  first_mess = info[2]
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')

@macbrobot.message_handler(commands=['twoparts'])
def currentTwoBot(message):
  info = formatted_packages_list()
  first_mess = info[0]
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')


@macbrobot.message_handler(commands=['next'])
def nextBot(message):
  first_mess = "Формат?"
  rep_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup2.add(types.KeyboardButton('/twoparts2'))
  rep_markup2.add(types.KeyboardButton('/onepart2'))
  rep_markup2.add(types.KeyboardButton('/pack'))

  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html',reply_markup=rep_markup2)

@macbrobot.message_handler(commands=['onepart2'])
def currentOne2Bot(message):
  info = formatted_packages_list()
  first_mess = info[-1]
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')

@macbrobot.message_handler(commands=['twoparts2'])
def currentTwo2Bot(message):
  info = formatted_packages_list()
  first_mess = info[1]
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')


@macbrobot.message_handler(commands=['sheets'])
def currentBot(message):
  first_mess = "Разделить по партиям?"
  rep_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup2.add(types.KeyboardButton('/yes'))
  rep_markup2.add(types.KeyboardButton('/no'))
  rep_markup2.add(types.KeyboardButton('/pack'))
  rep_markup2.add(types.KeyboardButton('/start'))

  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html',reply_markup=rep_markup2)

@macbrobot.message_handler(commands=['yes'])
def currentBot(message):
  first_mess = "Записано"
  rep_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup2.add(types.KeyboardButton('/pack'))
  rep_markup2.add(types.KeyboardButton('/start'))
  gsheet_package(True)
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html',reply_markup=rep_markup2)


@macbrobot.message_handler(commands=['no'])
def currentBot(message):
  first_mess = "Записано"
  rep_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup2.add(types.KeyboardButton('/pack'))
  rep_markup2.add(types.KeyboardButton('/start'))
  gsheet_package()
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html',reply_markup=rep_markup2)

if __name__ == '__main__':
  macbrobot.infinity_polling()