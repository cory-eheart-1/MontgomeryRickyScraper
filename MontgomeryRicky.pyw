#! c:\\Users\\corye\\AppData\\Local\\Programs\\Python\\Python38\\pythonw.exe

from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tinyWinToast.tinyWinToast import Toast, CROP_CIRCLE, CROP_NONE, getToast
from datetime import datetime, timedelta
import time

time.sleep(30)

url = 'https://store.rickymontgomery.com/products/683787-montgomery-ricky'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome('C:/Users\corye\Documents\MontgomeryRickyCheck\chromedriver.exe', chrome_options=options)
browser.get(url)

stock = browser.find_element_by_css_selector('.state')
appID = "Stock Check"
icon = "C:/Users\corye\Documents\MontgomeryRickyCheck\icom.jpg"
boolStock = False
timeCount = 0

while 1:
    if stock.text == 'Sold Out':
        toast = getToast("", "", icon, iconCrop=CROP_NONE, duration="short", appId=appID, isMute=True)
        toast.setTitle("Montgomery Ricky - Ricky Montgomery Stock", maxLines=2)
        toast.setMessage("Montgomery Ricky is out of stock", maxLines=2)
        boolStock = False
        timeCount += 1
    else:
        toast = getToast("", "", icon, iconCrop=CROP_NONE, duration="short", appId=appID, isMute=False)
        toast.setTitle("Montgomery Ricky - Ricky Montgomery Stock", maxLines=2)
        toast.setMessage("MONTGOMERY RICKY IS IN STOCK", maxLines=2)
        boolStock = True
    
    if boolStock == False:
        if timeCount == 1 or timeCount == 13:
            toast.show()
            if timeCount == 13:
                timeCount == 0
    else:
        toast.show()
    
    dt = datetime.now() + timedelta(hours=1)

    while datetime.now() < dt:
        time.sleep(1801)