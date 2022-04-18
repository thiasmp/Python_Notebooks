from multiprocessing.reduction import ACKNOWLEDGE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import bs4
import json




url = 'https://www.komplett.dk/category/21064/mobil/mobiltelefoner?nlevel=10444§21064&hits=240'
#This is for making a csv for all phones and prices on Komplett
def komplett():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
    
    # headless is needed here because we do not have a GUI version of firefox
    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
    browser = webdriver.Firefox(options=options)

    browser.get(url)
    browser.implicitly_wait(2)

    name = browser.find_elements_by_xpath('.//div[@class="text-content"]/h2')
    price = browser.find_elements_by_xpath('.//span[@class="product-price-now"]')
    
    product_names = [b.text for b in name]
    prices = [p.text for p in price]
    
    dct = {'Name': product_names, 'Price': prices}
    
    komplett_df = pd.DataFrame(dct)
    #print(komplett_df)
    komplett_df.to_csv("komplett.csv",index=False)   

    
def average_price():
    df = pd.read_csv('komplett.csv')
    
    
    mask_samsung = df.loc[df['Name'].str.contains('Samsung',case=True)]
    mask_iphone = df.loc[df['Name'].str.contains('iPhone',case=True)]
    
    to_numeric_samsung = (pd.to_numeric(mask_samsung['Price'].str.replace(r"[^\d]",""))) 
    to_numeric_iphone = (pd.to_numeric(mask_iphone['Price'].str.replace(r"[^\d]","")))
    
    all_samsung_phones = len(mask_samsung)
    all_iphones = len(mask_iphone)
    
    average_price_samsung = to_numeric_samsung.sum()/all_samsung_phones
    average_price_iphone = to_numeric_iphone.sum()/all_iphones
 
  
#komplett()
average_price()