import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRequiredInputs(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def get_registration_result(self, link):
        self.browser.get(link)

        # fill the erquired fields
        first_required = self.browser.find_element_by_css_selector("input.first[required]")
        second_required = self.browser.find_element_by_css_selector("input.second[required]")
        third_required = self.browser.find_element_by_css_selector("input.third[required]")
        elements = [first_required, second_required, third_required]
        for element in elements:
            element.send_keys("some text")

        # submit the form
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # wait for the page to render new element
        welcome_text_elt = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        result = self.get_registration_result(link)
        self.assertEqual("Congratulations! You have successfully registered!", result, "Registration failed")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        result = self.get_registration_result(link)
        self.assertEqual("Congratulations! You have successfully registered!", result, "Registration failed")


if __name__ == "__main__":
    unittest.main()