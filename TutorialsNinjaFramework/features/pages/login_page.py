from selenium.webdriver.common.by import By
from features.pages.account_page import AccountPage
from features.pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='login-email']")
    EMAIL_ADDRESS_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_MESSAGE = (By.XPATH, "//div[@id='account-login']/div[1]")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_email_address(self,email_text):
        self.set(self.EMAIL_ADDRESS_FIELD, email_text)

    def enter_password(self,password_text):
        self.set(self.PASSWORD_FIELD, password_text)

    def click_on_login_button(self):
        self.click_on_element(self.LOGIN_BUTTON)
        return AccountPage(self.driver)

    def display_status_of_warning_message(self,expected_warning_text):
        return self.retrieved_element_text_contains(self.WARNING_MESSAGE, expected_warning_text)





