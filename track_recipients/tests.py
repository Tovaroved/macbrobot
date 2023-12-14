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


# from datetime import datetime, timedelta

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


[
['XXX - Logitech MX Master 3S', 'Влад', '9400108205498247839401', '80.0', 'Ожидаем+', '2023-10-20'], 
['XXX - 3шт Logitech Combo Touch iPad Pro 12.9" - Sand', 'Уран', '1ZAC98180335944955', '92.0', 'Ожидаем+', '2023-10-19'],
['XXX - Mini M1 8/256', 'Уран', '92346903332000300007131463', '387.0', 'Ожидаем+', '2023-10-12'],
['XXX - Air 15 8/256 Space Gray', 'Валентина', '784810449018', '998.0', 'Ожидаем+', '2023-10-10'], 

['TP-Link Deco X60 Wi-Fi +', 'Влад', '9405508205499321957649', '117.0', 'Ожидаем', ' 2023-11-30', 'G2'], 
['Air M2 15 8/256 Silver', 'Алиса', '9410808205499399214937', '810.0', 'Ожидаем', ' 2023-11-25', 'F5'], 
['2шт Beats Studio Pro Black', 'Уран', '9405508205499391131055', '103.0', 'Готова к отправке', '2023-11-23', 'E3'], 
['iPad Air 5th M1 64Gb Rose Gold', 'Алиса', '1ZC754230334733348', '317.0', 'Готова к отправке', '2023-11-18', 'D5'], 
['Magic Trackpad 2 White', 'Влад', '9400108205498242290863', '79.0', 'Отправлена', '2023-11-15', 'C2'], 
['2шт Magic Trackpad 3 White', 'Влад', '9434608205499379207931', '42.0', 'В пути', '2023-11-19', 'D2'], 
['3шт Logitech iPad Pro 12.9 Sand', 'Уран', '785355088641', '93.0', 'В пути', '2023-11-15', 'C3'], 
['Pro 14 M1 Pro 16/512 SG', 'Валентина', '1Z22114E0334392747', '998.0', 'В пути', '2023-11-17', 'D4'], 
['iPad 4th 64Gb Sky Blue', 'Алиса', '1ZAC98180390708651', '300.0', 'В пути', '2023-11-16', 'C5'], 
['iPad Air 5th M1 64Gb Purple', 'Алиса', '1ZE566K10310272481', '400.0', 'В пути', '2023-11-15', 'C5'], 
['Mac Mini M2 24/512', 'Уран', '526935074656', '649.0', 'Таможенное оформление', '2023-11-22', 'E3'], 
['Logitech - MX Keys S Black', 'Влад', '1ZA2R2010314777113', '65.0', 'Прибыла', '2023-11-23', 'E2'], 
['Air M1 16/256 Silver', 'Уран', '784855877437', '660.0', 'Прибыла', '2023-11-24', 'F3']
 ]



"""Read from sheets"""

[
['Logitech MX Master 3S', 'Влад', '9400108205498247839401', '80.0', 'Ожидаем+', '2023-10-20', 'FALSE'],
['3шт Logitech Combo Touch iPad Pro 12.9" - Sand', 'Уран', '1ZAC98180335944955', '92.0', 'Ожидаем+', '2023-10-19', 'FALSE'], 
['Mini M1 8/256', 'Уран', '92346903332000300007131463', '387.0', 'Ожидаем+', '2023-10-12', 'FALSE'], 
['Air 15 8/256 Space Gray', 'Валентина', '784810449018', '998.0', 'Ожидаем+', '2023-10-10', 'FALSE'], 
['TP-Link Deco X60 Wi-Fi +', 'Влад', '9405508205499321957649', '117.0', 'Ожидаем', '2023-11-30', 'FALSE'], 
['Air M2 15 8/256 Silver', 'Алиса', '9410808205499399214937', '810.0', 'Ожидаем', '2023-11-25', 'FALSE'], 
['2шт Beats Studio Pro Black', 'Уран', '9405508205499391131055', '103.0', 'Готова к отправке', '2023-11-23', 'TRUE'], 
['iPad Air 5th M1 64Gb Rose Gold', 'Алиса', '1ZC754230334733348', '317.0', 'Готова к отправке', '2023-11-18', 'TRUE'], 
['Magic Trackpad 2 White', 'Влад', '9400108205498242290863', '79.0', 'Отправлена', '2023-11-15', 'FALSE'], 
['2шт Magic Trackpad 3 White', 'Влад', '9434608205499379207931', '42.0', 'В пути', '2023-11-19', 'FALSE'], 
['3шт Logitech iPad Pro 12.9 Sand', 'Уран', '785355088641', '93.0', 'В пути', '2023-11-15', 'FALSE'], 
['Pro 14 M1 Pro 16/512 SG', 'Валентина', '1Z22114E0334392747', '998.0', 'В пути', '2023-11-17', 'FALSE'], 
['iPad 4th 64Gb Sky Blue', 'Алиса', '1ZAC98180390708651', '300.0', 'В пути', '2023-11-16', 'FALSE'], 
['iPad Air 5th M1 64Gb Purple', 'Алиса', '1ZE566K10310272481', '400.0', 'В пути', '2023-11-15', 'FALSE'], 
['Mac Mini M2 24/512', 'Уран', '526935074656', '649.0', 'Таможенное оформление', '2023-11-22', 'FALSE'], 
['Logitech - MX Keys S Black', 'Влад', '1ZA2R2010314777113', '65.0', 'Прибыла', '2023-11-23', 'FALSE'], 
['Air M1 16/256 Silver', 'Уран', '784855877437', '660.0', 'Прибыла', '2023-11-24', 'FALSE']
    
]






d = {
'G2': ['TP-Link Deco X60 Wi-Fi +\n'], 
'F5': ['Air M2 15 8/256 Silver\n'], 
'E3': ['2шт Beats Studio Pro Black\n', 'Mac Mini M2 24/512\n'], 
'D5': ['iPad Air 5th M1 64Gb Rose Gold\n'], 
'C2': ['Magic Trackpad 2 White\n'], 
'D2': ['2шт Magic Trackpad 3 White\n'], 
'C3': ['3шт Logitech iPad Pro 12.9 Sand\n'], 
'D4': ['Pro 14 M1 Pro 16/512 SG\n'], 
'C5': ['iPad 4th 64Gb Sky Blue\n', 'iPad Air 5th M1 64Gb Purple\n'], 
'E2': ['Logitech - MX Keys S Black\n'], 
'F3': ['Air M1 16/256 Silver\n']
}
# h = d['I45']

# print(h)



{'9400108205498247839401': ['Logitech MX Master 3S', 'Влад', '80.0', 'Ожидаем+', '2023-10-20', 'FALSE'], 
 '1ZAC98180335944955': ['3шт Logitech Combo Touch iPad Pro 12.9" - Sand', 'Уран', '92.0', 'Ожидаем+', '2023-10-19', 'FALSE'], 
 '92346903332000300007131463': ['Mini M1 8/256', 'Уран', '387.0', 'Ожидаем+', '2023-10-12', 'FALSE'], 
 '784810449018': ['Air 15 8/256 Space Gray', 'Валентина', '998.0', 'Ожидаем+', '2023-10-10', 'FALSE'], 
 '9405508205499321957649': ['TP-Link Deco X60 Wi-Fi +', 'Влад', '117.0', 'Ожидаем', '2023-11-30', 'FALSE'], 
 '9410808205499399214937': ['Air M2 15 8/256 Silver', 'Алиса', '810.0', 'Ожидаем', '2023-11-25', 'FALSE'], 
 '9405508205499391131055': ['2шт Beats Studio Pro Black', 'Уран', '103.0', 'Готова к отправке', '2023-11-23', 'TRUE'], 
 '1ZC754230334733348': ['iPad Air 5th M1 64Gb Rose Gold', 'Алиса', '317.0', 'Готова к отправке', '2023-11-18', 'TRUE'], 
 '9400108205498242290863': ['Magic Trackpad 2 White', 'Влад', '79.0', 'Отправлена', '2023-11-15', 'FALSE'], 
 '9434608205499379207931': ['2шт Magic Trackpad 3 White', 'Влад', '42.0', 'В пути', '2023-11-19', 'FALSE'], 
 '785355088641': ['3шт Logitech iPad Pro 12.9 Sand', 'Уран', '93.0', 'В пути', '2023-11-15', 'FALSE'], 
 '1Z22114E0334392747': ['Pro 14 M1 Pro 16/512 SG', 'Валентина', '998.0', 'В пути', '2023-11-17', 'FALSE'], 
 '1ZAC98180390708651': ['iPad 4th 64Gb Sky Blue', 'Алиса', '300.0', 'В пути', '2023-11-16', 'FALSE'], 
 '1ZE566K10310272481': ['iPad Air 5th M1 64Gb Purple', 'Алиса', '400.0', 'В пути', '2023-11-15', 'FALSE'], 
 '526935074656': ['Mac Mini M2 24/512', 'Уран', '649.0', 'Таможенное оформление', '2023-11-22', 'FALSE'], 
 
 '1ZA2R2010314777113': ['Logitech - MX Keys S Black', 'Влад', '65.0', 'Прибыла', '2023-11-23', 'FALSE'], 
 '784855877437': ['Air M1 16/256 Silver', 'Уран', '660.0', 'Прибыла', '2023-11-24', 'FALSE']}

{'9405508205499321957649': ['TP-Link Deco X60 Wi-Fi +', 'Влад', '117.0', 'Ожидаем', ' 2023-11-30'], 
 '9434608205499379207931': ['2шт Magic Trackpad 3 White', 'Влад', '42.0', 'В пути', '2023-11-19'], 
 '9400108205498242290863': ['Magic Trackpad 2 White', 'Влад', '79.0', 'Отправлена', '2023-11-15'], 
 '9400108205498247839401': ['Logitech MX Master 3S', 'Влад', '80.0', 'Ожидаем+', '2023-10-20'], 
 '526935074656': ['Mac Mini M2 24/512', 'Уран', '649.0', 'Таможенное оформление', '2023-11-22'], 
 '785355088641': ['3шт Logitech iPad Pro 12.9 Sand', 'Уран', '93.0', 'В пути', '2023-11-15'], 
 '9405508205499391131055': ['2шт Beats Studio Pro Black', 'Уран', '103.0', 'Готова к отправке', '2023-11-23'], 
 '1ZAC98180335944955': ['3шт Logitech Combo Touch iPad Pro 12.9" - Sand', 'Уран', '92.0', 'Ожидаем+', '2023-10-19'], 
 '92346903332000300007131463': ['Mini M1 8/256', 'Уран', '387.0', 'Ожидаем+', '2023-10-12'], 
 '1Z22114E0334392747': ['Pro 14 M1 Pro 16/512 SG', 'Валентина', '998.0', 'В пути', '2023-11-17'], 
 '784810449018': ['Air 15 8/256 Space Gray', 'Валентина', '998.0', 'Ожидаем+', '2023-10-10'], 
 '1ZAC98180390708651': ['iPad 4th 64Gb Sky Blue', 'Алиса', '300.0', 'В пути', '2023-11-16'], 
 '9410808205499399214937': ['Air M2 15 8/256 Silver', 'Алиса', '810.0', 'Ожидаем', ' 2023-11-25'], 
 '1ZE566K10310272481': ['iPad Air 5th M1 64Gb Purple', 'Алиса', '400.0', 'В пути', '2023-11-15'], 
 '1ZC754230334733348': ['iPad Air 5th M1 64Gb Rose Gold', 'Алиса', '317.0', 'Готова к отправке', '2023-11-18']}



"""
2шт Magic Trackpad 3 White	Влад	9434608205499379207931	42.0	В пути	2023-11-19	ЛОЖЬ
3шт Logitech iPad Pro 12.9 Sand	Уран	785355088641	93.0	В пути	2023-11-15	ЛОЖЬ
Pro 14 M1 Pro 16/512 SG	Валентина	1Z22114E0334392747	998.0	В пути	2023-11-17	ЛОЖЬ
iPad 4th 64Gb Sky Blue	Алиса	1ZAC98180390708651	300.0	В пути	2023-11-16	ЛОЖЬ
iPad Air 5th M1 64Gb Purple	Алиса	1ZE566K10310272481	400.0	В пути	2023-11-15	ЛОЖЬ
Mac Mini M2 24/512	Уран	526935074656	649.0	Таможенное оформление	2023-11-22	ЛОЖЬ
Logitech MX Master 3S	Влад	9400108205498247839401	80.0	Ожидаем+	2023-10-20	ЛОЖЬ
3шт Logitech Combo Touch iPad Pro 12.9" - Sand	Уран	1ZAC98180335944955	92.0	Ожидаем+	2023-10-19	ЛОЖЬ
Mini M1 8/256	Уран	92346903332000300007131463	387.0	Ожидаем+	2023-10-12	ЛОЖЬ
Air 15 8/256 Space Gray	Валентина	784810449018	998.0	Ожидаем+	2023-10-10	ЛОЖЬ

"""

[
    ['Air M2 15 8/256 Silver', 'Алиса', '9410808205499399214937', '810.0', 'Ожидаем', '2023-11-25', 'FALSE'], 
    [['TP-Link Deco X60 Wi-Fi +', 'Влад', '9405508205499321957649', '117.0', 'Готова к отправке', '2023-11-29'], 'TRUE'], 
    ['2шт Beats Studio Pro Black', 'Уран', '9405508205499391131055', '103.0', 'Готова к отправке', '2023-11-23', 'TRUE'], 
    ['iPad Air 5th M1 64Gb Rose Gold', 'Алиса', '1ZC754230334733348', '317.0', 'Готова к отправке', '2023-11-18', 'TRUE'], 
    ['Magic Trackpad 2 White', 'Влад', '9400108205498242290863', '79.0', 'Отправлена', '2023-11-15', 'FALSE'], 
    ['2шт Magic Trackpad 3 White', 'Влад', '9434608205499379207931', '42.0', 'В пути', '2023-11-19', 'FALSE'], 
    ['3шт Logitech iPad Pro 12.9 Sand', 'Уран', '785355088641', '93.0', 'В пути', '2023-11-15', 'FALSE'], 
    ['Pro 14 M1 Pro 16/512 SG', 'Валентина', '1Z22114E0334392747', '998.0', 'В пути', '2023-11-17', 'FALSE'], 
    ['iPad 4th 64Gb Sky Blue', 'Алиса', '1ZAC98180390708651', '300.0', 'В пути', '2023-11-16', 'FALSE'], 
    ['iPad Air 5th M1 64Gb Purple', 'Алиса', '1ZE566K10310272481', '400.0', 'В пути', '2023-11-15', 'FALSE'], 
    ['Mac Mini M2 24/512', 'Уран', '526935074656', '649.0', 'Таможенное оформление', '2023-11-22', 'FALSE'], 
    ['Logitech MX Master 3S', 'Влад', '9400108205498247839401', '80.0', 'Ожидаем+', '2023-10-20', 'FALSE'], 
    ['3шт Logitech Combo Touch iPad Pro 12.9" - Sand', 'Уран', '1ZAC98180335944955', '92.0', 'Ожидаем+', '2023-10-19', 'FALSE'], 
    ['Mini M1 8/256', 'Уран', '92346903332000300007131463', '387.0', 'Ожидаем+', '2023-10-12', 'FALSE'], 
    ['Air 15 8/256 Space Gray', 'Валентина', '784810449018', '998.0', 'Ожидаем+', '2023-10-10', 'FALSE']
]


from datetime import datetime, timedelta

def find_previous_tuesday_thursday(input_date, flag=None):
    date_format = "%Y-%m-%d"
    input_date = datetime.strptime(input_date, date_format)

    # Найдем предыдущий вторник и четверг
    previous_tuesday = input_date - timedelta(days=(input_date.weekday() - 1) % 7)
    previous_thursday = input_date - timedelta(days=(input_date.weekday() - 3) % 7)

    # Выберем тот, который ближе к введенной дате
    output_date = max(previous_tuesday, previous_thursday).strftime(date_format)

    if flag:
        d = datetime.strptime(output_date, date_format)
        new_date = d - timedelta(days=7)
        return new_date.strftime(date_format)
    else:
        return output_date

# Пример использования
print(find_previous_tuesday_thursday("2023-12-17"))

