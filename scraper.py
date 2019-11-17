# Python 3.7

# Python module imports
import csv
import time

# Installed package imports
from selenium import webdriver

# Custom code imports
from get_prices import get_amazon_price, get_newegg_price
from send_email import send_email
from file_cont import file_exist_check


# Check to see if the products.csv file exists. If it does not, initiate it.
file_exist_check()

# Initialize program and greet the user
# Create menu options and display for the user
print("Welcome to Price Checker")
print("-" * 80)
print("1) Add a new item")
print("2) View watched items")
print("3) Run Auto Watcher")
print("4) Email current info")
print("5) Close the program")
print("-" * 80)
option_choice = input("Please select one of the options above > ")


if int(option_choice) == 1:
    # Get the URLs for the item to be watched (This should be the actual product page)
    print("Please make sure you have the Amazon and NewEgg URLs to add:")
    amazon_url = input("What is the Amazon URL? > ")
    newegg_url = input("What is the NewEgg URL? > ")
    # Add regex validation of the sites

    # Get Amazon and NewEgg info
    driver = webdriver.Chrome()
    amazon_name, amazon_price = get_amazon_price(driver, amazon_url)
    newegg_name, newegg_price = get_newegg_price(driver, newegg_url)
    driver.close()

    # Check to see which site has the current low price, the other will have the high price so set those variables accordingly
    if amazon_price > newegg_price:
        high_price = amazon_price
        high_site = "Amazon"
        low_site = "NewEgg"
        low_price = newegg_price
    else:
        high_price = newegg_price
        high_site = "NewEgg"
        low_site = "Amazon"
        low_price = amazon_price

    # Add new item to products.csv
    with open("products.csv", "a", newline="") as products:
        writer = csv.writer(products)
        # Get current date
        cur_date = time.strftime("%Y/%m/%d")

        writer.writerow(
            [
                cur_date,
                amazon_name,
                amazon_url,
                newegg_url,
                cur_date,
                high_price,
                high_site,
                low_price,
                low_site,
                amazon_price,
                newegg_price,
            ]
        )
    print("File Updated with new product")
