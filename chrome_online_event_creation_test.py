import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

def test_chrome():
    driver=webdriver.Сhrome()
    driver.get("https://leader-id.ru/")
    Keys.DOWN
    assert ("Leader-ID") in driver.title
    driver.find_element(By.CSS_SELECTOR, '.login-button').click()
    driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.header > div.app-dialog.modal-login > div > div > div.el-dialog__body > div.app-dialog__body.is-footer > div > div > span > div:nth-child(2) > div > span > div > input').send_keys('ostrovlyan@gmail.com'+Keys.TAB+'2S68e6n8nihxfqP')   
    #+Keys.RETURN) пока капчу просит, ввожу вручную
    sleep(30)
    driver.get("https://leader-id.ru/events/create/step-1")
    driver.find_element(By.CSS_SELECTOR, 'div._3VsR5hvgUORl:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys('тестовое онлайн мероприятие')
    
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div[2]/div[1]/div/div/label/span').click()

    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div[2]/div[1]/div/div/label/div').click()
    
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span[1]/div/div[2]/div[1]/div/div/div[2]').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/span/div/div[1]/span/div').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/span/div/div[1]/span/div/input').send_keys('31102022'+Keys.TAB+'1430'+Keys.TAB+'1500')
    
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span[2]/div/div[2]/div/div/div[2]/div/span/div').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span[2]/div/div[2]/div/div/div[2]/div/span/div/input').send_keys('http://127.0.0.1'+Keys.RETURN)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/button').click()
    sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div[2]/button[3]').click()
    sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/button[2]').click()
    sleep(3)
    assert ('тестовое онлайн мероприятие') in driver.title

    driver.close


