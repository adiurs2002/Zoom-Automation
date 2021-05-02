import pyautogui
import json
import time
import sys
# import webbrowser


# def classLogger(classid):
# #    # url = 'https://zoom.us/j/'+str(classid)+'?from=join'
# #     url = 'https://zoom.us/wc/join/'+str(classid)
# #     webbrowser.open_new_tab(url)
#  driver.get('https://zoom.us/join')

# id = driver.find_element_by_xpath('//*[@id="join-confno"]')
# id.send_keys('str(classid)')

# time.sleep(1)

# join = driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()


# pyautogui.press('space',presses=1)
# time.sleep(1)

# pyautogui.press('tab',presses=2)
# pyautogui.press('enter',presses=1)
# time.sleep(1)

# pyautogui.press('tab',presses=4)
# pyautogui.press('enter',presses=1)


# def initLogin():
#     try:
#         with open('data.txt') as rfile:
#             data = json.load(rfile)

#     except Exception as e:
#         print('first import classid data from getdata.py')

#     try:
#         cString = 'class'+str(sys.argv[1])
#         if(data[cString]):
#             print("logging into class....")
#             time.sleep(2)
#             classLogger(data[cString])

#     except Exception as e:
#         print('no such class exists')



# initLogin()
# def json():
#     x =open('data.txt',)
#     data = json.load(x)

#     print(data)


#     x.close

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
    driver = webdriver.Firefox()

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

