
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse
from selenium.webdriver.common.by import By
parser = argparse.ArgumentParser()
parser.add_argument('--username', dest = 'username')
parser.add_argument('--password', dest = 'password')
args = parser.parse_args()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browserstack.local import Local
from selenium.common.exceptions import NoSuchElementException

bs_local = Local()

# You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
bs_local_args = {"key": "2ZjTfYoi48HSCpsXUt2U"}

# Starts the Local instance with the required arguments
bs_local.start(**bs_local_args)

# Check if BrowserStack local instance is running
print(bs_local.isRunning())

desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 11',
    'realMobile': 'true',
    'os_version': '14.0',
    'name': 'BStack-[Python] Sample Test',  # test name
    'build': 'BStack Build Number 1',  # CI/CD job or build name
    'browserstack.local': 'true'
}

driver = webdriver.Remote(
    command_executor='https://rezzaernest_yZUNqf:2ZjTfYoi48HSCpsXUt2U@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
#FullScreen
driver.maximize_window()
#Opens TCC
driver.get("https://tcc.geziko.com/tcc/faces/faces/login.xhtml")
#Enter username

email = driver.find_element_by_id('j_idt19:username')
email.send_keys(args.username)
#Enter Password
password = driver.find_element_by_id('j_idt19:password')
password.send_keys(args.password)
loginbutton = driver.find_element_by_name('j_idt19:j_idt23')
loginbutton.click()
title = "TCC - V4"
assert title == "TCC - V4"