import pyautogui
import json
import time
import sys

def initLogin():
    try:
        with open('data.txt') as rfile:
            data = json.load(rfile)

    except Exception as e:
        print('first import classid data from getdata.py')

    try:
        cString = 'class'+str(sys.argv[1])
        
        if(data[cString]):
            print("logging into "+ cString)
            time.sleep(2)
            classLogger(data[cString])

    except Exception as e:
        print(e)

def classLogger(classid):
    
    from selenium import webdriver
    driver = webdriver.Firefox() #below automation only works on Firefox 

    driver.get('https://zoom.us/join')

    id = driver.find_element_by_xpath('//*[@id="join-confno"]')
    id.send_keys(str(classid))

    time.sleep(1)

    join = driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()


    pyautogui.press('space',presses=1)
    time.sleep(1)

    pyautogui.press('tab',presses=2)
    pyautogui.press('enter',presses=1)
    time.sleep(1)

    pyautogui.press('tab',presses=4)
    pyautogui.press('enter',presses=1)

initLogin()

