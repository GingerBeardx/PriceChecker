# Python 3.7
from selenium import webdriver
from get_prices import get_amazon_price
from send_email import send_email
import os, csv


# Declare page links
page_amazon = r"https://www.amazon.com/Samsung-32-inch-Curved-Monitor-LC32F391FWNXZA/dp/B01D3BDXQA/ref=sr_1_3?keywords=monitor&qid=1573787251&refinements=p_89%3ASamsung&rnid=2528832011&sr=8-3"
page_newegg = r"https://www.newegg.com/p/0JC-0007-00K85?Description=Samsung%2032-inch%20Curved%20LED%20Monitor%20%28Ultra-%20Slim%20Design%29%20%28LC32F391FWNXZA%29&cm_re=Samsung_32-inch_Curved_LED_Monitor_%28Ultra-_Slim_Design%29_%28LC32F391FWNXZA%29-_-9SIAA7W91S8486-_-Product"

# Open the browser
# driver = webdriver.Chrome()

# print(get_amazon_price(driver, page_amazon))

# driver.close()


# Check to see if the products.csv file exists. If it does not, initiate it.
if os.path.isfile("./products.csv") == False:
    with open("products.csv", "w", newline="") as prod_file:
        headers = [
            "Date Added",
            "Product Name",
            "Aamzon URL",
            "NewEgg URL",
            "Date Last Checked",
            "High Price",
            "High Site",
            "Low Price",
            "Low Site",
            "Amazon Current Price",
            "NewEgg Current Price",
        ]
        file_writer = csv.writer(prod_file)
        file_writer.writerow(headers)
