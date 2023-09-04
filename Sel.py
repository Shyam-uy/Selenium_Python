from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.get("https://www.flipkart.com/")

driver.maximize_window()
searchBtn = driver.find_element(By.XPATH, "//input[@name='q']")
searchBtn.send_keys("Smartphone under 30000")
# driver.implicitly_wait(5.5)
select = Select(driver.find_element(By.XPATH, "//ul[@class='_1MRYA1']"))
driver.implicitly_wait(10)
select.select_by_index(3)

