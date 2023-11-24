from bs4 import BeautifulSoup
import re


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

                package_date = package.find('div', class_='text-xs text-gray-500').text.strip().replace('\n', '')[-10:]

                package_amount = package_text[-1].strip()

                package_desc = package_text[0].strip() if int(package_amount) == 1 else f'{package_amount}шт {package_text[0].strip()}'

                package_price = package_text[1].strip()

                if "Ожидаем" in package_status:
                    package_date = package_text.split('|')[-1]
            
            except AttributeError:
                continue
            
            packages.append([package_desc, name, package_track, package_price, package_status, package_date])
        
    else:
        return None
    return packages