import re

from selenium.webdriver.common.by import By

from FB import login, scroll_down, sendMessage, scrapeGroup
from driver import driver

login()


scrapeGroup("https://www.facebook.com/groups/279412284353127/members", "gg")
