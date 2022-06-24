import argparse

from selenium import webdriver

parser = argparse.ArgumentParser()
parser.add_argument('--username', dest = 'username')
parser.add_argument('--password', dest = 'password')
args = parser.parse_args()

driver = webdriver.Chrome(executable_path=r"/Users/rezzaernest/Downloads/Instrallers/Drivers/chromedriver")
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
