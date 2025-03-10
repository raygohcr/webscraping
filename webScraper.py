from selenium import webdriver
import pprint
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://www.pressreader.com/newspapers'
    
    

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)



allow_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[text()='Allow all']")))

allow_button.click()
time.sleep(2)

current_height = browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')

while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
    new_height = browser.execute_script('return document.body.scrollHeight')

    soup = BeautifulSoup(browser.page_source, 'lxml')
    newspaper_container = soup.find('div', class_='ReactVirtualized__Grid__innerScrollContainer')
    if newspaper_container is None :
        continue
    item_list = newspaper_container.select('div[class*="ssi "]')
    for item in item_list:
        span_list = item.find_all('div', class_= 'page-source')
        print(span_list)
    
    if new_height == current_height:      # this means we have reached the end of the page!
        html = browser.page_source
        break
    prev_height = new_height