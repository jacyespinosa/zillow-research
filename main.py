from zillow import ZillowData
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

GOOGLE_FORM = 'ENTER GOOGLE FORM LINK'
CHROME_DRIVER_PATH = "ENTER CHROME DRIVER PATH"


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
website = driver.get(GOOGLE_FORM)
