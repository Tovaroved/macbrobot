from bs4 import BeautifulSoup
from datetime import datetime
import re
from datetime import datetime, timedelta


def get_previous_weekday(d, weekday):
    days_until_previous_weekday = (d.weekday() - weekday + 7) % 7
    return d - timedelta(days=days_until_previous_weekday)

def get_next_weekday(d, weekday):
    days_until_next_weekday = (weekday - d.weekday() + 7) % 7
    return d + timedelta(days=days_until_next_weekday)

def is_date_this_week(date_str):
    date_to_check = datetime.strptime(date_str, "%Y-%m-%d")

    today = datetime.now()

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    if start_of_week <= date_to_check <= end_of_week:
        return True
    else:
        return False


def get_package_week(date, status):
    today = datetime.today()
    input_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    current_week_wednesday = get_previous_weekday(today, 2).strftime("%Y-%m-%d")
    previous_week_wednesday = get_previous_weekday(today - timedelta(weeks=1), 2).strftime("%Y-%m-%d")
    next_week_wednesday = get_next_weekday(today + timedelta(weeks=1), 2).strftime("%Y-%m-%d")

    if 'Готова' in status:
        if is_date_this_week(date):
            return 'A week later'
        
        elif not is_date_this_week(date):
            return 'Next week'
    
    elif 'В пути' in status:
        if is_date_this_week(date):
            return 'Next week'
        
        elif not is_date_this_week(date):
            return 'Current week'

    else:
        return None


def get_formatted_data(account_html_code, name: str):
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

                package_weight = re.sub(r'[^\d.]', '',package.find('div', class_='w-fit rounded-full px-2 text-sm font-medium bg-lime-100 text-lime-600').text.strip())

                package_status = package.find('div', class_='flex items-center gap-x-1').text.strip()

                package_date = package.find('div', class_='text-xs text-gray-500').text.strip().replace('\n', '')[-10:]

                package_desc = package_text[0].strip()

                package_price = package_text[1].strip()

                package_amount = package_text[-1].strip()

                date_of_receipt = get_package_week(package_date, package_status)

            except AttributeError:
                continue

            if date_of_receipt:
                packages.append([package_desc, name, package_weight, f'{round(float(package_weight)*12, 2)}', package_track, date_of_receipt, package_amount])
        
    else:
        return None
    return packages



