from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import pprint
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pycountry
import time

def get_countries():
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = str.lower(country.alpha_2)
    countries["International"] = "_i"
    countries["Bolivia"] = "bo"
    countries["Brunei"] = "bn"
    countries["Congo, Democratic Republic of the"] = "cd"
    countries["Congo, Republic of the"] = "cg"
    countries["Iran"] = "ir"
    countries["Korea, Democratic People's Republic"] = "kp"
    countries["Korea, Republic"] = "kr"
    countries["Laos"] = "la"
    countries["Macau"] = "mo"
    countries["Micronesia"] = "fm"
    countries["Palestine"] = "ps"
    countries["Russia"] = "ru"
    countries["Syria"] = "sy"
    countries["Taiwan"] = "tw"
    countries["Tanzania"] = "tz"
    countries["Venezuela"] = "ve"
    countries["Vietnam"] = "vn"
    countries["Vatican City"] = "va"
    return countries


url = 'https://www.pressreader.com/catalog'
    
    

browser = webdriver.Chrome()
browser.get(url)
time.sleep(1)


allow_button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[text()='Allow all']")))

allow_button.click()


element = WebDriverWait(browser,60).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='All countries/regions']")))
element.click()

checkbox = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='title' and text()='All countries/regions']")))
checkbox.click()

soup = BeautifulSoup(browser.page_source, 'lxml')

countries = get_countries()

div = soup.find('ul', class_="navfilter-list")

countries_list = div.select('li[class*="is-available"]')




for country in countries_list:
    country_name = country.find('div',class_="title").get_text()
    code = countries.get(country_name,"")
    redirect_url = url + "?country={}".format(code)
    browser.get(url)
    time.sleep(5)




# while True:
#     current_height = browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#     time.sleep(2)
#     new_height = browser.execute_script('return document.body.scrollHeight')

#     soup = BeautifulSoup(browser.page_source, 'lxml')
#     newspaper_container = soup.find('div', class_='ReactVirtualized__Grid__innerScrollContainer')
#     if newspaper_container is None :
#         continue
#     item_list = newspaper_container.select('div[class*="ssi "]')
#     for item in item_list:
#         span_item = item.find('div', class_= 'page-source').get_text()
#         print(span_item)
    
#     if new_height == current_height:      # this means we have reached the end of the page!
#         html = browser.page_source
#         break
#     prev_height = new_height