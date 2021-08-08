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


over = False
while not over:
    for i in range(len(address)):
        address_question = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_question.click()
        time.sleep(1)
        address_question.send_keys(f'{address[i]}')

        price_question = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_question.click()
        time.sleep(1)
        price_question.send_keys(f'{price[i]}')