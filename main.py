from threading import main_thread
import time
from plyer import notification 
import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import time

def notifyMe(title,message):
    notification.notify(
        title= title,
        message = message,
        app_icon= "C:\\Users\\Khushi\\Desktop\\covid\\icon.ico",
        timeout = 15

    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__== "__main__":
   # notifyMe("User","Lets stop the spread of Coronavirus") 
    myHtmlData = getData('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')

   
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())

    myDataStr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
     myDataStr += tr.get_text()
     myDataStr = myDataStr[0:]
    itemList=myDataStr.split("\n\n")
    country = ['North Korea', 'India', 'Germany','United Kingdom','Russia','Canada']
    
    for item in itemList[0:150]:
            dataList=item.split('\n')
            
            if dataList[0] in country:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f" Country: {dataList[0]}\nCases: {dataList[1]}\nDeaths: {dataList[2]}\nRegion: {dataList[3]}\n: "
                notifyMe(nTitle, nText)
                time.sleep(10)
          