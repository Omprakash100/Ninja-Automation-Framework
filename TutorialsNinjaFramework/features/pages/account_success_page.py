from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class AccountSuccessPage(BasePage):
    ACCOUNT_CREATED_HEADING = (By.XPATH, "//div[@id='content']/h1")

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_account_created_heading(self, expected_heading):
        return self.retrieved_element_text_equals(self.ACCOUNT_CREATED_HEADING, expected_heading)
