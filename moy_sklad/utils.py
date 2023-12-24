from datetime import datetime, timedelta

def check_30_days_ago(input_date):
    try:
        date_obj = datetime.strptime(input_date, '%Y-%m-%d')

        today = datetime.now()

        difference = today - date_obj

        if difference.days >= 30:
            return False
        else:
            return True

    except ValueError:
        return "Некорректный формат даты. Используйте yyyy-mm-dd."

# Пример использования
input_date = input("Введите дату в формате yyyy-mm-dd: ")
result = check_30_days_ago(input_date)
print(result)
23