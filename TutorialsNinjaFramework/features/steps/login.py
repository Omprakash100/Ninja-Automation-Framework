from behave import given, when, then
from features.pages.home_page import HomePage
from utilities.config_reader import ConfigReader


@given('I am on the login page')
def step_given_login_page(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()
    context.feature_logger.info('Navigated to the login page.')


@when('I enter valid email')
def step_when_enter_valid_email(context):
    valid_email = context.login_credentials.get_valid_email()
    context.login_page.enter_email_address(valid_email)
    context.feature_logger.info(f'Entered valid email: {valid_email}')


@when('I enter valid password')
def step_when_enter_valid_password(context):
    valid_password = context.login_credentials.get_valid_password()
    context.login_page.enter_password(valid_password)
    context.feature_logger.info(f'Entered valid password: {valid_password}')


@when('I click the login button')
def step_when_click_login_button(context):
    context.account_page = context.login_page.click_on_login_button()
    context.feature_logger.info('Clicked the login button.')


@then('I should be redirected to the account page')
def step_then_redirected_to_account_page(context):
    current_title = context.login_page.get_title()
    expected_title = ConfigReader.get_account_page_title()
    assert current_title == expected_title, f"Expected Title: {expected_title}, Actual Title: {current_title}"
    context.feature_logger.info('Successfully redirected to the account page.')


@when('I enter invalid email "{email}"')
def step_when_enter_invalid_email(context, email):
    context.login_page.enter_email_address(email)
    context.feature_logger.info(f'Entered invalid email: {email}')


@then('I should see an error message')
def step_then_see_error_message(context):
    expected_message = ConfigReader.get_invalid_credentials_warning()
    assert context.login_page.display_status_of_warning_message(expected_message)
    context.feature_logger.info(f'Saw error message: {expected_message}')


@then("I should remain on the login page")
def step_then_remain_on_login_page(context):
    current_title = context.login_page.get_title()
    expected_title = ConfigReader.get_login_page_title()
    assert current_title == expected_title, f"Expected Title: {expected_title}, Actual Title: {current_title}"
    context.feature_logger.info('Remained on the login page.')


@when('I enter invalid password "{password}"')
def step_when_enter_invalid_password(context, password):
    context.login_page.enter_password(password)
    context.feature_logger.info(f'Entered invalid password: {password}')


@when("I leave both email and password fields empty")
def step_when_leave_both_fields_empty(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
    context.feature_logger.info('Left both email and password fields empty.')
