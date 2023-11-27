from behave import given, when, then
from features.pages.home_page import HomePage
from utilities.config_reader import ConfigReader


@given('I am on the registration page')
def step_given_registration_page(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()
    context.feature_logger.info('Navigated to the registration page.')


@when('I enter below details into mandatory fields')
def step_when_enter_mandatory_details(context):
    table = context.table
    for row in table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_email(row["email"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
    context.feature_logger.info('Entered mandatory details for registration.')


@when('I select Privacy Policy option')
def step_when_select_privacy_policy(context):
    context.register_page.select_privacy_policy()
    context.feature_logger.info('Selected Privacy Policy option.')


@when('I click on Continue button')
def step_when_click_continue(context):
    context.account_success_page = context.register_page.click_on_continue_button()
    context.feature_logger.info('Clicked on the Continue button.')


@then('Account should get created')
def step_then_account_created(context):
    success_message = ConfigReader.get_account_created_success_message()
    assert context.account_success_page.display_status_of_account_created_heading(success_message)
    context.feature_logger.info('Account has been created successfully.')


@when('I enter details into all fields except email field')
def step_when_enter_all_fields_except_email(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()
    context.feature_logger.info('Entered details into all fields except the email field.')


@when('I enter existing accounts email "{email}" into email field')
def step_when_enter_existing_email(context, email):
    context.register_page.enter_email(email)
    context.feature_logger.info(f'Entered existing account email: {email}.')


@then('I should see a warning message for duplicate email')
def step_then_see_warning_message_for_duplicate_email(context):
    duplicate_email_warning = ConfigReader.get_duplicate_email_warning()
    assert context.register_page.display_status_of_duplicate_email_warning(duplicate_email_warning)
    context.feature_logger.info(f'Saw warning message: {duplicate_email_warning}.')



@when('I dont enter anything into the fields')
def step_when_dont_enter_anything(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_password_confirm("")
    context.feature_logger.info('Left all fields empty.')


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_then_warning_messages_displayed(context):
    expected_warnings = ConfigReader.get_warning_messages()
    assert context.register_page.display_status_of_all_warning_messages(*expected_warnings)
    context.feature_logger.info('Saw proper warning messages for every mandatory field.')

