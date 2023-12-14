from datetime import datetime, timedelta


def is_date_in_current_week(input_date_str):
    # print([input_date_str])
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')

    current_date = datetime.now()

    current_week_start = current_date - timedelta(days=current_date.weekday())

    current_week_end = current_week_start + timedelta(days=6)

    return current_week_start.date() <= input_date.date() <= current_week_end.date()


def get_sort_key(item):
    custom_order = { "Ожидаем": 1, "Готова к отправке": 2, "Отправлена": 3, "В пути": 4, "Таможенное оформление": 5, "Прибыла": 6, "Ожидаем+":7}
    return custom_order.get(item[-2], float('inf'))


def get_sort_key2(item):
    custom_order = { "Ожидаем": 1, "Готова к отправке": 2, "Отправлена": 3, "В пути": 4, "Таможенное оформление": 5, "Прибыла": 6, "Ожидаем+":7}
    return custom_order.get(item[-3], float('inf'))

def calculate_week_dates():
    current_date = datetime.now()

    before_last_friday = current_date - timedelta(days=current_date.weekday() + 3, weeks=1)
    before_last_friday = before_last_friday.replace(hour=0, minute=0, second=0, microsecond=0)
    last_tuesday = current_date - timedelta(days=current_date.weekday() - 1, weeks=1)
    last_tuesday = last_tuesday.replace(hour=0, minute=0, second=0, microsecond=0)

    last_wednesday = before_last_friday - timedelta(days=-5)
    last_thursday = last_wednesday + timedelta(days=1)
    last_friday = last_thursday + timedelta(days=1)

    current_wednesday = current_date - timedelta(days=current_date.weekday() - 2)
    current_tuesday = current_wednesday - timedelta(days=1)
    current_thursday = current_wednesday + timedelta(days=1)
    current_friday = current_date - timedelta(days=current_date.weekday() - 4)

    next_wednesday = current_date + timedelta(days=(2 - current_date.weekday()) + 7)
    next_tuesday = next_wednesday - timedelta(days=1)
    next_thursday = next_wednesday + timedelta(days=1)
    next_friday = current_date + timedelta(days=(4 - current_date.weekday()) + 7)

    further_next_wednesday = current_date + timedelta(days=(2 - current_date.weekday()) + 14)
    further_next_tuesday = further_next_wednesday - timedelta(days=1)
    further_next_thursday = further_next_wednesday + timedelta(days=1)
    further_next_friday = current_date + timedelta(days=(4 - current_date.weekday()) + 14)

    in_two_weeks_wednesday = current_date + timedelta(days=(2 - current_date.weekday()) + 21)
    in_two_weeks_tuesday = in_two_weeks_wednesday - timedelta(days=1)
    in_two_weeks_thursday = in_two_weeks_wednesday + timedelta(days=1)
    in_two_weeks_friday = current_date + timedelta(days=(4 - current_date.weekday()) + 21)

    in_three_weeks_tuesday = current_date + timedelta(days=(2 - current_date.weekday()) + 27)

    return {
        'B': [before_last_friday, last_tuesday], 
        
        'C': [last_wednesday, last_thursday],

        'D': [last_friday, current_tuesday],

        'E': [current_wednesday, current_thursday],

        'F': [current_friday, next_tuesday], 

        'G': [next_wednesday, next_thursday], 

        'H': [next_friday, further_next_tuesday], 

        'I': [further_next_wednesday, further_next_thursday], 

        'J': [further_next_friday,in_two_weeks_tuesday],

        'K': [in_two_weeks_wednesday,in_two_weeks_thursday],

        'L': [in_two_weeks_friday, in_three_weeks_tuesday]
    }




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
    
print(find_previous_tuesday_thursday("2023-12-13", 1))