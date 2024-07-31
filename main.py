from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import csv


# for BeautifulSoup scraping
url = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
            "Accept-Language": "en-US,en;q=0.9,he;q=0.8,el;q=0.7,la;q=0.6",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Priority": "u=1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1"
            }

# For selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class HouseData:
    def __init__(self, url, headers):
        response = requests.get(url=url, headers=headers)
        site = response.text
        soup = BeautifulSoup(site, "html.parser")
        self.property_cards = soup.find_all(class_="StyledPropertyCardDataWrapper")

    def write_links(self):
        links = []
        for property_card in self.property_cards:
            a_tag = property_card.find('a')
            link = a_tag.get("href")
            links.append(link)
        return links

    def write_costs(self):
        prices = []
        for property_card in self.property_cards:
            price_element = property_card.find(class_="PropertyCardWrapper__StyledPriceLine")
            raw_price = price_element.text.strip()
            cleaned_price = self.clean_price(raw_price)
            prices.append(cleaned_price)
        return prices

    def clean_price(self, price):
        parts = price.split('/')
        cleaned_price = parts[0].split('+')[0]
        return cleaned_price

    def write_addresses(self):
        addresses = []
        for property_card in self.property_cards:
            address_element = property_card.find('address')
            address = address_element.text.strip()
            addresses.append(address)
        return addresses

    def write_to_google_form(self, links, prices, addresses):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfH8mz2tul3bTYcub5vMOtnhrYLOeVeGgi3YVgf498YwXURKQ/viewform?usp=sf_link")
        time.sleep(2)
        for i in range(len(links)):
            input_fields = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")
            input_fields[0].send_keys(addresses[i])
            input_fields[1].send_keys(prices[i])
            input_fields[2].send_keys(links[i])
            # submit button
            submit_button = driver.find_element(By.CSS_SELECTOR, ".lRwqcd .uArJ5e")
            submit_button.click()
            # submit another response
            new_response_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            new_response_link.click()
        driver.quit()

    def write_to_csv(self):
        assert len(addresses) == len(links) == len(prices), "Lists must have the same length"

        with open("output.csv", "w", newline='') as file:
            writer = csv.writer(file)
            # write header
            writer.writerow(["addresses", "links", "cost per month"])
            for address, link, price in zip(addresses, links, prices):
                writer.writerow([address, link, price])


data = HouseData(url, headers)
links = data.write_links()
prices = data.write_costs()
addresses = data.write_addresses()
data.write_to_google_form(links, prices, addresses)
data.write_to_csv()
