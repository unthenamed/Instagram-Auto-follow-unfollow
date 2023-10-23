from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from datetime import datetime, timedelta
from rich import print
import time
import pickle
import os

SESSION_FILE = 'cookies.pkl'
display = Display(visible=0, size=(800, 600)) #size virtualdisplay
display.start()
#for chormedriver
chromedriver_path ='./chromedriver' # Change this to your own chromedriver path!
service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
webdriver = webdriver.Chrome(service=service, options=options)
#for firefoxdriver
# i = __file__.rfind('/')
# webdriver = webdriver.Firefox(executable_path=__file__[:i + 1] + 'geckodriver.exe')
sleep(5)

def delay():
    sleep(300) #delay in sec

def clear_text(element):
            length = len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            print("[green]--> Remove {} ..[/green]".format(element).text)

def login() :
    # Visit loginpage    
    webdriver.get('https://www.instagram.com/accounts/login/')
    print("[green][+]Waiting Page redy[/green]")
    result = input("Press Enter to next setup...")

    # Skip the cookie banner
    #button_login = webdriver.find_element(By.XPATH, '//*[@id="mount_0_0_r2"]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div/div[2]/div[3]/span/div')
    #button_login.click()
    #sleep(3)

    # Email & Password inputs
    print("[green][+]Input User[/green]")
    username = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
    clear_text(username) 
    username.send_keys(account_name)
    password = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
    clear_text(password) 
    password.send_keys(account_password)

    # Submit Login
    button_login = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')
    button_login.click()
    print("[green][+]Submit login ...[/green]")

    # Optional save info popup
    delay()
    try:
        save_info = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        save_info.click()
        print("[green]--> optional saveinfo[/green]")
    except :
        print("[red]--> optional saveinfo erorr[/red]")
        pass

    # Optional notifications popup
    delay()
    try:
        notnow = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notnow.click() 
        print("[green]--> optional popup[/green]")
    except :
        print("[red]--> optional popup erorr[/red]")
        pass
        
def follow() :
    print("[red][+] Open Recommend frend page. [/red]")
    webdriver.get('https://www.instagram.com/explore/people/')
    delay()
    i = 1
    while i < 31:
        followbutton = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/div/div/div[{}]/div/div/div/div[3]/div/button/div/div".format(i)
        namefoxhr = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/div/div/div[{}]/div/div/div/div[2]/div/div/div/span/div/a/div/div/span".format(i)
        try:
            namenow = webdriver.find_element(By.XPATH, namefoxhr).text
            print("[blue]--> Following {} [/blue]".format(namenow))
            follownow = webdriver.find_element(By.XPATH, followbutton)
            follownow.click()
            delay()
        except :
            pass
        i = i + 1 

def unfollow() :
    print("[red][+] Open unfollow frend page. [/red]")
    while 1 < 5:
        try:
            webdriver.get('https://www.instagram.com/{}/following/'.format(account_name))
            sleep(10)
            selectunfollow = webdriver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div')
            selectunfollow.click()
            sleep(5)
            try:
                unnamenow = webdriver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div/span').text
                print("[blue]--> {} [/blue]".format(unnamenow))
            except :
                pass
            delay()
            unfollowbutton = webdriver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
            unfollowbutton.click()
            sleep(5)
        except :
            pass

def start() :
    if os.path.exists(SESSION_FILE):
        webdriver.get('https://www.instagram.com/accounts/login/')
        print("[green][+]login with session...[/green]")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            webdriver.add_cookie(cookie) 
    else :
        login()
        pickle.dump(webdriver.get_cookies(), open("cookies.pkl", "wb"))

def loop(element):
    try:
        while 1 < 2:
            element()
    except :
        pass


# Setup credentials
account_name="" # Change this to your own Instagram username
account_password="" # Change this to your own Instagram password



start()

TRUE_FILE = "1"
FALSE_FILE = "0"
if os.path.exists(TRUE_FILE):
    mainConfig = "1"
else :
if os.path.exists(FALSE_FILE):
    mainConfig = "0"
else :                    
#mainConfig = input("  () Auto Follow or Unfollow? 1=follow;0=unfollow :")
if mainConfig == "0":
    loop(unfollow)
else:
    loop(follow)
