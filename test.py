from datetime import datetime, timedelta


def is_date_this_week(date_str):
    date_to_check = datetime.strptime(date_str, "%Y-%m-%d")

    today = datetime.now()

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    if start_of_week <= date_to_check <= end_of_week:
        return True
    else:
        return False



print(is_date_this_week('2023-10-07'))