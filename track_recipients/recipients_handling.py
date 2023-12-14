from bs4 import BeautifulSoup
from .utils import get_sort_key, is_date_in_current_week, calculate_week_dates, find_previous_tuesday_thursday, get_sort_key2
from track_package.requests_test import get_data_from_accounts
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
                        package_date = package_desc.split('|')[-1].strip()
                        
                    else:
                        package_status = 'Ожидаем+'
                
                if "Прибыла" in package_status and not is_date_in_current_week(package_date):
                    continue
                
                package_desc = package_desc.split('|')[0].strip()

            except AttributeError:
                continue
            
            packages.append([package_desc, name, package_track, package_status, package_date])
        
    else:
        return None

    return packages

names = {
    "Уран": "2",
    "Влад": "3",
    "Леша": "4",
    "Антон": "5",
    "Дима": "6",
    "Руслан": "7",
    "Ира": "8",
    "Мекен": "9",
    "Марина": "10",
    "Костя": "11",
    "Сергей": "12",
    "Ксения": "13",
    "Александра": "14",
    "Иван": "15",
    "Валентина": "16",
    "Арина": "17",
    "Ольга": "18",
    "Гульнур": "19",
    'Михаил_П': "20",
    'Михаил_М': "21",
    'Алиса': "22"
}


def data_for_rs():
    packages=[]
    get_data_from_accounts()
    for name in names:
        with open(f'track_package/html_pages/{name}.html', 'r+') as f:
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



def filter_get_and_read():
    """Google Sheets reading"""
    """Авторизация"""
    sa = gspread.service_account()

    """Подключаемся к документу"""
    sh = sa.open("MacPython")

    """Подключаемся к странице и очищаем её"""
    wks = sh.worksheet('Лист15')

    """Получение и чтение данных из аккаунтов LS и таблицы"""
    packages_sheets = wks.get("A26:F55")
    packages_lifeshop = data_for_rs()

    """Словари для обработки и список для хранения данных"""
    pack_sheets = {}
    pack_lifes = {}
    done_packs = []

    """Форматирование данных в словари"""
    for pack_sh in packages_sheets:
        try:
            pack_sheets[pack_sh.pop(2)] = pack_sh
        except IndexError:
            continue


    for pack_ls in packages_lifeshop:
        try:
            pack_lifes[pack_ls.pop(2)] = pack_ls
        except IndexError:
            continue


    # print(pack_sheets)
    """Сравнение данных"""

    for track, package in pack_lifes.items():

        try: #Действия если товар уже записан
            package_s = pack_sheets[track]
            package_l = package_s[:-1]

            if package == package_l:
                package_s.insert(2, track)

            elif package_s[-1] == "TRUE" or package_s[-1] == "ИСТИНА":
                package_s[-3] = package[-2]
                package_s.insert(2, track)

            elif package_s[-3] == "Ожидаем" or '+' in package_s[-3]:
                if "Готова к отправке" == package[-2]:
                    package_s[-3:] = package[-2:] + ["TRUE"]
                    package_s.insert(2, track)
                elif "В пути" in package[-2] or "Отправл" in package[-2]:
                    package_s[-3:] = package[-3:] + [find_previous_tuesday_thursday(package[-1])] + ["ЛОЖЬ"]
                    package_s.insert(2, track)
                elif "Прибыл" in package[-2] or "Таможенн" in package[-2]:
                    package_s[-3:] = package[-3:] + [find_previous_tuesday_thursday(package[-1], 1)] + ["ЛОЖЬ"]
                    package_s.insert(2, track)

            elif package_s[-3] == "Готова к отправке":
                package_s[-3] = package[-2]
                package_s.insert(2, track)

            elif "В пути" in package_s[-3] or "Отправл" in package_s[-3]:
                if "Прибыл" in package[-2] or "Таможенн" in package[-2]:
                    package_s[-3] = package[-2]
                    package_s.insert(2, track)

                elif "В пути" in package[-2] or "Отправл" in package[-2]:
                    package_s[-3] = package[-2]
                    package_s.insert(2, track)

            elif "Прибыл" in package[-2] or "Таможенн" in package[-2]:
                    package_s[-3] = package[-2]
                    package_s[-2] = [find_previous_tuesday_thursday(package[-1], 1)]
                    package_s.insert(2, track)        


            else:
                package.insert(2, track)
                package += ["FALSE"]
                done_packs.append(package)
                continue
            
            done_packs.append(package_s)

        except KeyError:
            if package[-2] == "Ожидаем":
                package += ["FALSE"]

            elif "Готова к отправ" in package[-2]:
                package += ["TRUE"]
            
            elif "Отправ" in package[-2] or "В пути" in package[-2]:
                package[-1] = find_previous_tuesday_thursday(package[-1])
                package += ["FALSE"]

            elif "Таможенное" in package[-2] or "Прибыл" in package[-2]:
                package[-1] = find_previous_tuesday_thursday(package[-1],1)
                package += ["FALSE"]

            elif '+' in package[-2]:
                package += ["FALSE"]
            
            package.insert(2,track)
            done_packs.append(package)

    return done_packs
     



def write_to_table():
    packages = filter_get_and_read()
    dates = calculate_week_dates()
    done_packs = {}
    problem_packs = []
    remaining_packages = []  # Новый список для хранения оставшихся пакетов

    for package in packages:
        package_added = False  # Флаг, чтобы удостовериться, что пакет добавлен только один раз

        for coll_word, date_list in dates.items():
            if '+' in package[-3]:
                problem_packs.append(package)
                package_added = True
                break  # Добавил break, чтобы выйти из внутреннего цикла, если условие выполнилось
                
            elif date_list[0].date() <= datetime.strptime(package[-2].strip(), '%Y-%m-%d').date() <= date_list[1].date():
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
    wks.batch_clear(["B2:L20", "A26:F55"])

    for coord, value in done_packs.items():
        wks.update(coord, ''.join(value))

    wks.update(f'A26:F{26+len(packages)}', packages, value_input_option='USER_ENTERED')



'''
elif 'Готова к' in package[3]:
                package.insert(2, track)
                done_packs.append(package+['TRUE'])

            elif '+' in package[3]:
                package.insert(2, track)
                done_packs.append(package+['FALSE'])

            elif all([package_s[3]=='Ожидаем', 'Готова к' not in package[3], "Прибыла" not in package[3]]):
                package.insert(2,track)
                print(package[-1]+[find_previous_tuesday_thursday(package[-1])]+['FALSE'], 'hello')
                done_packs.append(package[-1]+[find_previous_tuesday_thursday(package[-1])]+['FALSE'])

            else:
                raise

        except KeyError:
            if "Готова к" in package[3]:
                package.insert(2, track)
                done_packs.append(package+['TRUE'])

            elif any(["В пути" in package[3], "Отправл" in package[3]]):
                package[:-1]+[find_previous_tuesday_thursday(package[-1])]+['FALSE']
                done_packs.append(package)

            elif package[3] == "Ожидаем" or '+' in package[3]:
                done_packs.append(package.insert(2, track)+['FALSE'])
    print(done_packs)
    done_packs = sorted(done_packs, key=get_sort_key2)'''
