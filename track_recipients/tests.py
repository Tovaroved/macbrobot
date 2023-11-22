# from datetime import datetime, timedelta

# def is_date_in_current_week(input_date_str):
#     input_date = datetime.strptime(input_date_str, '%Y-%m-%d')

#     current_date = datetime.now()

#     current_week_start = current_date - timedelta(days=current_date.weekday())

#     current_week_end = current_week_start + timedelta(days=6)

#     return current_week_start.date() <= input_date.date() <= current_week_end.date()

# # Пример использования:
# input_date_str = input("Введите дату в формате YYYY-mm-dd: ")

# try:
#     result = is_date_in_current_week(input_date_str)
#     if result:
#         print("Да, введенная дата находится в текущей неделе.")
#     else:
#         print("Нет, введенная дата не находится в текущей неделе.")
# except ValueError:
#     print("Ошибка: некорректный формат даты.")


from datetime import datetime, timedelta

# def calculate_week_dates():
#     # Получаем текущую дату
#     current_date = datetime.now()

#     before_last_friday = current_date - timedelta(days=current_date.weekday() + 3, weeks=1)
#     before_last_friday = before_last_friday.replace(hour=0, minute=0, second=0, microsecond=0)
#     last_tuesday = current_date - timedelta(days=current_date.weekday() - 1, weeks=1)
#     last_tuesday = last_tuesday.replace(hour=0, minute=0, second=0, microsecond=0)

#     last_wednesday = before_last_friday - timedelta(days=-5)
#     last_thursday = last_wednesday + timedelta(days=1)
#     last_friday = last_thursday + timedelta(days=1)

#     current_wednesday = current_date - timedelta(days=current_date.weekday() - 2)
#     current_tuesday = current_wednesday - timedelta(days=1)
#     current_thursday = current_wednesday + timedelta(days=1)
#     current_friday = current_date - timedelta(days=current_date.weekday() - 4)

#     next_wednesday = current_date + timedelta(days=(2 - current_date.weekday()) + 7)
#     next_tuesday = next_wednesday - timedelta(days=1)
#     next_thursday = next_wednesday + timedelta(days=1)
#     next_friday = current_date + timedelta(days=(4 - current_date.weekday()) + 7)

#     further_next_wednesday = current_date + timedelta(days=(2 - current_date.weekday()) + 14)
#     further_next_tuesday = further_next_wednesday - timedelta(days=1)
#     further_next_thursday = further_next_wednesday + timedelta(days=1)
#     further_next_friday = current_date + timedelta(days=(4 - current_date.weekday()) + 14)

#     in_two_weeks_wednesday = current_date + timedelta(days=(2 - current_date.weekday()) + 21)
#     in_two_weeks_tuesday = in_two_weeks_wednesday - timedelta(days=1)
#     in_two_weeks_thursday = in_two_weeks_wednesday + timedelta(days=1)
#     in_two_weeks_friday = current_date + timedelta(days=(4 - current_date.weekday()) + 21)

#     in_three_weeks_tuesday = current_date + timedelta(days=(2 - current_date.weekday()) + 27)

#     return {
#         'B': [before_last_friday, last_tuesday], 
        
#         'C': [last_wednesday, last_thursday],

#         'D': [last_friday, current_tuesday],

#         'E': [current_wednesday, current_thursday],

#         'F': [current_friday, next_tuesday], 

#         'G': [next_wednesday, next_thursday], 

#         'H': [next_friday, further_next_tuesday], 

#         'I': [further_next_wednesday, further_next_thursday], 

#         'J': [further_next_friday,in_two_weeks_tuesday],

#         'K': [in_two_weeks_wednesday,in_two_weeks_thursday],

#         'L': [in_two_weeks_friday, in_three_weeks_tuesday]
#     }

# Пример использования
# dates = calculate_week_dates()
# c = 0
# # Вывод результатов
# for key, value in dates.items():
#     if c % 2 == 0 and c != 0:
#         print('\n\n')
#     print(f"{key}: {value.strftime('%Y-%m-%d')}")
#     c += 1


import gspread


sa = gspread.service_account()
sh = sa.open("MacPython")
wks = sh.worksheet('Список посылок')

checkboxes = wks.acell('G16:G17').value

print(checkboxes)



['iPad 4th 64Gb Sky Blue', 'Алиса', '1ZAC98180390708651', '300.0', 'В пути', '2023-11-16']
['Air M2 15 8/256 Silver', 'Алиса', '9410808205499399214937', '810.0', 'Ожидаем', ' 2023-11-25']
['iPad Air 5th M1 64Gb Purple', 'Алиса', '1ZE566K10310272481', '400.0', 'В пути', '2023-11-15']
['iPad Air 5th M1 64Gb Rose Gold', 'Алиса', '1ZC754230334733348', '317.0', 'Готова к отправке', '2023-11-18']


['Pro 14 M1 Pro 16/512 SG', 'Валентина', '1Z22114E0334392747', '998.0', 'В пути', '2023-11-17']
['XXX - Air 15 8/256 Space Gray', 'Валентина', '784810449018', '998.0', 'Ожидаем+', '2023-10-10']


['Logitech - MX Keys S Black', 'Влад', '1ZA2R2010314777113', '65.0', 'Прибыла', '2023-11-23']
['TP-Link Deco X60 Wi-Fi +', 'Влад', '9405508205499321957649', '117.0', 'Ожидаем', ' 2023-11-30']
['2шт Magic Trackpad 3 White', 'Влад', '9434608205499379207931', '42.0', 'В пути', '2023-11-19']
['Magic Trackpad 2 White', 'Влад', '9400108205498242290863', '79.0', 'Отправлена', '2023-11-15']


['Mac Mini M2 24/512', 'Уран', '526935074656', '649.0', 'Таможенное оформление', '2023-11-22']
['3шт Logitech iPad Pro 12.9 Sand', 'Уран', '785355088641', '93.0', 'В пути', '2023-11-15']
['2шт Beats Studio Pro Black', 'Уран', '9405508205499391131055', '103.0', 'Готова к отправке', '2023-11-23']
['Air M1 16/256 Silver', 'Уран', '784855877437', '660.0', 'Прибыла', '2023-11-24']
