import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from FB import login, scroll_down
from options import options

driver = webdriver.Chrome(service=Service("C:/utility/chromedriver_win32/chromedriver.exe"), options=options)

login(driver)

driver.get("https://www.facebook.com/groups/319516465411062/members")

scroll_down(driver)

r = re.compile(r'https://www.facebook.com/groups/\d+/user/\d+/')
anchors = map(lambda a: str(a.get_attribute("href")), driver.find_elements(By.TAG_NAME, "a"))
profiles = set([a for a in anchors if r.match(a)])

for a in profiles:
    print(a)
