# Instagram msg bot
# @Owner - Yuvraj


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time



PATH = "C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=PATH)

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.instagram.com")

user = ""
password = ""

person = ''

driver.implicitly_wait(10)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

user_input = driver.find_element(By.NAME, "username")
user_input.send_keys(user)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

pass_input = driver.find_element(By.NAME, "password")
pass_input.send_keys(password)



login_xpath = "//button[contains(@class, '_acan') and div[text()='Log in']]"
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, login_xpath))
)

login_button = driver.find_element(By.XPATH, login_xpath)
login_button.click()


not_now_xpath = "//div[contains(@class, 'x1i10hfl') and text()='Not now']"
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, not_now_xpath))
)

not_now_button = driver.find_element(By.XPATH, not_now_xpath)
not_now_button.click()


msg_sec_xpath = "//a[contains(@aria-label, 'Direct messaging')]"
WebDriverWait(driver, 25).until(
    EC.element_to_be_clickable((By.XPATH, msg_sec_xpath))
)

msg_sec = driver.find_element(By.XPATH, msg_sec_xpath)
msg_sec.click()


#WebDriverWait(driver, 20).until(
#    EC.element_to_be_clickable((By.XPATH, "//button[text()='Turn On']"))
#)

#turn_on_button = driver.find_element(By.XPATH, "//button[text()='Turn On']")
#turn_on_button.click()

driver.implicitly_wait(10)
WebDriverWait(driver, 25).until(
    EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{person}')]"))
)
select_msg_button = driver.find_element(By.XPATH, f"//span[contains(text(), '{person}')]")
select_msg_button.click()


WebDriverWait(driver, 25).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-placeholder='Message...']"))
)

message = driver.find_element(By.XPATH, "//div[@aria-placeholder='Message...']")
message.click()

for i in range(10):
    message.send_keys("meow" + str(i) + Keys.ENTER)



#WebDriverWait(driver, 25).until(
#    EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Close']"))
#)

#close_button = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Close']")
#close_button.click()


time.sleep(25)


driver.quit()
