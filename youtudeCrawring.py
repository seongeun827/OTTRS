from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from selenium import webdriver
import time

url = "https://www.youtube.com/feed/storefront?bp=kgEmCGQSIlBMSFBUeFR4dEMwaVpFSkE4TFdrSVVPOTJkVk9aMmVZOWKiBQIoBQ%3D%3D"
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(url)
elemsLinks = browser.find_elements_by_xpath('//*[@id="thumbnail"]')
# print(type(elemsLinks)) #타입은 list
elemsList = []
print("================")
for elemLink in elemsLinks:
    elemsList.append(elemLink.get_attribute("href"))

for elem in elemsList:

    browser.get(elem)
    try:
        title = browser.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        code = elem.split("=")[-1]
        plot = browser.find_element_by_xpath('//*[@id="description"]/yt-formatted-string').text
        modebtn = browser.find_element_by_xpath('//*[@id="button"]')
        modebtn.click()

        # mode = browser.find_elements_by_xpath('//*[@id="description"]')
        price = browser.find_element_by_xpath('//*[@id="text"]').text
        director = browser.find_element_by_xpath('//*[@id="content"]/yt-formatted-string/a').text
        genre = browser.find_element_by_xpath('//*[@id="content"]/yt-formatted-string[1]/a').text
        print("============================")
        print(title)
        print(code)
        print(plot)
        print("---------------------------")
    except:
        print("error")
