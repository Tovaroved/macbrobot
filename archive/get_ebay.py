# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()

# driver.get("https://signin.ebay.com/signin/")

# time.sleep(500)

# login_form = driver.find_element(value="userid")

# login_form.send_keys("oguseva1996@gmail.com")

# time.sleep(5)

# submit_continue = driver.find_element(value="signin-continue-btn")

# submit_continue.click()

# time.sleep(5)

# pass_form = driver.find_element(by=By.ID, value="pass")

# pass_form.send_keys("Macbro4Olg1")

# signin_btn = driver.find_element(value="sgnBt")

# signin_btn.click()

# time.sleep(5)

# try:
#     skip = driver.find_element(value="passkeys-cancel-btn")

#     skip.click()
#     time.sleep(5)
# except:
#     print("Blya")