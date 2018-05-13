from selenium import webdriver
import time

username = 'fb_email@email.com'
password = 'fb_password'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/johnfisher/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()

