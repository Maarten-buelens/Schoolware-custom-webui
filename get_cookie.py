from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")
#options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options)
driver.get("https://kov.schoolware.be/webleerling/start.html#!fn=llagenda")
driver.implicitly_wait(10)
office_button = driver.find_element(By.XPATH, '//*[@id="ext-comp-1014"]').click()
f=open("/var/www/user","r")
user = f.read()
f.close()
user = driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(user, Keys.ENTER)
sleep(4)
passwd = driver.find_element(By.XPATH, '//*[@id="i0118"]')
f=open("/var/www/pas","r")
pas = f.read()
f.close()
passwd.send_keys(pas)
sleep(4)
passwd_button = driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div').click()
sleep(1)
try:
    all_cookies=driver.get_cookies()
    cookies_dict = {}
    for cookie in all_cookies:
        cookies_dict[cookie['name']] = cookie['value']
    print(cookies_dict.get('FPWebSession'))
    FPWebSession = cookies_dict.get('FPWebSession')
except:
    print("no cookie so sleeping")
    sleep(2)
    all_cookies=driver.get_cookies()
    cookies_dict = {}
    for cookie in all_cookies:
        cookies_dict[cookie['name']] = cookie['expiry']
    print(cookies_dict.get('FPWebSession'))
    FPWebSession = cookies_dict.get('FPWebSession')



try:
    cookie = open("/var/www/cookie", "x")
    cookie.close()
except:
    a=1
try:
    cookie = open("/var/www/cookie" , "w")
    cookie.write(str(FPWebSession))
    cookie.close()
except:
    cookie.close()
    print("error writing cookie")
driver.close()
