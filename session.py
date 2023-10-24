from selenium import webdriver
from time import sleep
import pickle
import os
SESSION =  'cookies.pkl'
try:
    os.remove(SESSION)
except OSError as e:
    print({e})
os.system("adb devices")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("androidPackage", "org.chromium.chrome.stable")
webdriver = webdriver.Chrome(options=options)
sleep(5)
webdriver.get('https://www.instagram.com/accounts/login/')
finish = input("()")
pickle.dump(webdriver.get_cookies(), open( SESSION, "wb"))


            
