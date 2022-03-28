import random
import time

from selenium.webdriver.common.by import By

from FB import send_message
from driver import driver
from regex import group_user_regex


class FbGroupScraper:

    def __init__(self, url, group_name):
        driver.get(url)
        self.name = group_name
        self.previous_batches = set()

    def execute_batch(self):

        # scrapes all available members
        anchors = driver.find_elements(By.TAG_NAME, "a")
        hrefs = map(lambda a: str(a.get_attribute("href")), anchors)
        profiles = set([a for a in hrefs if group_user_regex.match(a)])

        # exclude already batched profiles
        new_profiles = profiles - self.previous_batches
        print(f"Found {len(new_profiles)} new profiles out of {len(profiles)}")
        # save all profiles to not repeat them
        self.previous_batches.update(new_profiles)

        # open new tab to write messages
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[1])

        history = open("persistent/history.txt", "a+")
        for i, p in enumerate(new_profiles):
            print(f"\n{i} out of {len(new_profiles)}", end="")
            send_message(p, self.name, history)

            if i == 35:
                # pauses if the batch is too big
                print(f"\nsleeping...", end="")
                time.sleep(600 + random.randrange(600))

        # close previous window and (to be sure) go back to first window
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # close history file
        history.close()
        print(f"\nsleeping...", end="")
        time.sleep(900 + random.randrange(900))

    def start(self):
        """A method for scrolling the page."""

        # Get scroll height.
        last_height = driver.execute_script("return document.body.scrollHeight")
        # how many time we scrolled
        counter = 0

        while True:

            # Scroll down to the bottom.
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            counter += 1

            # when we buffered 250 or more people
            if counter >= 5:
                counter -= 5
                self.execute_batch()

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
