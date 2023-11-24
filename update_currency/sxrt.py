import gspread
from .sxrap import get_rates



def find_extreme_rates(currency_rates):
    # Инициализируем минимальный курс доллара и максимальный курс рубля
    min_usd_rate = float('inf')  # Положительная бесконечность
    max_rub_rate = float('-inf')  # Отрицательная бесконечность

    # Проходим по элементам словаря
    for bank, rates in currency_rates.items(): 
        usd_rate, rub_rate = rates

        # Проверяем, является ли текущий курс доллара минимальным
        if usd_rate < min_usd_rate:
            min_usd_rate = usd_rate

        # Проверяем, является ли текущий курс рубля максимальным
        if rub_rate > max_rub_rate:
            max_rub_rate = rub_rate

    return [min_usd_rate, max_rub_rate]


def main():
    """Авторизация"""
    sa = gspread.service_account()
    sh = sa.open("Деньги")
    wks = sh.worksheet('Переводы')

    data = find_extreme_rates(get_rates())

    wks.update('F5', data[0])

    wks.update('F2', data[1])