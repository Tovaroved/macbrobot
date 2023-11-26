from bs4 import BeautifulSoup
from utils import get_sort_key, is_date_in_current_week, calculate_week_dates
import gspread
from datetime import datetime

def get_formatted_recipients_data(account_html_code, name: str):
    soup = BeautifulSoup(account_html_code, 'lxml')
    packages = []
    try:
        packages_block = soup.find('div', class_='mt-8 border border-gray-200 rounded-md divide-y')
        all_packages = packages_block.find_all('div', class_='relative px-5 py-3 space-y-1')
    except Exception as e:
        return None
    if len(all_packages) >= 1:
        for package in all_packages:
            try:
                package_text = package.find('div', class_='text-sm text-gray-700').text.strip().replace('\n', '').split('⨯')

                package_track = package.find('div', class_='font-semibold text-gray-900 w-56 md:w-auto truncate').text.strip()

                package_status = package.find('div', class_='flex items-center gap-x-1').text.strip()

                package_date = package.find('div', class_='text-xs text-gray-500').text.strip().replace('\n', '')[-10:].strip()

                package_amount = package_text[-1].strip()

                package_desc = package_text[0].strip() if int(package_amount) == 1 else f'{package_amount}шт {package_text[0].strip()}'

                package_price = package_text[1].strip()

                if "Ожид" in package_status:
                    # print(package_desc.split('|')[-1].strip())
                    if len(package_desc.split('|')[-1].strip()) == 10:
                        package_date = package_desc.split('|')[-1]
                        
                    else:
                        package_status = 'Ожидаем+'
                
                if "Прибыла" in package_status and not is_date_in_current_week(package_date):
                    continue
                
                package_desc = package_desc.split('|')[0].strip()

            except AttributeError:
                continue
            
            packages.append([package_desc, name, package_track, package_price, package_status, package_date])
        
    else:
        return None

    return packages

names = {
    "Влад": '2',
    "Уран": '3',
    "Валентина": '4',
    "Алиса": '5',
}


def data_for_rs():
    packages=[]
    for name in names:
        with open(f'track_recipients/test_html_pages/{name}.html', 'r+') as f:
            html_code = f.read()
            data = get_formatted_recipients_data(html_code, name)
            if data:
                packages+=data
            else:
                continue
    packages = sorted(packages, key=get_sort_key)



    return packages


def table_architecht():
    dates = calculate_week_dates()

    """Авторизация"""
    sa = gspread.service_account()

    """Подключаемся к документу"""
    sh = sa.open("MacPython")

    """Подключаемся к странице и очищаем её"""
    wks = sh.worksheet('Лист15')

    for k, v in dates.items():
        wks.update(f'{k}1', f"{v[0].strftime('%d.%m')}-{v[1].strftime('%d.%m')}")

    for k, v in names.items():
        wks.update(f"A{v}", k)



def write_to_table():

    packages = data_for_rs() # Заменить
    dates = calculate_week_dates()
    done_packs = {}
    problem_packs = []
    remaining_packages = []  # Новый список для хранения оставшихся пакетов

    for package in packages:
        package_added = False  # Флаг, чтобы удостовериться, что пакет добавлен только один раз

        for coll_word, date_list in dates.items():
            if '+' in package[-2]:
                problem_packs.append(package)
                package_added = True
                break  # Добавил break, чтобы выйти из внутреннего цикла, если условие выполнилось
                
            elif date_list[0].date() <= datetime.strptime(package[-1].strip(), '%Y-%m-%d').date() <= date_list[1].date():
                row_number = names[package[1]]
                key = coll_word + row_number
                done_packs.setdefault(key, []).append(package[0] + '\n')
                package_added = True
                break  # Также добавил break здесь
                
        if not package_added:
            remaining_packages.append(package)

    """Авторизация"""
    sa = gspread.service_account()

    """Подключаемся к документу"""
    sh = sa.open("MacPython")

    """Подключаемся к странице и очищаем её"""
    wks = sh.worksheet('Лист15')

    for coord, value in done_packs.items():
        wks.update(coord, ''.join(value))

    wks.update(f'A21:G{21+len(packages)}', packages, value_input_option='USER_ENTERED')