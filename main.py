from zillow import ZillowData
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

GOOGLE_FORM = 'ENTER GOOGLE FORM LINK'
CHROME_DRIVER_PATH = "ENTER CHROME DRIVER PATH"


zillow = ZillowData()
price = zillow.get_price()
address = zillow.get_address()
links = zillow.get_links()


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
website = driver.get(GOOGLE_FORM)


time.sleep(3)
address_question = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
address_question.click()
time.sleep(1)
