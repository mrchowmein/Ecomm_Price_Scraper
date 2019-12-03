import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from datetime import datetime

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

driver = webdriver.Chrome("/Users/jasonchanmbp1/chromedriver")


def getAmzPrice(url):
    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")
    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="price_inside_buybox").get_text().split()[-1][1:].replace(",","")
    print("AMZ: ", title.strip(),": ", price)
    return price

def getBBPrice(url):
    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")
    title = soup2.find(class_= "heading-5 v-fw-regular").get_text()
    price = soup2.find(class_ = "priceView-hero-price priceView-customer-price").get_text().split()[-1].replace(",","")
    print( "BB: ", title.strip(),": ", price)
    return price

def getWalmartPrice(url):
    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.title.string
    price = float(soup.find(class_ ="price-group").get_text()[1:].replace(",",""))
    print( "Walmart: ", title.strip(),": ", price)
    return price

def getTargetPrice(url):
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser" )
    title = soup.title.string
    price = float(soup('div',attrs={'data-test':'product-price'})[1].string[1:])
    driver.quit()
    print( "Target: ", title.strip(),": ", price)
    return price




productPathAmz = "https://www.amazon.com/Samsung-Inch-Internal-MZ-76E1T0B-AM/dp/B078DPCY3T"
productPathBB = "https://www.bestbuy.com/site/samsung-860-evo-1tb-internal-sata-solid-state-drive/6178649.p?skuId=6178649"
productPathWal = "https://www.walmart.com/ip/Somerset-Home-Oven-Mitts-Set-of-2-Oversized-Quilted-Mittens-Flame-and-Heat-Resistant/542162962"
productPathTarget = "https://www.target.com/p/as-seen-on-tv-power-7qt-air-fryer/-/A-76544202"

while(True):
    dt_object = datetime.fromtimestamp(datetime.timestamp(datetime.now()))

    print("Current Date/Time:", dt_object)
    tarPrice = getTargetPrice(productPathTarget)
    amzPrice =getAmzPrice(productPathAmz)
    bbPrice = getBBPrice(productPathBB)
    newEggPrice = getWalmartPrice(productPathWal)

    time.sleep(3600)
