import requests
from pygame import mixer
import time
import random

mixer.init()
mixer.music.load("sound.mp3")

proxies = []
proxyfile = open('proxies.txt')
user = "sashaonln1@gmail.com"
password = "r3R!W3w2e+2APf"
port = "8080"
for line in proxyfile:
    proxies.append(user + ":" + password + "@" + line.strip("\n") + ":" + port)
proxyfile.close()

useragents = []
useragentfile = open('useragents.txt')
for line in useragentfile:
    useragents.append(line.strip("\n"))
useragentfile.close()

def runNewegg():
    neweggfile = open('newegg.txt') 
    for line in neweggfile:
        p1 = line[:line.index(" ")]
        p2 = line.replace("\n", "")[line.index(" ") + 1:]
        url = "https://www.newegg.com/p/" + p1
        session=requests.session()
        prox = random.choice(proxies)
        proxy = {"http": prox, "https": prox}
        header = {'User-Agent' : random.choice(useragents)}
        html = session.get(url, headers = header, proxies = proxy).text
        if (not "OUT OF STOCK" in html) and "FinalPrice" in html:
            priceind = html.index("FinalPrice")
            pricesubstring = html[priceind+12:priceind+20]
            pricecomma = 3 + pricesubstring[3:].index(",")
            price = pricesubstring[:pricecomma]
            if float(price) < float(p2):
                nameind = 15 + html.index("ProductTitle")
                namecomma = nameind + html[nameind:].index('"')
                name= html[nameind:namecomma]
                print("\n" + name + "\n$"+ price + "\n" + url)
                mixer.music.play()        
        time.sleep(.1)
    neweggfile.close()
        
            
            
def runBestBuy():
    bestbuyfile = open('bestbuy.txt')
    for line in bestbuyfile:
        url = "https://www.bestbuy.com/site/" + line.strip("\n") + ".p?skuId=" + line.strip("\n")
        session = requests.session()
        prox = random.choice(proxies)
        proxy = {"http": prox, "https": prox}
        header = {'User-Agent':random.choice(useragents)}
        html = session.get(url, headers = header).text
        print("hello")
        if "ADD_TO_CART" in html[html.find("buttonState") + 16 : html.find("buttonState") + 30]:
            priceind = html.index(',\"price\":')
            pricesubstring = html[priceind+10:priceind+20]
            pricecomma = 2 + pricesubstring[2:].index(",")
            price = pricesubstring[:pricecomma - 1]
            nameind = 8 + html.index("<title >")
            name = html[nameind:html.index(" - Best Buy</title>")]
            print("\n" + name + "\n$"+ price + "\n" + url)
            mixer.music.play()  
        time.sleep(.1)
        
    bestbuyfile.close()


            
    
    


def run():
    while True:
        runNewegg()
        runBestBuy()
run()