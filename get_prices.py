def get_amazon_price(driver, page):
    """ Get the name and price of the product from Aamzon """
    driver.get(page)
    name_amazon = driver.find_element_by_id("productTitle").text
    price_amazon = float(
        driver.find_element_by_id("priceblock_ourprice").text.strip("$")
    )
    return name_amazon, price_amazon


def get_newegg_price(driver, page):
    """ Get the name and price of the product from NewEgg """
    driver.get(page)
    # Since there is no ID on the price, get the price box by ID first and then find the price name within the box by class name
    price_box_newegg = driver.find_element_by_id("landingpage-price")
    price_newegg = float(
        price_box_newegg.find_element_by_class_name("price-current").text.strip("$")
    )
    name_newegg = driver.find_element_by_id("grpDescrip_h").text
    return name_newegg, price_newegg


def get_price_high_low(amazon_price, newegg_price):
    """ Determine which site has the high price and low price """
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
    return high_price, high_site, low_price, low_site


def get_product_short_name(amazon_name, newegg_name):
    """ Determines which product name is shortest for inclusion in the csf file """
    if len(amazon_name) > len(newegg_name):
        product_name = newegg_name
    else:
        product_name = amazon_name
    return product_name
