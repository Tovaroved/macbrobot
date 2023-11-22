from bs4 import BeautifulSoup
from utils import get_sort_key, is_date_in_current_week


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

                if "Ожид" in package_status:
                    # print(package_desc.split('|')[-1].strip())
                    if len(package_desc.split('|')[-1].strip()) == 10:
                        package_date = package_desc.split('|')[-1]
                        
                    else:
                        package_status = 'Ожидаем+'
                        package_desc = 'XXX - ' + package_desc

                
                
                if "Прибыла" in package_status and not is_date_in_current_week(package_date):
                    continue
                
                package_desc = package_desc.split('|')[0].strip()

            except AttributeError:
                continue
            
            packages.append([package_desc, name, package_track, package_price, package_status, package_date])
        
    else:
        return None

    return packages

names = [
    "Уран",
    "Влад",

    "Валентина",
    "Алиса",

]

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


for i in data_for_rs():
    print(i)