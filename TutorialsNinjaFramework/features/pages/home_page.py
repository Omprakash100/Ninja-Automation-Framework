from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage
from features.pages.search_page import SearchPage


class HomePage(BasePage):
    MY_ACCOUNT_OPTION = (By.XPATH, "//a[@title='My Account']")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    REGISTER_OPTION = (By.LINK_TEXT, "Register")
    SEARCH_BOX_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//div[@id='search']//button")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_my_account(self):
        self.click_on_element(self.MY_ACCOUNT_OPTION)

    def select_login_option(self):
        self.click_on_element(self.LOGIN_OPTION)
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element(self.REGISTER_OPTION)
        return RegisterPage(self.driver)

    def enter_product_into_search_box_field(self, product_text):
        self.set(self.SEARCH_BOX_FIELD, product_text)

    def click_on_search_button(self):
        self.click_on_element(self.SEARCH_BUTTON)
        return SearchPage(self.driver)

