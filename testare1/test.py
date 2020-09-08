# This code opens the google.ro webpage, types "World of Warcraft" in the search bar, then searches it on google.
# Then, it clicks on the first result, so it opens the World of Warcraft main page. - 2 methods coded for this

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.ro")
#print(driver.title) #prints out title of current webpage

time.sleep(2)

searchBox = driver.find_element_by_css_selector("#tsf input.gLFyf.gsfi")
searchBox.send_keys("world of warcraft")
searchBox.send_keys(Keys.RETURN)

time.sleep(2)

# Method 1
# results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  #finds webresults
# results[0].click() #clicks the first one

# Method 2
firstSite = driver.find_element_by_css_selector("#rso .g:nth-of-type(1) .rc div.r a h3")
firstSite.click()

time.sleep(2)

#driver.close() #close current tab
driver.quit() #close entire browser
