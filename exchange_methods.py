from selenium import webdriver
from selenium.webdriver.common.by import By

def get_exchange():
    driver = webdriver.Chrome(r'C:\Users\Lenovo\Documents\chromedriver.exe')
    url = 'https://www.banki.ru/products/currency/cash/sankt-peterburg/'
    driver.maximize_window()
    driver.get(url)
    currency = driver.find_elements(By.XPATH,"//div[@class='table-flex__cell table-flex__cell--without-padding padding-left-default']")
    return currency[1].text, currency[2].text