from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pickle
import os

SESSION_FILE = 'cookies.pkl'
chrome_service = Service(ChromeDriverManager().install())
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1024,1024",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)
webdriver = webdriver.Chrome(service=chrome_service, options=chrome_options)
sleep(5)
def poppup() :
    try:
        save_info = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        save_info.click()
    except :
        pass
    try:
        notnow = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notnow.click() 
    except :   
        pass
def follow() :
    webdriver.get('https://www.instagram.com/explore/people/')
    sleep(5)
    followbutton = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/button/div/div"
    follownow = webdriver.find_element(By.XPATH, followbutton)
    follownow.click()
def unfollow() :
    webdriver.get('https://www.instagram.com/jalil_khoironi/following/')
    sleep(2)
    poppup()
    selectunfollow = webdriver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[3]/div/button')
    selectunfollow.click()
    sleep(2)
    unfollowbutton = webdriver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
    unfollowbutton.click()
    sleep(2)
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
