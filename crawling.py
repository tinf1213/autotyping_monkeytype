from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
options = Options()
s = Service("D:/ICSIE/web_crawling/chromedriver.exe")
driver = webdriver.Chrome(options=options)
url = "https://monkeytype.com/"
driver.get(url)
# time.sleep(1)
ac_btn = driver.find_element_by_css_selector("#cookiePopup > div.main > div.buttons > button.active.acceptAll")
ac_btn.click()
time.sleep(2)

while(True):
    str = driver.find_element_by_css_selector("#words > div.word.active").get_attribute('innerHTML').replace("<letter>", "").replace("</letter>", "")
    actions = ActionChains(driver)
    for ch in str:
        actions.send_keys(ch)
    actions.send_keys(Keys.SPACE)
    actions.perform()
