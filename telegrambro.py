import telebot
from telebot import types
from sxrt import main
from archive.selenium_test import get_thursday_friday_dates, formatted_packages_list

macbrobot = telebot.TeleBot('6670439167:AAECvyhfuw2g6hoLpYp05lMtOmwgDY6kC84')

@macbrobot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} </b>, привет!\nВыбери действие"
  rep_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  rep_markup.add(types.KeyboardButton('/rates'))
  rep_markup.add(types.KeyboardButton('/pack'))
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=rep_markup)

@macbrobot.message_handler(commands=['rates'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} </b>, привет!\nКурс обновлен"

  main()
  
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')


@macbrobot.message_handler(commands=['pack'])
def startBot(message):
  packages_info = formatted_packages_list()
  first_mess = f"<b>Товары на этой неделе{get_thursday_friday_dates()}</b>\n{packages_info[0]}\n\n<b>{packages_info[-2]}</b>\n\n\n\n<b>Товары на следующей неделе</b>\n{packages_info[1]}\n\n<b>{packages_info[-1]}</b>"
  
  macbrobot.send_message(message.chat.id, first_mess, parse_mode='html')

if __name__ == '__main__':
  macbrobot.infinity_polling()