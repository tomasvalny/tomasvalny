from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loginpage import LoginPage

import time

class NewCustomerPage:
    def __init__(self):
        self.login_page = LoginPage()
        self.driver = self.login_page.driver
        self.login_page.accept_cookies()
        self.login_page.really_reject_cookies()
        self.login_page.login()

    def opennewcustomer(self):
        #open new customer
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='addcustomerpage.php']"))).click()

    def handle_calendar_picker(self, date):
        # Click on the input field or button to open the calendar
        date_input = self.driver.find_element(By.CSS_SELECTOR, self.locators['dob'])
        date_input.clear()  # Clear any existing value
        date_input.send_keys(date)
    def input_customer_details(self, details):
        # Input customer details
        for key, value in details.items():
            if key == 'dob':
                self.handle_calendar_picker(value)
            elif key == 'gender':
            # Handle the radio buttons
                self.handle_radio_buttons(value)
            else:
                self.driver.find_element(By.CSS_SELECTOR, self.locators[key]).send_keys(value)

    def handle_radio_buttons(self, gender):
        # Handle the radio buttons for gender
        if gender.lower() == 'male':
            self.driver.find_element(By.XPATH, self.locators['male_radio']).click()
        elif gender.lower() == 'female':
            self.driver.find_element(By.XPATH, self.locators['female_radio']).click()
    def submit_customer_form(self):
        # Submit customer form
        self.driver.find_element(By.CSS_SELECTOR,"input[value='Submit']").click()
        # Locators
    locators = {
            'custname': "input[name='name']",
            'custaddress': "textarea[name='addr']",
            'custcity': "input[name='city']",
            'custstate': "input[name='state']",
            'custpin': "input[name='pinno']",
            'custmobnum': "input[name='telephoneno']",
            'custemail': "input[name='emailid']",
            'custpw': "input[name='password']",
            'male_radio': "//input[@value='m']",
            'female_radio': "//input[@value='f']",
            'dob': "#dob",
            'pw': "input[name='password']",
        }

    def quit_browser(self):
        # Close the browser
        self.driver.quit()