from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise

    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def verify_page_title(self,expected_title):
        return self.driver.title.__eq__(expected_title)

    def set(self, locator, value):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)

    def retrieved_element_text_contains(self, locator, expected_text):
        element = self.wait_for_element(locator)
        return element.text.__contains__(expected_text)

    def retrieved_element_text_equals(self, locator, expected_text):
        element = self.wait_for_element(locator)
        return element.text.__eq__(expected_text)

    def return_and_status(self,privacy_status,first_name_status,last_name_status,email_status,telephone_status,password_status):
        if privacy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
            return True
        else:
            return False

    def get_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def get_title(self):
        return self.driver.title
    def get_dropdown(self, locator):
        dropdown_element = self.wait_for_element(locator)
        dropdown = Select(dropdown_element)
        return dropdown

