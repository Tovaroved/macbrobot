from datetime import datetime, timedelta


def get_package_interval(date):

    form_date = datetime.strptime(date, '%Y-%m-%d').date()
    # Get the current date
    current_date = datetime.now()

    # Calculate the dates of the past week's Wednesday and Friday
    last_week_start = current_date - timedelta(days=current_date.weekday() + 7)
    last_week_wednesday = last_week_start + timedelta(days=2)
    last_week_friday = last_week_start + timedelta(days=4)

    # Calculate the dates of the current week's Wednesday and Friday
    current_week_start = current_date - timedelta(days=current_date.weekday())
    current_week_wednesday = current_week_start + timedelta(days=2)
    current_week_friday = current_week_start + timedelta(days=4)

    # Calculate the dates of the next week's Wednesday
    next_week_start = current_date + timedelta(days=(6 - current_date.weekday()) + 7)
    next_week_wednesday = next_week_start + timedelta(days=2)

    if last_week_wednesday.date() <= form_date < last_week_friday.date():
        return 'lw: wed-fri'

    elif last_week_friday.date() <= form_date < current_week_wednesday.date():
        return 'lw: fri-wed'

    elif current_week_wednesday.date() <= form_date < current_week_friday.date():
        return 'cw: wed-fri'

    elif current_week_friday.date() <= form_date:
        return 'cw: fri-wed'



def is_date_in_current_week(input_date_str):
    # Convert input string to datetime object
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')

    # Get the current date
    current_date = datetime.now()

    # Calculate the start of the current week (considering Monday as the start of the week)
    current_week_start = current_date - timedelta(days=current_date.weekday())

    # Calculate the end of the current week
    current_week_end = current_week_start + timedelta(days=6)

    # Check if the input date is within the current wee
    return current_week_start.date() <= input_date.date() <= current_week_end.date()

def check_date_range(input_date):
    # Преобразуем строку с датой в объект datetime
    try:
        date_obj = datetime.strptime(input_date, '%Y-%m-%d')
    except ValueError:
        return "Некорректный формат даты. Используйте yyyy-mm-dd."

    # Получаем день недели (понедельник = 0, воскресенье = 6)
    day_of_week = date_obj.weekday()

    if 0 <= day_of_week <= 3:  # с понедельника до четверга
        return "cw: wed-fri"
    elif day_of_week in (4, 5, 6):  # пятница
        return "cw: fri-wed"
    else:
        raise Exception
    