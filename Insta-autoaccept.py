#!/usr/bin/env python
# coding: utf-8

# In[15]:


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(ChromeDriverManager().install()) # Optional argument, if not specified will search path.
driver.get('https://www.instagram.com/');
time.sleep(5)
username = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
username.send_keys("enter your username here")
time.sleep(5)

password = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys("enter your password here")
time.sleep(5)
login = driver.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[3]/button")
login.click()
time.sleep(5)
if driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button"):
    not_now = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
    not_now.click()
time.sleep(5)

if driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]"):
    not_now = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    not_now.click() 
while True:
    time.sleep(5)

    if driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[4]/a"):
        heart = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[4]/a")
        heart.click() 
    time.sleep(5)
    try:
        if driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]"):
            show = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]")
            show.click()   
    except NoSuchElementException:
        home = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a")
        home.click() 
    time.sleep(5)
    try:
        if driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[1]/button"):
            confirm = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[1]/button")
            confirm.click()   
    except NoSuchElementException:  #spelling error making this code not work as expected
        home = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a")
        home.click() 
    time.sleep(5)
    driver.refresh()
        
time.sleep(50) 
driver.quit() 


# In[ ]:




