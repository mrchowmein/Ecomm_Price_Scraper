import requests
from bs4 import BeautifulSoup
import time
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}



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


productPathAmz = "https://www.amazon.com/Samsung-Inch-Internal-MZ-76E1T0B-AM/dp/B078DPCY3T"
productPathBB = "https://www.bestbuy.com/site/samsung-860-evo-1tb-internal-sata-solid-state-drive/6178649.p?skuId=6178649"
productPathWal = "https://www.walmart.com/ip/Holiday-Time-Pre-Lit-12-Williams-Pine-Artificial-Christmas-Tree-Clear-Lights/733042803"

while(True):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current Time:", current_time)
    amzPrice =getAmzPrice(productPathAmz)
    bbPrice = getBBPrice(productPathBB)
    newEggPrice = getWalmartPrice(productPathWal)

    time.sleep(3600)
