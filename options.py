from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

# headless options
options.headless = True
options.add_argument("--window-size=1920x1080")
