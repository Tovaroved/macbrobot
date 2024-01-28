# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time


"""Тестрирование возможности повторного открытия вкладки браузера"""

# driver = webdriver.Chrome()
# executor_url = driver.command_executor._url
# session_id = driver.session_id
# driver.get("https://signin.ebay.com/signin/")

# time.sleep(60)

# driver.close()

# print (session_id)
# print (executor_url)

# options = Options()
# driver2 = webdriver.Remote(command_executor=executor_url, options=options)
# time.sleep(10)

# driver2.session_id = session_id
# print (driver2.current_url)



# """Пример скачивания файлов по ссылке"""
# import requests
 
# url = 'http://flibusta.site/b/697746/epub'
# response = requests.get(url)
 
# with open('grokaem.epub', 'wb') as file:
#     file.write(response.content)
