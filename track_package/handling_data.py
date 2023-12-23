from bs4 import BeautifulSoup
from datetime import datetime
import re
from datetime import datetime, timedelta
from .utils import get_package_interval, is_date_in_current_week, check_date_range
# from .requests_test import get_data_from_accounts


def get_package_week(date, status):

    part = get_package_interval(date)

    if part:

        if "Готова" in status:
            if "lw: fri-wed" in part:
                return "Next: part #1"
            elif "cw: wed-fri" in part:
                return "Next: part #2"
            elif "cw: fri-wed" in part:
                return "Later: part #1"
            
        elif "Отправ" in status or "В пути" in status:
            if "lw: wed-fri" in part:
                return "Current: part #1"
            
            elif "lw: fri-wed" in part:
                return "Current: part #2"
            
            elif "cw: wed-fri" in part:
                return "Next: part #1"
            
            elif "cw: fri-wed" in part:
                return "Next: part #2"
            
        elif "Таможенное" in status:
            if is_date_in_current_week(date):
                return "Current: part #2"
            
            ##ToDo

        elif "Прибыла" in status and is_date_in_current_week(date):

            if "cw: wed-fri" in check_date_range(date):
                return "Current: part #1"
            
            elif "cw: fri-wed" in check_date_range(date):
                return "Current: part #2"

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
                # package_price = package_text[1].strip()

                package_amount = package_text[-1].strip()

                date_of_receipt = get_package_week(package_date.strip(), package_status)

            except AttributeError:
                continue

            if date_of_receipt:
                packages.append([package_desc, name, package_weight, f'{round(float(package_weight)*12, 2)}', package_track, date_of_receipt, package_amount])
        
    else:
        return None
    return packages