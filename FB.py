import time
import re

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from assets import fb_connection
from driver import driver


def login():
    """Login into facebook"""

    driver.get("https://www.facebook.com/")

    email = driver.find_element(By.ID, "email")
    email.send_keys("francesco.bruno.cia@gmail.com")

    password = driver.find_element(By.ID, "pass")
    password.send_keys("Gigagiova")

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[@title='Only allow essential cookies']").click()
    driver.find_element(By.NAME, "login").click()
    time.sleep(2)


def scroll_down():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(1)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            # not the best code in the world
            # this snippet is made to prevent stopping before the page is actually fully loaded

            for t in range(8):
                time.sleep(1)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if last_height != new_height:
                    break

            if last_height == new_height:
                break

        last_height = new_height


def sendMessage(receiver, group_name):
    """
    ARGS
        receiver: URL string of receiver's FB account
    """

    # connect to page
    driver.get(receiver)
    actions = ActionChains(driver)

    # get all buttons that contain the word message
    message_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Messaggio')]")
    if len(message_buttons) == 0:
        # probably our own profile
        return

    # click on message form
    message_buttons[0].find_element(By.XPATH, '../..').click()
    time.sleep(6)

    # send message
    actions.send_keys(fb_connection(group_name))
    actions.perform()
    actions.send_keys(Keys.ENTER)
    actions.perform()


def scrapeGroup(url, name):

    driver.get(url)
    scroll_down()

    r = re.compile(r'https://www.facebook.com/groups/\d+/user/\d+/')
    anchors = map(lambda a: str(a.get_attribute("href")), driver.find_elements(By.TAG_NAME, "a"))
    profiles = set([a for a in anchors if r.match(a)])

    for p in profiles:
        sendMessage(p, name)
