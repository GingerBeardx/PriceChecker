# Python 3.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv, time

# Declare page links
page_amazon = r"https://www.amazon.com/Samsung-32-inch-Curved-Monitor-LC32F391FWNXZA/dp/B01D3BDXQA/ref=sr_1_3?keywords=monitor&qid=1573787251&refinements=p_89%3ASamsung&rnid=2528832011&sr=8-3"
page_newegg = r"https://www.newegg.com/p/0JC-0007-00K85?Description=Samsung%2032-inch%20Curved%20LED%20Monitor%20%28Ultra-%20Slim%20Design%29%20%28LC32F391FWNXZA%29&cm_re=Samsung_32-inch_Curved_LED_Monitor_%28Ultra-_Slim_Design%29_%28LC32F391FWNXZA%29-_-9SIAA7W91S8486-_-Product"

# Open the browser
driver = webdriver.Chrome()

# Get the name and price of the product from Aamzon
def get_amazon_price():
    driver.get(page_amazon)
    name_amazon = driver.find_element_by_id("productTitle").text
    price_amazon = float(
        driver.find_element_by_id("priceblock_ourprice").text.strip("$")
    )
    print(f"The current Amazon price for {name_amazon} is ${price_amazon}.")


def get_newegg_price():
    # Get the name and price of the product from NewEgg
    driver.get(page_newegg)
    # Since there is no ID on the price, get the price box by ID first and then find the price name within the box by class name
    price_box_newegg = driver.find_element_by_id("landingpage-price")
    price_newegg = float(
        price_box_newegg.find_element_by_class_name("price-current").text.strip("$")
    )
    name_newegg = driver.find_element_by_id("grpDescrip_h").text
    print(f"The current NewEgg price for {name_newegg} is ${price_newegg}.")


get_amazon_price()
get_newegg_price()

driver.close()
