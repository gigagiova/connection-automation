import json
import random
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from assets import fb_connection
from driver import driver


def login():
    """Login into facebook"""

    driver.get("https://www.facebook.com/")

    # fetch credentials from JSON file
    cf = open("persistent/credentials.JSON", "r")
    credentials = json.loads(cf.read())
    cf.close()

    # fill email
    email = driver.find_element(By.ID, "email")
    email.send_keys(credentials["email"])

    # fill password
    password = driver.find_element(By.ID, "pass")
    password.send_keys(credentials["password"])

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[@title='Only allow essential cookies']").click()
    driver.find_element(By.NAME, "login").click()
    time.sleep(2)


def send_message(receiver, group_name, history):
    """
    ARGS
        receiver: URL string of receiver's FB account
    """

    history.seek(0)
    uuids = history.read().splitlines()
    uuid = receiver.split("/")[-2]

    # check if we already sent a message
    if uuid in uuids:
        return

    # connect to page
    driver.get(receiver)
    actions = ActionChains(driver)

    # get all buttons that contain the word message
    message_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Messaggio')]")

    # You can't send messages to your own profile
    if len(message_buttons) == 0:
        return

    # click on message form
    message_buttons[0].find_element(By.XPATH, '../..').click()
    time.sleep(30 + random.randrange(30))

    # send message
    actions.send_keys(fb_connection(group_name))
    actions.perform()
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # save uuid
    history.write(uuid + "\n")
    time.sleep(30 + random.randrange(30))

