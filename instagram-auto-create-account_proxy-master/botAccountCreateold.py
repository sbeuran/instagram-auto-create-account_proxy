from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse
import pandas as pd
from selenium.webdriver.common.proxy import Proxy, ProxyType
from numpy import random
from time import sleep
import random

# from pandas import ExcelWriter
# from pandas import ExcelFile
# from pandas import DataFrame
# from openpyxl import Workbook


def configure_api_firefox():
    api_key = 'fe5e06bc8ba3b0d4d5c7222b8b8e7a71'
    print("Input the key in the extension: {} and save then press Enter in console.".format(api_key))
    nothing = input()


ext_path = 'C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ls8isr8l.default-release\\extensions\\{487609b5-5ca6-4c62-8523-11f3e1db851c}.xpi'
list_user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0']
i = 1

for i in range(1, 5):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
    group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")

    args = parser.parse_args()

    ua = UserAgent()
    userAgent = ua.random
    userAgent = random.choice(list_user_agents)
    print(userAgent)

    if args.firefox:
        with open('proxy.txt','r') as file:
            countriesStr = file.read()
        PROXY_HOST = countriesStr.split(":")[0]
        PROXY_PORT = countriesStr.split(":")[1]
        profile = webdriver.FirefoxProfile()
        profile.set_preference("xpinstall.signatures.required", False)
        profile.set_preference("intl.accept_languages", "en-US")
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http",PROXY_HOST)
        print(PROXY_HOST)
        profile.set_preference("network.proxy.http_port",int(PROXY_PORT))
        print(int(PROXY_PORT))
        profile.set_preference("general.useragent.ovrride", userAgent)
        profile.update_preferences()
        try:
            driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"C:\\Users\Administrator\Downloads\\instagram-auto-create-account_proxy-master\\instagram-auto-create-account_proxy-master\\geckodriver.exe")
            driver.install_addon(ext_path)
            configure_api_firefox()
        except:
            driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"geckodriver.exe")
            driver.install_addon(ext_path)
            configure_api_firefox()


    if args.chrome:
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument("--lang=en")
        options.add_extension('anticaptcha.zip')
        options.add_argument(f'user-agent={userAgent}')
        try:
            driver = webdriver.Chrome(options=options, executable_path=r"C:\\Users\Administrator\Downloads\\instagram-auto-create-account_proxy-master\\instagram-auto-create-account_proxy-master\\chromedriver.exe")
        except:
            driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

    driver.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(8)
    name = account.username()
    #//button[text()='Accept']
    try:
        driver.find_element_by_xpath("//button[text()='Accept']").click()
    except:
        pass

    #Fill the email value
    email_field = driver.find_element_by_name('emailOrPhone')
    fake_email = email.getFakeMail()
    email_field.send_keys(fake_email)
    print(fake_email)

    # Fill the fullname value
    fullname_field = driver.find_element_by_name('fullName')
    fullname_field.send_keys(account.generatingName())
    print(account.generatingName())
    # Fill username value
    username_field = driver.find_element_by_name('username')
    username_field.send_keys(name)
    print(name)
    # Fill password value
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(account.generatePassword())  # You can determine another password here.
    paw = account.generatePassword()
    print(account.generatePassword())
    time.sleep(8)

    driver.find_elements_by_class_name('L3NKy')[1].click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()

    time.sleep(8)

    #Birthday verification
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
    time.sleep(3)
    #
    fMail = fake_email[0].split("@")
    mailName = fMail[0]
    domain = fMail[1]
    instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
    old_url = driver.current_url
    driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
    time.sleep(8)
    curr = driver.current_url
    while curr == old_url:
        time.sleep(2)
        curr = driver.current_url
    if 'challenge' in curr:
        time.sleep(2)
        recaptcha_iframe = driver.find_element_by_id('recaptcha-iframe')
        driver.switch_to.frame(recaptcha_iframe)
        while 1:
            status = driver.find_element_by_class_name('status').get_attribute('innerHTML')
            if status == 'Solved':
                break
        driver.switch_to.default_content()
        driver.find_element_by_class_name('L3NKy').click()
    driver.navigate().to("https://www.instagram.com/growthfxtrading/")
    sleeptime = random.uniform(2, 4)
    print("sleeping for:", sleeptime, "seconds")
    sleep(sleeptime)
    print("sleeping is over")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Follow']"))).click()
    


    with open("test.txt", "a") as myfile:
        myfile.write(str(fake_email)+"\n")
        myfile.write(str(name)+"\n")
        myfile.write(str(name)+"\n")
        myfile.write("--------------------------------------------------  \n")
