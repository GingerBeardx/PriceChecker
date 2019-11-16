def get_amazon_price(driver, page):
    """ Get the name and price of the product from Aamzon """
    driver.get(page)
    name_amazon = driver.find_element_by_id("productTitle").text
    price_amazon = float(
        driver.find_element_by_id("priceblock_ourprice").text.strip("$")
    )
    return f"The current Amazon price for {name_amazon} is ${price_amazon}."


def get_newegg_price(driver, page):
    """ Get the name and price of the product from NewEgg """
    driver.get(page)
    # Since there is no ID on the price, get the price box by ID first and then find the price name within the box by class name
    price_box_newegg = driver.find_element_by_id("landingpage-price")
    price_newegg = float(
        price_box_newegg.find_element_by_class_name("price-current").text.strip("$")
    )
    name_newegg = driver.find_element_by_id("grpDescrip_h").text
    return f"The current NewEgg price for {name_newegg} is ${price_newegg}."
