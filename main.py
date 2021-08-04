import requests
import lxml as lxml
from bs4 import BeautifulSoup

ZILLOW_URL = 'https://www.zillow.com/san-jose-ca/rentals/2-2_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.11190420019531%2C%22east%22%3A-121.63811879980469%2C%22south%22%3A37.136968211576836%2C%22north%22%3A37.48049223172488%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A2%2C%22max%22%3A2%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'


class ZillowData:
    def __init__(self):
        self.response = requests.get(ZILLOW_URL, headers={"Accept-Language": "en-US,en;q=0.9",
                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"})

        self.response.raise_for_status()
        self.webpage = self.response.text
        self.soup = BeautifulSoup(self.webpage, "lxml")