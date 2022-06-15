from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstField = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    secondField = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    thirdField = browser.find_element(By.CSS_SELECTOR, "input.third[required]")

    fields = [firstField, secondField, thirdField]
    for field in fields:
       field.send_keys("some text")
       time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Test passed")

finally:
    time.sleep(1)
    browser.quit()