import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://leader-id.ru/")
    assert ("Leader-ID") in driver.title
    driver.find_element(By.CSS_SELECTOR, '.login-button').click() 
    driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.header > div.app-dialog.modal-login > div > div > div.el-dialog__body > div.app-dialog__body.is-footer > div > div > span > div:nth-child(2) > div > span > div > input').send_keys('ostrovlyan@gmail.com'+Keys.TAB+'2S68e6n8nihxfqP')
    #+Keys.ENTER)
    sleep(30)
    driver.get("https://leader-id.ru/events/create/step-1")
    assert('Создание мероприятия - Основное') in driver.title
    sleep(3)
    driver.close()

def test_firefox():
    driver=webdriver.Firefox()
    driver.get("https://leader-id.ru/")
    assert ("Leader-ID") in driver.title
    driver.find_element(By.CSS_SELECTOR, '.login-button').click()
    driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.header > div.app-dialog.modal-login > div > div > div.el-dialog__body > div.app-dialog__body.is-footer > div > div > span > div:nth-child(2) > div > span > div > input').send_keys('ostrovlyan@gmail.com'+Keys.TAB+'2S68e6n8nihxfqP')
    #+Keys.ENTER)
    sleep(30)
    driver.get("https://leader-id.ru/events/create/step-1")
    assert('Создание мероприятия - Основное') in driver.title
    sleep(3)
    driver.close()
