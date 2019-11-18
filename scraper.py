# Python 3.7

# Native module imports
import csv
import time
import os

# Installed package imports
from selenium import webdriver

# Custom code imports
from file_cont import (
    add_product,
    display_products,
    file_exist_check,
)
from get_prices import (
    get_amazon_price,
    get_newegg_price,
    get_price_high_low,
    get_product_short_name,
)

# from send_email import send_email


# Check to see if the products.csv file exists. If it does not, initiate it.
file_exist_check()

# Initialize program and greet the user
while True:
    # Clear the terminal
    os.system("cls" if os.name == "nt" else "clear")
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
    print("-" * 80)

    if int(option_choice) == 1:  # Add a Product
        # Get the URLs for the item to be watched (This should be the actual product page)
        print("Please make sure you have the Amazon and NewEgg URLs to add:")
        amazon_url = input("What is the Amazon URL? > ")
        newegg_url = input("What is the NewEgg URL? > ")
        print("Getting price data, please wait...")
        print("-" * 80)
        # Add regex validation of the sites

        # Get Amazon and NewEgg info
        driver = webdriver.Chrome()
        amazon_name, amazon_price = get_amazon_price(driver, amazon_url)
        newegg_name, newegg_price = get_newegg_price(driver, newegg_url)
        driver.close()

        # Check to see which site has the current low price, the other will have the high price so set those variables accordingly
        high_price, high_site, low_price, low_site = get_price_high_low(
            amazon_price, newegg_price
        )

        # See which product name is shortest and set that as the product name for the CSV file
        product_name = get_product_short_name(amazon_name, newegg_name)

        # Add new item to products.csv
        add_product(
            product_name,
            amazon_url,
            newegg_url,
            high_price,
            high_site,
            low_price,
            low_site,
            amazon_price,
            newegg_price,
        )
        input("Enter anything to return to the menu > ")
    elif int(option_choice) == 2:  # Display Watched Products
        print("Fetcing products...")
        print("Product Name - Amazon Price - Newegg Price - Low Price - Low Site")
        print("-" * 80)
        display_products()
        input("Enter anything to return to the menu > ")
    elif int(option_choice) == 5:  # Close the program
        print("Goodbye!")
        break

