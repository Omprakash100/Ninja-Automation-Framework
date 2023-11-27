from selenium.webdriver.common.by import By
from features.pages.account_success_page import AccountSuccessPage
from features.pages.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    TELEPHONE_FIELD = (By.ID, "input-telephone")
    PASSWORD_FIELD = (By.ID, "input-password")
    PASSWORD_CONFIRM_FIELD = (By.ID, "input-confirm")
    PRIVACY_POLICY_OPTION = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")
    YES_RADIO_OPTION = (By.XPATH, "//input[@name='newsletter'][@value='1']")
    DUPLICATE_EMAIL_WARNING = (By.XPATH, "//div[@id='account-register']/div[1]")
    PRIVACY_POLICY_WARNING = (By.XPATH, "//div[@id='account-register']/div[1]")
    FIRST_NAME_WARNING = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    LAST_NAME_WARNING = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    EMAIL_WARNING = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
    TELEPHONE_WARNING = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
    PASSWORD_WARNING = (By.XPATH, "//input[@id='input-password']/following-sibling::div")

    def enter_first_name(self, first_name_text):
        self.set(self.FIRST_NAME_FIELD, first_name_text)

    def enter_last_name(self, last_name_text):
        self.set(self.LAST_NAME_FIELD, last_name_text)

    def enter_email(self, email_text):
        self.set(self.EMAIL_FIELD, email_text)

    def enter_telephone(self, telephone_text):
        self.set(self.TELEPHONE_FIELD, telephone_text)

    def enter_password(self, password_text):
        self.set(self.PASSWORD_FIELD, password_text)

    def enter_password_confirm(self, password_confirm_text):
        self.set(self.PASSWORD_CONFIRM_FIELD, password_confirm_text)

    def select_privacy_policy(self):
        self.click_on_element(self.PRIVACY_POLICY_OPTION)

    def click_on_continue_button(self):
        self.click_on_element(self.CONTINUE_BUTTON)
        return AccountSuccessPage(self.driver)

    def select_yes_newsletter_option(self):
        self.click_on_element(self.YES_RADIO_OPTION)

    def display_status_of_duplicate_email_warning(self, expected_warning_text):
        return self.retrieved_element_text_contains(self.DUPLICATE_EMAIL_WARNING, expected_warning_text)

    def display_status_of_all_warning_messages(self, expected_privacy_warning, expected_first_name_warning, expected_last_name_warning, expected_email_warning, expected_telephone_warning, expected_password_warning):
        privacy_status = self.retrieved_element_text_contains(self.PRIVACY_POLICY_WARNING, expected_privacy_warning)
        first_name_status = self.retrieved_element_text_equals(self.FIRST_NAME_WARNING, expected_first_name_warning)
        last_name_status = self.retrieved_element_text_equals(self.LAST_NAME_WARNING, expected_last_name_warning)
        email_status = self.retrieved_element_text_equals(self.EMAIL_WARNING, expected_email_warning)
        telephone_status = self.retrieved_element_text_equals(self.TELEPHONE_WARNING, expected_telephone_warning)
        password_status = self.retrieved_element_text_equals(self.PASSWORD_WARNING, expected_password_warning)
        return self.return_and_status(privacy_status, first_name_status, last_name_status, email_status, telephone_status, password_status)
