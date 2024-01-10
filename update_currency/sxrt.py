import gspread
from .sxrap import get_rates



def find_extreme_rates(currency_rates):
    min_usd_rate = float('inf')
    max_rub_rate = float('-inf')

    for bank, rates in currency_rates.items(): 
        usd_rate, rub_rate = rates

        if usd_rate < min_usd_rate:
            min_usd_rate = usd_rate

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