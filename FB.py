import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def login(driver):
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


def scroll_down(driver):
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
                print(f'{last_height} == {new_height}')
                if last_height != new_height:
                    break

            if last_height == new_height:
                break

        last_height = new_height


def sendMessage(receiver, driver):
    """
    ARGS
        receiver: URL string of receiver's FB account
        driver: self explanatory unless you are FB
    """

    text = f"""Ciao! Ho trovato il tuo profilo su .Assieme a dei miei amici developer vogliamo aiutare i gamer a migliorare le loro skills e diventare pro.
            Sarebbe molto utile per noi poterti fare qualche domanda per capire le difficoltà che i gamer incontrano ed elaborare una giusta soluzione.
            Qual'è il momento migliore in cui potremmo sentirci per una breve intervista informale?"""

    # connect to page
    driver.get(receiver)
    actions = ActionChains(driver)

    # click on message form
    driver.find_elements(By.XPATH, "//span[contains(text(), 'Messaggio')]")[0].find_element(By.XPATH, '../..').click()

    # send message
    actions.send_keys(text)
    actions.perform()
    actions.send_keys(Keys.ENTER)
    actions.perform()
