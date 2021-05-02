from urllib.request import urlopen
from pygame import mixer
import time
 

def run():
    mixer.init()
    mixer.music.load("sound.mp3")
    while True:
        neweggfile = open('newegg.txt') 
        for line in neweggfile:
            p1 = line[:line.index(" ")]
            p2 = line[line.index(" "):]
            url = "https://www.newegg.com/p/" + p1
            
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            print(html)
            if not "OUT OF STOCK" in html and "FinalPrice" in html:
                priceind = html.index("FinalPrice")
                poop = html[priceind+12:priceind+20]
                pricecomma = 3 + poop[3:].index(",")
                price = poop[:pricecomma]
                if price < p2:
                    nameind = 15 + html.index("ProductTitle")
                    namecomma = nameind + html[nameind:].index('"')
                    name= html[nameind:namecomma]
                    print("")
                    print(name + " ")
                    print(price)
                    print(url)
                    mixer.music.play()
                    print("hello rice im right here!!!!")
                    
            time.sleep(100)
                
                
                

        neweggfile.close()
        
            
            
            
            
    
    


run()
