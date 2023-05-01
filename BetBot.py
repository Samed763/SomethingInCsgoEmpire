from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service= Service("./chromedriver")
driver=webdriver.Chrome(service=service)
driver.get("https://csgoempire.com/")
time.sleep(120)
accountbalance= driver.find_element(By.XPATH,'//*[@id="empire-header"]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span/div/span')
convert=  accountbalance.text
convert=convert.replace(',','.')
balance = float(convert)
previousbalance=float(convert)
print(balance)
while (True ):
    accountbalance= driver.find_element(By.XPATH,'//*[@id="empire-header"]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span/div/span')
    convert=  accountbalance.text
    convert=convert.replace(',','.')
    balance = float(convert)
    timer=driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[2]/div[3]/div/div[2]').text
    timer=timer.replace(',','.')
    if(timer==''):
        time.sleep(1)
        continue
        
    else:
        timer=float(timer)
    print(timer)
    if(timer<=11 and timer>10):
        if(balance>=previousbalance):
                clear=driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[4]/div/div[2]/div/div[1]/button').click()
                value=driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/button').click()
                btn= driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[1]/button').click()

                accountbalance= driver.find_element(By.XPATH,'//*[@id="empire-header"]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span/div/span')
                convert=  accountbalance.text
                convert=convert.replace(',','.')
                balance = float(convert)
                if(accountbalance==previousbalance):
                    btn= driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[1]/button').click()

                previousbalance=balance
                time.sleep(4)
        elif(balance<previousbalance):
                x2=driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[4]/div/div[2]/div/div[8]/button').click()
                value=driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[4]/div/div[2]/div/div[2]/button').click()
                btn= driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[1]/button').click()

                accountbalance= driver.find_element(By.XPATH,'//*[@id="empire-header"]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span/div/span')
                convert=  accountbalance.text
                convert=convert.replace(',','.')
                balance = float(convert)
                if(accountbalance==previousbalance):
                    btn= driver.find_element(By.XPATH,'//*[@id="page-scroll"]/div[1]/div[2]/div/div[5]/div[1]/button').click()
                previousbalance=balance
                time.sleep(4)
    time.sleep(0.2)