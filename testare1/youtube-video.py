# Youtube - search, open video, mute, change volume, change resolution, wider video screen, fullscreen
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

def hover(driver, element_css):
    element_to_hover_over = driver.find_element_by_css_selector(element_css)
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()

# Access youtube website
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com")

time.sleep(7)

# Accept cookies - on homepage
driver.switch_to.frame(driver.find_element_by_css_selector("#dialog iframe.ytd-consent-bump-lightbox"))
introAgreeButton = driver.find_element_by_xpath("/html/body//div[@id='introAgreeButton']")
introAgreeButton.click()
driver.switch_to.default_content()

time.sleep(2)

# Search "bella ciao"
searchBox = driver.find_element_by_css_selector("#search-input #search")
searchBox.send_keys("bella ciao")
searchBox.send_keys(Keys.RETURN)

time.sleep(2)

# Click first result - TODO: open in another tab
results = driver.find_elements_by_css_selector("#contents ytd-video-renderer #dismissable")
results[0].click()

time.sleep(2)

# Click "no thanks" button on signin popup - on video page - TODO: add if
noThanksButton = driver.find_element_by_css_selector("yt-upsell-dialog-renderer #dialog #button-container #dismiss-button")
noThanksButton.click()

time.sleep(2)

# Start video (so controls bar will appear)
videoContainer = driver.find_element_by_css_selector("#movie_player .ytp-cued-thumbnail-overlay")
videoContainer.click()
time.sleep(2)

# Change video settings
videoControlsBar_css = "#columns #primary #primary-inner #player #ytd-player .ytp-chrome-bottom .ytp-chrome-controls"
volumeArea_css = videoControlsBar_css + " .ytp-left-controls .ytp-volume-area"
rightBarButtons_css = videoControlsBar_css + " .ytp-right-controls button.ytp-button"

# mute volume
muteVolume_css = volumeArea_css + " .ytp-mute-button"
hover(driver,volumeArea_css)
muteVolume = driver.find_element_by_css_selector(muteVolume_css)
muteVolume.click()
time.sleep(3)

# change volume
volumeSlider_css = volumeArea_css + " .ytp-volume-panel.ytp-volume-control-hover .ytp-volume-slider .ytp-volume-slider-handle"
hover(driver,volumeArea_css)
volumeSlider = driver.find_element_by_css_selector(volumeSlider_css)
move = ActionChains(driver)
move.click_and_hold(volumeSlider).move_by_offset(10, 0).release().perform()
time.sleep(3)
move.click_and_hold(volumeSlider).move_by_offset(10, 0).release().perform()
time.sleep(3)
move.click_and_hold(volumeSlider).move_by_offset(10, 0).release().perform()
time.sleep(3)

time.sleep(2)

# change resolution
settingsButton_css = rightBarButtons_css + ".ytp-settings-button"
settingsButton = driver.find_element_by_css_selector(settingsButton_css)
settingsButton.click()
settingsMenu_css = "#columns #primary #primary-inner #player #ytd-player .ytp-popup.ytp-settings-menu"
settingsMenuItem_css = settingsMenu_css + " .ytp-panel .ytp-panel-menu .ytp-menuitem"
settingsMenuItems = driver.find_elements_by_css_selector(settingsMenuItem_css)
settingsMenuItems[3].click() #Quality button
time.sleep(1)
qualityOptions_css = settingsMenu_css + " .ytp-panel.ytp-quality-menu .ytp-panel-menu .ytp-menuitem .ytp-menuitem-label"
qualityOptions = driver.find_elements_by_css_selector(qualityOptions_css)
qualityOptions[0].click() #click on first option (highest quality)

time.sleep(2)

# video in fullscreen
fullscreenButton_css = rightBarButtons_css + ".ytp-fullscreen-button"
fullscreenButton = driver.find_element_by_css_selector(fullscreenButton_css)
fullscreenButton.click()
time.sleep(2)
fullscreenButton.click()
time.sleep(2)

# video in theater mode
theaterModeButton_css = rightBarButtons_css + ".ytp-size-button"
theaterModeButton = driver.find_element_by_css_selector(theaterModeButton_css)
theaterModeButton.click()
time.sleep(2)

driver.close() #close only current tab
time.sleep(2)
driver.quit() #close browser