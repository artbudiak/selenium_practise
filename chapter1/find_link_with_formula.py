import math 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    link_element = browser.find_element_by_link_text(link_text)
    link_element.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Artem")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Semenovich")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Kharkiv")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(6)
    browser.quit()

