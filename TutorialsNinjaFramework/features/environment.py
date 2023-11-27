import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities.config_reader import ConfigReader
from utilities.logger import CustomLogger
from utilities.credentials_manager import CredentialsManager


def before_feature(context, feature):
    context.feature_logger = CustomLogger(feature.name, f"log/{feature.name}.log").get_logger()


def before_scenario(context, scenario):
    browser_name = ConfigReader.get_browser()

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.get_base_url())


def after_scenario(context, scenario):
    context.driver.quit()


def before_tag(context, login):
    context.login_credentials = CredentialsManager()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)
