from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from rich import print
import pickle
import os

account_name="jalil_khoironi" # Change this to your own Instagram username
SESSION_FILE = 'cookies.pkl'

display = Display(visible=0, size=(800, 600))
display.start()
chromedriver_path ='./chromedriver'
service = Service(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
webdriver = webdriver.Chrome(service=service, options=options)
sleep(5)

def delay():
    sleep(300) #delay in sec   
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
        pass

start()
TRUE_FILE = "1"
FALSE_FILE = "0"
if os.path.exists(TRUE_FILE):
    print("[green][+] Workflow Follow mode[/green]")
    mainConfig = "1"
else :
    if os.path.exists(FALSE_FILE):
        print("[green][+] Workflow Unfollow mode[/green]")
        mainConfig = "0"
    else :
        pass

if mainConfig == "0":
    unfollow()
else:
    follow()
