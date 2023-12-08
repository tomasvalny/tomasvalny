from selenium import webdriver
from loginpage import LoginPage
from newcustomer import NewCustomerPage
import time

new_customer_page = NewCustomerPage()
new_customer_page.opennewcustomer()
time.sleep(2)
customer_details = {
            'custname': "custname",
            'custpw': "custpw",
            'gender': "Female",
            'dob': "31121990",
            'custaddress': "custaddress",
            'custcity': "custcity",
            'custstate': "custstate",
            'custpin': "123",
            'custmobnum': "456987645",
            'custemail': "custemail",
            'pw':"hnup",

}

new_customer_page.input_customer_details(customer_details)
new_customer_page.submit_customer_form()
time.sleep(2)
new_customer_page.quit_browser()



