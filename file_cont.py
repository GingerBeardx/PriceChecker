import os
import csv
import time


def add_product(
    product_name,
    amazon_url,
    newegg_url,
    high_price,
    high_site,
    low_price,
    low_site,
    amazon_price,
    newegg_price,
):
    with open("products.csv", "a", newline="") as products:
        writer = csv.writer(products)
        # Get current date
        cur_date = time.strftime("%Y/%m/%d")

        writer.writerow(
            [
                cur_date,
                product_name,
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


def display_products():
    """ Opens the products.csv file and iterates over each product """
    # Open the products file as a dictionary
    with open("products.csv", "r") as products:
        product_reader = csv.DictReader(products)
        # Loop through each item and display the relevant information
        for product in product_reader:
            print(
                product["Product Name"],
                product["Amazon Current Price"],
                product["NewEgg Current Price"],
                product["Low Price"],
                product["Low Site"],
            )


def file_exist_check():
    """ Determines if the products.csv file exists and creates it with headers if it does not """
    if not os.path.isfile("./products.csv"):
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
