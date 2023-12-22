from datetime import datetime, timedelta

# Define the start and end times
start_time_str = "12:40"
end_time_str = "22:10"

# Convert string times to datetime objects
start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

# Calculate the duration
duration = end_time - start_time

# Print the result
# print(f"You worked for {duration}")



def check_date_range(input_date):
    # Преобразуем строку с датой в объект datetime
    try:
        date_obj = datetime.strptime(input_date, '%Y-%m-%d')
    except ValueError:
        return "Некорректный формат даты. Используйте yyyy-mm-dd."

    # Получаем день недели (понедельник = 0, воскресенье = 6)
    day_of_week = date_obj.weekday()

    # Проверяем, попадает ли дата в нужный промежуток
    if 0 <= day_of_week <= 3:  # с понедельника до четверга
        return "Дата находится в промежутке с понедельника до четверга."
    elif day_of_week == 4:  # пятница
        return "Дата находится в пятницу."
    elif day_of_week == 5:  # суббота
        return "Дата находится в субботу."
    else:
        return "Дата не попадает в заданные промежутки."

# Пример использования
input_date = input("Введите дату в формате yyyy-mm-dd: ")
result = check_date_range(input_date)
print(result)


