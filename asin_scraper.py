import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os



def get_asin(asin):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(f"https://www.amazon.com/dp/{asin}")
    html_sauce = driver.page_source
    driver.close()
    soup = BeautifulSoup(html_sauce, 'html.parser')
    product_title = soup.find("span", {"id": "productTitle"}).contents[0].strip()
    total_stars = soup.find("span", {"class": "a-icon-alt"}).contents[0].strip()
    total_reviews = soup.find("span", {"id": "acrCustomerReviewText"}).contents[0].strip()
    price = soup.find("span", {"class": "a-offscreen"}).contents[0].strip()
    div = soup.find('img',{"alt":product_title})
    product_image = div.attrs['src']
    return [product_title,total_stars,total_reviews,price,product_image]