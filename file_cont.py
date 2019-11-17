import os
import csv


def file_exist_check():
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
