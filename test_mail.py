from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

driver = webdriver.Chrome('C:/Users/user/Desktop/python/test/chromedriver.exe')
url = 'https://accounts.google.com/ServiceLogin/signinchooser?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


driver.find_element_by_xpath('//*[@id="identifierId"]').click()
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('beomsun2017@gmail.com')
driver.find_element_by_class_name("VfPpkd-vQzf8d").click()




