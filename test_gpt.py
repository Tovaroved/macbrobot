import datetime

# Получаем текущую дату
now = datetime.datetime.now().date()

# Получаем номер текущего дня недели (0 - понедельник, 6 - воскресенье)
weekday = now.weekday()

# Вычисляем даты
last_wednesday = now - datetime.timedelta(days=(weekday - 2) % 7 + 7)
if weekday >= 4:  
    last_friday = now - datetime.timedelta(days=weekday - 4 + 7)
# Если сегодня день до пятницы
else:  
    last_friday = now - datetime.timedelta(days=weekday + 3 + 7)
this_wednesday = now + datetime.timedelta(days=(2 - weekday) % 7 if weekday <= 2 else (2 - weekday) % 7 - 7)
this_friday = now + datetime.timedelta(days=(4 - weekday) % 7 if weekday <= 4 else (4 - weekday) % 7 - 7)
next_wednesday = now + datetime.timedelta(days=(2 - weekday) % 7)

# Выводим даты
print("Среда прошлой недели: ", last_wednesday)
print("Пятница прошлой недели: ", last_friday)
print("Среда текущей недели: ", this_wednesday)
print("Пятница текущей недели: ", this_friday)
print("Среда следующей недели: ", next_wednesday)
