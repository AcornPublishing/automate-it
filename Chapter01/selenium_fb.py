__author__ = 'Chetan'

from selenium import webdriver
browser = webdriver.Firefox()
print "WebDriver Object", browser
browser.maximize_window()
browser.get('https://facebook.com')

email = browser.find_element_by_name('email')
password = browser.find_element_by_name('pass')
print "Html elements:"
print "Email:", email, "\nPassword:", password

email.send_keys('abc@gmail.com') #Enter correct email address
password.send_keys('pass123') #Enter correct password

browser.find_element_by_id('loginbutton').click()
#browser.quit()
