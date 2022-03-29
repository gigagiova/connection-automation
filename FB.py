import json
import random
import time

from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from assets import fb_connection
from options import options
from regex import group_user_regex
from settings import SCROLLS


class FbAccount:

    def __init__(self, account):
        """Login into facebook"""

        self.driver = webdriver.Chrome(
            service=Service("C:/utility/chromedriver_win32/chromedriver.exe"),
            options=options)
        self.driver.get("https://www.facebook.com/")

        # fetch credentials from JSON file
        cf = open("persistent/credentials.JSON", "r")
        credentials = json.loads(cf.read())[account]
        cf.close()

        # fill email
        email = self.driver.find_element(By.ID, "email")
        email.send_keys(credentials["email"])

        # fill password
        password = self.driver.find_element(By.ID, "pass")
        password.send_keys(credentials["password"])

        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[@title='Only allow essential cookies']").click()
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(2)

    def send_message(self, receiver, group_name="lol"):
        """
        ARGS
            receiver: URL string of receiver's FB account,
            group_name: the name of the group
        """

        # connect to page
        self.driver.get(f"https://www.facebook.com/{receiver}")
        time.sleep(12 + random.randrange(12))
        actions = ActionChains(self.driver)

        # get all buttons that contain the word message
        message_buttons = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Message')]")
        time.sleep(12 + random.randrange(12))

        # You can't send messages to your own profile
        if len(message_buttons) == 0:
            return False

        # click on message form
        message_buttons[0].find_element(By.XPATH, '../..').click()
        time.sleep(2 + random.randrange(2))

        # send message
        actions.send_keys(fb_connection(group_name))
        time.sleep(2 + random.randrange(2))
        actions.perform()
        actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(30 + random.randrange(30))
        return True

    def scroll_down(self, times):
        # how many time we scrolled
        for sc in range(times):

            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            # Wait to load the page.
            time.sleep(3)

    def scrape_batch(self, name, link, previous_batches):

        # if we are not in the group's member page
        if self.driver.current_url != link:
            self.driver.get(link)

        completed = False

        # Get scroll height.
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        # how many profiles we actually contacted

        # how many time we scrolled
        for sc in range(SCROLLS):

            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            # Wait to load the page.
            time.sleep(1)
            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                # not the best code in the world
                # this snippet is made to prevent stopping before the page is actually fully loaded

                for t in range(8):
                    time.sleep(1)
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    if last_height != new_height:
                        break

                if last_height == new_height:
                    # we are done
                    completed = True
                    break

            last_height = new_height

        # executes batch...

        # open uuid history
        history = open("persistent/history.txt", "a+")
        history.seek(0)

        # scrapes all available members
        anchors = self.driver.find_elements(By.TAG_NAME, "a")
        hrefs = map(lambda a: str(a.get_attribute("href")), anchors)
        profiles = set([a for a in hrefs if group_user_regex.match(a)])

        # exclude already batched profiles and get uuid for each one
        new_profiles = set(map(lambda url: url.split("/")[-2], profiles - previous_batches))
        # exclude previously connected profiles
        unconnected_profiles = new_profiles - set(history.read().splitlines())
        print(f"Found {len(unconnected_profiles)} new profiles out of {len(profiles)}")

        # open new tab to write messages
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[1])

        # how many messages we sent at one
        message_counter = 0

        for i, p in enumerate(unconnected_profiles):
            print(f"\r{i + 1} out of {len(unconnected_profiles)}", end="")
            if self.send_message(p, name):
                message_counter += 1
                # saves uuid
                history.write(p + "\n")

            if message_counter == 30:
                # pauses if we surpassed the threshold
                print(f"\rsleeping...", end="")
                message_counter = 0
                time.sleep(300 + random.randrange(300))

        # close previous window and (to be sure) go back to first window
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # new line, since we do not put it during the batch
        print("\n")

        # close history file
        history.close()
        return new_profiles, completed
