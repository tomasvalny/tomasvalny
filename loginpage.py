from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.guru99.com/V4/index.php")

    def accept_cookies(self):
        #frame with cookies
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '#gdpr-consent-notice')))
        #reject button
        self.driver.find_element(By.CSS_SELECTOR, '#denyAll').click()

    def really_reject_cookies(self):
        #reject button in popup
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reject']"))).click()
        #swap to default frame
        self.driver.switch_to.default_content()
        #waiting due to potential timing error
        time.sleep(1)

    def login(self):
        #id
        id_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='uid']")
        id_input.send_keys("mngr541178")
        #pw
        pw_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        pw_input.send_keys("sYdygar")
        #login button
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='LOGIN']")
        submit_button.click()

    def close(self):
        time.sleep(3)
        self.driver.quit()