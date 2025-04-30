from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#mendapatkan halaman utama
driver.get("https://app.hive.com/join")

time.sleep(10)


time.sleep(15)
driver.quit