from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .handling_data import get_formatted_data
import gspread
from datetime import datetime, timedelta



logins1,passwords1,names1 = [
    'sulaimanovuran@gmail.com',
    'macbookfrombro@gmail.com', 
    'brayanbekgriffin@gmail.com',
    'macbrobro2@gmail.com',
    'macbookbrobishkek@gmail.com',
    'macbookbro.baltyan@gmail.com',
    'macbookbro.oshashin@gmail.com',
    'macbookbro.ivanov@gmail.com',
    'polinabuldakova741@gmail.com',
    'macbookbro1@yandex.ru',
    'macbookbro.kiselev@yandex.ru',
    'macbookbro.guseva@yandex.ru',
    'macbookbro.guseva2@yandex.ru',
    'macbookbro.losev@yandex.ru',
    'macbookbro.landishev@yandex.ru',
    'johnycash52@yandex.ru',
    'bossniger.nn@yandex.ru',
    'gruzinka41@yandex.ru'
],[
    'murakami670',
    'macbro1v',
    'murakami670',
    'macbro6f',
    'Murakami670',
    'parol_baltyan',
    'parol_oshashin',
    'parol_ivanov',
    '2323polbul',
    'parol_12',
    'parol_kiselev1',
    'parol_guseva',
    'parol_guseva',
    'parol_losev1',
    'parol_landishev',
    'widqogEL45',
    'bossniger2323',
    'gruzin41'
],[
    "Уран",
    "Влад",
    "Леша",
    "Антон",
    "Дима",
    "Руслан",
    "Ира",
    "Мекен",
    "Марина",
    "Костя",
    "Сергей",
    "Ксения",
    "Александра",
    "Иван",
    "Валентина"
    "Арина",
    "Ольга",
    "Гульнур"
]

# Открытие страницы авторизации


def get_data_about_packages(logins1, passwords1, names1):
    driver = webdriver.Safari()
    login_url = "https://app.lifeshop.kg/auth/login"
    packages = []
    for login, password, name in zip(logins1, passwords1, names1):
        driver.get(login_url)
        
        email_field = driver.find_element(value="user_email")
        password_field = driver.find_element(value="user_password")
        
        email_field.send_keys(login)
        time.sleep(2)
        password_field.send_keys(password)

        # Отправка формы
        submit_button = driver.find_element(by=By.NAME,value="commit")
        submit_button.click()
        time.sleep(6)
        source = driver.page_source

        with open(f'track_package/html_pages/{name}.html', 'w') as f:
            f.write(str(source))

        if login == logins1[-1]:
            driver.close()
        else:
            driver.close()
            time.sleep(3)
            driver.start_session({})
        

    time.sleep(10)

    for name in names1:
        with open(f'track_package/html_pages/{name}.html', 'r+') as f:
            html_code = f.read()
            data = get_formatted_data(html_code, name)
            if data:
                packages+=data
            else:
                continue
    return packages


def get_thursday_friday_dates():
    today = datetime.now()

    current_day = today.weekday()

    thursday = today - timedelta(days=current_day - 3)

    friday = today - timedelta(days=current_day - 4)

    thursday_formatted = thursday.strftime("%d.%m")
    friday_formatted = friday.strftime("%d.%m")

    result = f"{thursday_formatted} - {friday_formatted}"

    return result



def formatted_packages_list():
    all_packages = get_data_about_packages(logins1, passwords1, names1)

    packages_list_current = ''
    packages_list_next = ''
    total_price_current = 0
    total_price_next = 0
    for package_list in all_packages:
        
        if package_list[-2] == 'Current week':
            total_price_current+=float(package_list[3])
            if int(package_list[-1]) > 1:
                packages_list_current+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
            else:
                packages_list_current+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'

        elif package_list[-2] == 'Next week':
            total_price_next+=float(package_list[3])
            if int(package_list[-1]) > 1:
                packages_list_next+=f'{package_list[-1]}шт {package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
            else:
                packages_list_next+=f'{package_list[0]} - {package_list[1]} – ${package_list[3]}\n'
    


    return [packages_list_current, packages_list_next, f'Общая сумма доставки: ${round(total_price_current,2)}', f'Общая сумма доставки: ${round(total_price_next,2)}']



# def gsheet_package():
#     """Авторизация"""
#     sa = gspread.service_account()
#     sh = sa.open("MacPython")
#     wks = sh.worksheet('Получение посылок')
#     data = get_data_about_packages(logins1, passwords1, names1)
#     wks.update('P143:U165', data)
    
#     print("Записано")


# gsheet_package()