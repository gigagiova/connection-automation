from time import time
from selenium.webdriver.common.by import By


def Login(driver):
    driver.get("https://www.facebook.com/")

    email = driver.find_element(By.ID, "email")
    email.send_keys("francesco.bruno.cia@gmail.com")

    password = driver.find_element(By.ID, "pass")
    password.send_keys("Gigagiova")

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[@title='Only allow essential cookies']").click()
    driver.find_element(By.NAME, "login").click()
