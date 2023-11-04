import requests
from bs4 import BeautifulSoup
from selenium import webdriver


all_banks_rate_data = {}

def get_rates():

    """Finca"""

    finca = 'https://www.fincabank.kg/#tab-737b3e61323d0b75ad8'


    request = requests.get(finca)

    soup = BeautifulSoup(request.text, 'lxml')

    rates_table = soup.find('div', class_='fusion-fullwidth fullwidth-box fusion-builder-row-2 fusion-parallax-none nonhundred-percent-fullwidth non-hundred-percent-height-scrolling').find(attrs={'class':'tab-pane fade fusion-clearfix', 'id':'tab-737b3e61323d0b75ad8'})

    usd, rub = rates_table.find_all('div', class_='fif-planes-row')[1], rates_table.find_all('div', class_='fif-planes-row')[3]

    all_banks_rate_data['finca'] = [float(usd.find_all('div', class_='fif-planes-col2 fif-planes-center')[2].text.strip()), float(rub.find_all('div', class_='fif-planes-col2 fif-planes-center')[1].text.strip())]


    """Bakai"""

    driver = webdriver.Safari()

    bakai = 'https://bakai.kg/ru/'

    driver.get(bakai)

    source = driver.page_source

    soup = BeautifulSoup(source, 'lxml')

    table_ = soup.find(attrs={'class':'tab_item', 'id':'non_cash_tab'})

    rub = table_.find(attrs={'id':'currency_RUB'}).find('td', class_='currency_buy').text

    usd = table_.find(attrs={'id':'currency_USD'}).find('td', class_='currency_sell').text

    all_banks_rate_data['bakai'] = [float(usd), float(rub)]

    driver.close()


    """Ayil"""

    ayil = 'https://ab.kg'

    request = requests.get(ayil)

    soup = BeautifulSoup(request.text, 'lxml')

    all_courses = soup.find_all('div', class_='tabs-descr__content')[1].find('tbody').find_all('tr')

    rub = all_courses[2].find_all('td')[1].text

    usd = all_courses[0].find_all('td')[2].text

    all_banks_rate_data['ayil'] = [float(usd), float(rub)]


    """kompanion"""


    kompanion = 'https://www.kompanion.kg'

    request = requests.get(kompanion)

    soup = BeautifulSoup(request.text, 'lxml')

    all_courses = soup.find('div', class_="course_widget").find_all('div', class_='tab-pane')[1].find('table', class_='table course').find_all('tr')

    rub = all_courses[3].find_all('td')[1].text

    usd = all_courses[1].find_all('td')[2].text

    all_banks_rate_data['kompanion'] = [float(usd), float(rub)]



    """Optima"""


    optima = 'https://www.optimabank.kg/index.php?lang=ru'

    request = requests.get(optima)

    soup = BeautifulSoup(request.text, 'lxml')

    all_courses = soup.find('div', id='tab-cashless').find('div', class_='nbrates_head')

    rub = all_courses.find('div', class_='row1 iso-RUB').find('div', class_='rate buy').find('span', class_='up').text

    usd = all_courses.find('div', class_='row0 iso-USD').find('div', class_='rate sell').find('span', class_='up').text

    all_banks_rate_data['optima'] = [float(usd), float(rub)]



    """Keremet"""


    keremet = 'https://keremetbank.kg'

    request = requests.get(keremet)

    soup = BeautifulSoup(request.text, 'lxml')

    all_courses = soup.find('div', class_='course_block').find('div', id='rosin_beznal').find('tbody').find_all('tr')

    rub = all_courses[2].find_all('td')[1].text

    usd = all_courses[0].find_all('td')[2].text

    all_banks_rate_data['keremet'] = [float(usd), float(rub)]


    """mbank"""

    import json

    mbank = 'https://mbank.kg'

    request = requests.get(mbank)

    soup = BeautifulSoup(request.text, 'lxml')

    json_ = soup.find('script', id='__NEXT_DATA__').text

    with open('mbank.json', 'w') as f:
        f.write(json_)

    with open('mbank.json', 'r+') as f:
        data = json.loads(f.read())

    all_courses = data['props']['pageProps']['mainPage']['exchange']['cash_exchange'][1]['values']

    rub = all_courses[2]['buy']

    usd = all_courses[0]['sell']

    all_banks_rate_data['mbank'] = [float(usd), float(rub)]


    """KICB"""


    kicb = 'https://kicb.net/welcome/'

    request = requests.get(kicb)

    soup = BeautifulSoup(request.text, 'lxml')

    all_courses = soup.find('div', class_='curency').find_all('div', class_='con')[1].find_all('div', class_='cur_line')

    rub = all_courses[3].find('div', class_='data2').text

    usd = all_courses[1].find('div', class_='data3').text

    all_banks_rate_data['kicb'] = [float(usd), float(rub)]

    return all_banks_rate_data