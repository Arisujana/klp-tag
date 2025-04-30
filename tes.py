from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://app.hive.com/join")

# Tunggu tombol "Continue with email" muncul, lalu klik
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mounter-react-root"]/div/div/div/div/div[2]/div/div/div/button'))
).click()

# Tunggu field email muncul
work_email = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'email'))
)
work_email.send_keys('gunggayatri12@gmail.com')

# Klik sembarang area untuk lanjut (sebenarnya lebih baik cari tombol submit jika ada)
driver.find_element(By.ID, 'mounter-react-root').click()

# Tunggu sampai field nama muncul
first_name = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'firstName'))
)
first_name.send_keys('deyrenathaniel')

# Tunggu 30 detik biar bisa lihat hasil
import time
time.sleep(30)

driver.quit()
