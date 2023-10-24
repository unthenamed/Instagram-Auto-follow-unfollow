from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pickle
import os

SESSION_FILE = 'cookies.pkl'
display = Display(visible=0, size=(1600, 1600))
display.start()
chromedriver_path ='./chromedriver'
service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1024,1024")
webdriver = webdriver.Chrome(service=service, options=options)
sleep(5)
def follow() :
    webdriver.get('https://www.instagram.com/explore/people/')
    sleep(10)
    followbutton = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/button/div/div"
    follownow = webdriver.find_element(By.XPATH, followbutton)
    follownow.click()
def unfollow() :
    webdriver.get('https://www.instagram.com/jalil_khoironi/following/')
    sleep(5)
    selectunfollow = webdriver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[3]/div/button')
    selectunfollow.click()
    sleep(5)
    unfollowbutton = webdriver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
    unfollowbutton.click()
    sleep(5)
def start() :
    if os.path.exists(SESSION_FILE):
        webdriver.get('https://www.instagram.com/accounts/login/')
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            webdriver.add_cookie(cookie) 
    else :
        pass
TRUE_FILE = "1"
FALSE_FILE = "0"
if os.path.exists(TRUE_FILE):
    mainConfig = "1"
else :
    if os.path.exists(FALSE_FILE):
        mainConfig = "0"
    else :
        mainConfig = input("  () Auto Follow or Unfollow? 1=follow;0=unfollow :")
start()
if mainConfig == "0":
    unfollow()
else:
    follow()
