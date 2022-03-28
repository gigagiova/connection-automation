from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from options import options

driver = webdriver.Chrome(service=Service("C:/utility/chromedriver_win32/chromedriver.exe"), options=options)

