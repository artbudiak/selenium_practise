import math
import time
import unittest
from numpy import append
from pip import main
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # this code executes after tests finish
    print("\nquit browser..")
    browser.quit()

urls = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

@pytest.mark.parametrize('url', urls)
class TestMainPage():  
    blankList = list()
    def test_answers(self, browser, url):
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)

        inputPath = browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea")
        inputValue = str(math.log(int(time.time())))
        inputPath.send_keys(inputValue)

        buttonPath = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(buttonPath)
        )
        buttonPath.click()

        answer = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        
        if answer.text != "Correct!":
            self.blankList.append(answer.text)
            print("".join(self.blankList))
        
        assert "Correct!" == answer.text