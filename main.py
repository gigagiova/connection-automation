import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from FB import Login
from options import options

driver = webdriver.Chrome(executable_path="C:/utility/chromedriver_win32/chromedriver.exe", options=options)

Login(driver)

driver.get("https://www.facebook.com/groups/368096750277850")

driver.implicitly_wait(5)
members = driver.find_elements(By.XPATH, "//span[contains(text(), 'Persone')]")
driver.implicitly_wait(2)
members[1].find_element(By.XPATH, '../..').click()
time.sleep(2)

members = map(lambda a: a.get_attribute("href"), set(driver.find_elements(By.TAG_NAME, "a")))

