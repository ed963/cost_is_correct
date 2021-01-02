from selenium import webdriver
from typing import Tuple, List
from random import choice, randint
from selenium.common.exceptions import NoSuchElementException
from currency_converter import string_to_cents


def get_product_info(n: int) -> List[Tuple[str, str, int]]:
    products = []
    driver = webdriver.Chrome('chromedriver.exe')
    i = 0
    try:
        while i < n:
            try:
                driver.get('https://www.amazon.ca/gp/bestsellers')

                # Navigate to a random department
                choice(driver.find_elements_by_xpath("//ul[@id='zg_browseRoot']/ul/li/a[text()!='Gift Cards' and text()!='Audible Books & Originals']")).click()

                # Pick a random product out of first 10 products
                prod_num = randint(1, 10)

                prod = driver.find_element_by_xpath(f"//ol[@id='zg-ordered-list']/li[{prod_num}]//img")
                name = prod.get_attribute('alt')
                img_path = prod.get_attribute('src')
                raw_price = driver.find_element_by_xpath(f"//ol[@id='zg-ordered-list']/li[{prod_num}]//span[@class='p13n-sc-price']").text
                price = string_to_cents(raw_price.split('$')[1])

                products.append((name, img_path, price))
                i += 1
            except NoSuchElementException:
                pass
    finally:
        driver.quit()

    return products


if __name__ == '__main__':
    print(get_product_info(1))
