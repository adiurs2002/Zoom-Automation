from selenium import webdriver
import time
import pyautogui 


driver = webdriver.Firefox()

driver.get('https://zoom.us/join')

id = driver.find_element_by_xpath('//*[@id="join-confno"]')
id.send_keys('Zooom Id')

time.sleep(1)

join = driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()


pyautogui.press('space',presses=1)
time.sleep(1)

pyautogui.press('tab',presses=2)
pyautogui.press('enter',presses=1)
time.sleep(1)

pyautogui.press('tab',presses=4)
pyautogui.press('enter',presses=1)
