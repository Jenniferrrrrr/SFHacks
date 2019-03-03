import requests,time
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def scraper(address):
    places = {}
    options = webdriver.ChromeOptions()
    options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    options.add_argument('window-size=800x841')
    options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    driver.get("https://www.domesticshelters.org")
    time.sleep(2)
    # textbox
    element = driver.find_element_by_xpath("//input[@class='search-input js-geocomplete home']")
    element.click()
    # type address
    element.send_keys(address + Keys.ENTER)
    time.sleep(4)
    html = driver.page_source
    soup = BeautifulSoup(html, 'xml')
    results = soup.find_all('li', attrs = {"class":"box1 d-pad-30"})[:3]
    for result in results: # find top 3 name and phone number
        found = result.find("h2")
        name = found.find('a').text
        phone = result.find('span', attrs = {"data-bind":"text: phone_number"}).text
        phone = phone.replace("-"," ")
        places[name] = phone
    return places
