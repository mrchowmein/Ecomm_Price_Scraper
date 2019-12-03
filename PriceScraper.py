import requests
from bs4 import BeautifulSoup
import time
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}



def getAmzPrice(url):
    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")
    title = soup2.find(id="productTitle").get_text()
    price = float(soup2.find(id="priceblock_ourprice").get_text()[1:])

    print("AMZ: ", title.strip(),": ", price)

def getBBPrice(url):
    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")
    title = soup2.find("h1", attrs={"class": "heading-5 v-fw-regular"}).get_text()
    price = soup2.find("div", attrs={"class": "priceView-hero-price priceView-customer-price"}).get_text().split()[-1].replace(",","")
    print( "BB: ", title.strip(),": ", price)

productPathAmz = "https://www.amazon.com/Samsung-Inch-Internal-MZ-76E1T0B-AM/dp/B078DPCY3T"
productPathBB = "https://www.bestbuy.com/site/samsung-860-evo-1tb-internal-sata-solid-state-drive/6178649.p?skuId=6178649"
productPathBB2 = "https://www.bestbuy.com/site/sony-wh-1000xm3-wireless-noise-canceling-over-the-ear-headphones-with-google-assistant-black/6280544.p?skuId=6280544"

while(True):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current Time:", current_time)
    getAmzPrice(productPathAmz)
    getBBPrice(productPathBB)

    time.sleep(3600)
