# Test - Create a yahoo mail account - filling in data (it does not fully create an account, since yahoo has bot security)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def setName(driver):
    firstNameBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-firstName']")
    firstNameBox.send_keys("William")
    time.sleep(0.2)
    lastNameBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-lastName']")
    lastNameBox.send_keys("Smith")

def setBirth(driver):
    monthBox = driver.find_element_by_xpath("//html[@id='Stencil']//select[@id='usernamereg-month']/option[@value='7']")
    monthBox.click()  # click on July option
    time.sleep(0.2)
    dayBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-day']")
    dayBox.send_keys("23")
    time.sleep(0.2)
    yearBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-year']")
    yearBox.send_keys("1997")

def setAccDetails(driver):
    setName(driver)
    time.sleep(0.2)
    emailBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-yid']")
    emailBox.send_keys("willc.smith123")
    time.sleep(0.2)
    passBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-password']")
    passBox.send_keys("WcS12345")
    time.sleep(0.2)
    phoneBox = driver.find_element_by_xpath("//html[@id='Stencil']//input[@id='usernamereg-phone']")
    phoneBox.send_keys("0701000100")
    time.sleep(0.2)
    setBirth(driver)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://mail.yahoo.com")

time.sleep(2)

#Create a new account
accountButton = driver.find_element_by_xpath("//form[@id='login-username-form']//p[@class='row sign-up-link']")
accountButton.click()

#time.sleep(1)

#Fill account details boxes
setAccDetails(driver)
#time.sleep(1)

#Submit account
continueButton = driver.find_element_by_xpath("//html[@id='Stencil']//button[@id='reg-submit-button']")
continueButton.click()

#time.sleep(1)

#Recaptcha
# checkBox = driver.find_element_by_xpath("//span[@id='recaptcha-anchor']/div[2]")
# checkBox.click()
#//span[@id='recaptcha-anchor']/div[1]
#//span[@id='recaptcha-anchor']/div[2]
#/html//span[@id='recaptcha-anchor']
#/html//div[@id='rc-anchor-container']//div[@class='rc-anchor-center-item rc-anchor-checkbox-holder']
#//span[@id='recaptcha-anchor']/div[3]
#//span[@id='recaptcha-anchor']/div[4]

time.sleep(2)

driver.quit()
