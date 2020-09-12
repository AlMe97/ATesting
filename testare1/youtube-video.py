# Youtube - login into my account, search sth, open video, up volume, change resolution, wider video screen, fullscreen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Access youtube website
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com")

time.sleep(7)

# Login into already created account - TODO

# 2 ifs here - 1)cookies popup + 2)signin popup (if appears) - TODO
# don't continue unless they appear or
# 1) on homepage
# 2) on video page

# Accept cookies
# introAgreeButton = driver.find_element_by_id("introAgreeButton")
# introAgreeButton.click()

# <form action="https://consent.youtube.com/set?pc=yt&amp;uxe=23934716" method="post"
# class="A28uDc" jsaction="JIbuQc:tQDWEc">
#      <div role="button" id="introAgreeButton"

# Click "no thanks" button on signin popup - TODO
noThanksButton = driver.find_element_by_css_selector("yt-upsell-dialog-renderer #dialog #button-container #dismiss-button")
noThanksButton.click()

time.sleep(7)

# Search "bella ciao"
searchBox = driver.find_element_by_css_selector("#search-input #search")
searchBox.send_keys("bella ciao")
searchBox.send_keys(Keys.RETURN)

time.sleep(2)

# Click first result - TODO: open in another tab
results = driver.find_elements_by_css_selector("#contents ytd-video-renderer #dismissable")
results[0].click()

time.sleep(2)

# Change video settings
videoControlsBar_css = "#columns #primary #primary-inner #player #ytd-player .ytp-chrome-bottom .ytp-chrome-controls"
rightBarButtons_css = videoControlsBar_css + " .ytp-right-controls button.ytp-button"

# increase volume - TODO
time.sleep(2)

# change resolution - TODO: verify if working
settingsButton_css = rightBarButtons_css + ".ytp-settings-button"
settingsButton = driver.find_element_by_css_selector(settingsButton_css)
settingsButton.click()
settingsMenu_css = "#columns #primary #primary-inner #player #ytd-player .ytp-popup.ytp-settings-menu"
settingsMenuItem_css = settingsMenu_css + " .ytp-panel .ytp-panel-menu .ytp-menuitem"
settingsMenuItems = driver.find_elements_by_css_selector(settingsMenuItem_css)
settingsMenuItems[4].click() #Quality button
qualityOptions_css = settingsMenu_css + " .ytp-panel.ytp-quality-menu .ytp-panel-menu .ytp-menuitem"
qualityOptions = driver.find_elements_by_css_selector(qualityOptions_css)
qualityOption[0].click() #click on first option (highest quality)

time.sleep(2)

# video in theater mode - TODO: verify if working
theaterModeButton_css = rightBarButtons_css + ".ytp-size-button"
theaterModeButton = driver.find_element_by_css_selector(theaterModeButton_css)
theaterModeButton.click()
time.sleep(2)

# video in fullscreen - TODO: verify if working
fullscreenButton_css = rightBarButtons_css + ".ytp-fullscreen-button"
fullscreenButton = driver.find_element_by_css_selector(fullscreenButton_css)
fullscreenButton.click()
time.sleep(2)

driver.close() #close only current tab
time.sleep(2)
driver.quit() #close browser