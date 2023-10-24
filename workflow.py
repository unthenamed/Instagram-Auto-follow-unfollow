from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pickle
import os

account_name="jalil_khoironi"
SESSION_FILE = 'cookies.pkl'

chrome_service = Service(ChromeDriverManager().install())
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=360,640",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
]
for option in options:
    chrome_options.add_argument(option)
webdriver = webdriver.Chrome(service=chrome_service, options=chrome_options)
sleep(5)
def follow() :
    webdriver.get('https://www.instagram.com/explore/people/')
    sleep(5)
    followbutton = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/div/div/div[1]/div/div/div/div[3]/div/button/div/div"
    follownow = webdriver.find_element(By.XPATH, followbutton)
    follownow.click()
def unfollow() :
    webdriver.get('https://www.instagram.com/{}/following/'.format(account_name))
    sleep(5)
    selectunfollow = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div')
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
