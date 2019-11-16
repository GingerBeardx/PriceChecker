# Python 3.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv, time

# Open the browser
driver = webdriver.Chrome()

# Open a browser window and navigate to a page
page = "https://www.amazon.com/Samsung-32-inch-Curved-Monitor-LC32F391FWNXZA/dp/B01D3BDXQA/ref=sr_1_3?keywords=monitor&qid=1573787251&refinements=p_89%3ASamsung&rnid=2528832011&sr=8-3"
driver.get(page)

# Get the name and price of the product from Aamzon
name = driver.find_element_by_id('productTitle').text
price = float(driver.find_element_by_id('priceblock_ourprice').text.strip('$'))
