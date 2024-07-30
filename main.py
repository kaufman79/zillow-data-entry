import requests
from bs4 import BeautifulSoup
import time

url = "https://www.zillow.com/charlotte-nc/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A35.51573940185062%2C%22south%22%3A34.79265920419744%2C%22east%22%3A-80.37336194628905%2C%22west%22%3A-81.3209327470703%7D%2C%22usersSearchTerm%22%3A%22Charlotte%2C%20NC%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A24043%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A12614%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A47121%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%2C%22min%22%3A1700%7D%2C%22price%22%3A%7B%22max%22%3A400977%2C%22min%22%3A340830%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22sche%22%3A%7B%22value%22%3Afalse%7D%2C%22schm%22%3A%7B%22value%22%3Afalse%7D%2C%22schh%22%3A%7B%22value%22%3Afalse%7D%2C%22schp%22%3A%7B%22value%22%3Afalse%7D%2C%22schr%22%3A%7B%22value%22%3Afalse%7D%2C%22schc%22%3A%7B%22value%22%3Afalse%7D%2C%22schu%22%3A%7B%22value%22%3Afalse%7D%2C%22sqft%22%3A%7B%22min%22%3A1750%7D%7D%2C%22isListVisible%22%3Atrue%7D"
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


class HouseData:
    def __init__(self, url, headers):
        response = requests.get(url=url, headers=headers)
        site = response.text
        soup = BeautifulSoup(site, "html.parser")
        self.property_cards = soup.find_all(class_="property-card-data")

    def write_links(self):
        links = []
        for property_card in self.property_cards:
            a_tag = property_card.find('a')
            link = a_tag.get("href")
            links.append(link)
        print(links)

    def write_costs(self):
        pass

    def write_addresses(self):
        pass

    def write_to_google_form(self):
        pass

    def write_to_csv(self):
        pass


data = HouseData(url, headers)
data.write_links()
data.write_costs()
data.write_addresses()
data.write_to_google_form()
data.write_to_google_form()


