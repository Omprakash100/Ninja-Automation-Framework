from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class SearchPage(BasePage):
    PRODUCTS = (By.XPATH, "//div[@id='content']//div[@class='caption']//a")
    MESSAGE = (By.XPATH, "//input[@id='button-search']/following-sibling::p")
    PRODUCTS_PRICE = (By.XPATH, "//div[@id='content']//div[@class='caption']//p[@class ='price']")
    SORT_DROPDOWN = (By.ID, "input-sort")

    def __init__(self, driver):
        super().__init__(driver)

    def results_contain_product(self, product):
        all_products = self.get_elements(self.PRODUCTS)
        products_contain_product = [product.lower() in product_element.text.lower() for product_element in all_products]
        return all(products_contain_product)

    def display_status_of_message(self, expected_message_text):
        return self.retrieved_element_text_equals(self.MESSAGE, expected_message_text)

    def sort_by(self, sort_type):
        dropdown = self.get_dropdown(self.SORT_DROPDOWN)
        dropdown.select_by_visible_text(sort_type)

    def sort_by_order(self, sort_type):
        if sort_type == "ascending":
            return self.sort_by("Price (Low > High)")
        else:
            return self.sort_by("Price (High > Low)")

    def get_all_products_price(self):
        all_products = self.get_elements(self.PRODUCTS_PRICE)
        all_products_data = [product_element.text for product_element in all_products]
        all_products_price = [float(item.split('$')[1].replace(',', '').split('\n')[0]) for item in all_products_data]
        return all_products_price

    def are_all_products_sorted(self, sort_type):
        all_products_price = self.get_all_products_price()
        if sort_type == "ascending":
            return all_products_price == sorted(all_products_price)
        else:
            return all_products_price == sorted(all_products_price, reverse=True)




