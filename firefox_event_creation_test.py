import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

def test_firefox():
    driver=webdriver.Firefox()
    driver.get("https://leader-id.ru/")
    Keys.DOWN
    assert ("Leader-ID") in driver.title
    driver.find_element(By.CSS_SELECTOR, '.login-button').click()
    driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.header > div.app-dialog.modal-login > div > div > div.el-dialog__body > div.app-dialog__body.is-footer > div > div > span > div:nth-child(2) > div > span > div > input').send_keys('ostrovlyan@gmail.com'+Keys.TAB+'2S68e6n8nihxfqP')   
    #+Keys.RETURN) пока капчу просит, ввожу вручную
    sleep(30)
    driver.get("https://leader-id.ru/events/create/step-1")
    driver.find_element(By.CSS_SELECTOR, 'div._3VsR5hvgUORl:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys('тестовое мероприятие')
    driver.find_element(By.CSS_SELECTOR, 'label.app-radio:nth-child(2) > span:nth-child(2) > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'button.app-button:nth-child(3)').click()
    driver.find_element(By.NAME, 'file').send_keys('/home/ostrovlyan/python/selenium_leader_id/3x2.png')
    driver.find_element(By.CSS_SELECTOR,'button.app-button:nth-child(2)').click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content > div > div.wrapper > div > div._1oOXncqVzqmx._3IJlBydYjn7Z > div > div.aXiruEMFC6dH > button').click()
    sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span[1]/div/div[2]/div[3]/div/div[1]/div/span/div[2]/div').click()
    #TODO: другие города 
    driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div[1]/div/input').send_keys('Москва') 
    sleep (3)
    driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div[1]/div/input').send_keys(Keys.RETURN)
        
    sleep(3)
    Keys.RETURN
    
    sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span[1]/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/img').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/span/span/div/div[1]/label/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/span/div/input').click()
    driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/span/div[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/span/div').click()
    driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[1]/div[1]/div/div/div[2]/div[43]/div/div/span').click()
    driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/button').click()
    
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/span/div/input').send_keys('1430')
    Keys.RETURN
    
    sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/button').click()
    sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div[2]/button[3]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/button[2]').click()
    sleep(3)

    assert ('тестовое мероприятие') in driver.title
    driver.close()








