from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

driver = webdriver.Chrome('C:/Users/user/Desktop/python/test/chromedriver.exe')
url = 'https://www.incheoncc.com:1436/login/login.asp'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
