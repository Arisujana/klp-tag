from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#mendapatkan halaman utama
driver.get("https://ojs.uhnsugriwa.ac.id/index.php/nivedita/user/register")

time.sleep(10)
nama_depan= driver.find_element(By.XPATH, '//*[@id="givenName"]')
nama_depan.send_keys("ayu")

nama_belakang= driver.find_element(By.XPATH, '//*[@id="familyName"]')
nama_belakang.send_keys("ningsih")

afilisai= driver.find_element(By.XPATH, '//*[@id="affiliation"]')
afilisai.send_keys("uhnsugriwa")

negara= driver.find_element(By.XPATH, '//*[@id="country"]/option[text()="Indonesia"]').click()

email= driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("ayuning@gmail.com")

nama_pengguna= driver.find_element(By.XPATH, '//*[@id="username"]')
nama_pengguna.send_keys('ayuningsih')

sandi= driver.find_element(By.XPATH, '//*[@id="password"]')
sandi.send_keys('ayuning')

sandi2= driver.find_element(By.XPATH, '//*[@id="password2"]')
sandi2.send_keys('ayuning')

setuju= driver.find_element(By.XPATH, '//*[@id="register"]/fieldset[3]/div[1]/div/label/input').click()

setuju2= driver.find_element(By.XPATH, '//*[@id="register"]/fieldset[3]/div[2]/div/label/input').click()

daftar= driver.find_element(By.XPATH, '//*[@id="register"]/div/button').click()

time.sleep(15)
driver.quit