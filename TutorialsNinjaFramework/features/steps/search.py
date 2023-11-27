from behave import given, when, then
from features.pages.home_page import HomePage
from utilities.config_reader import ConfigReader


@given("I am on the Home page")
def step_given_home_page(context):
    context.home_page = HomePage(context.driver)
    context.feature_logger.info('Navigated to the Home page.')


@when('I enter valid product into the Search box field')
def step_when_enter_valid_product(context):
    valid_product = ConfigReader.get_products()["valid_product"]
    context.home_page.enter_product_into_search_box_field(valid_product)
    context.feature_logger.info(f'Entered valid product: {valid_product} into the Search box field.')


@when("I click on Search button")
def step_when_click_search_button(context):
    context.search_page = context.home_page.click_on_search_button()
    context.feature_logger.info('Clicked on the Search button.')


@then('I should see search results containing valid product only')
def step_then_search_results_contain_valid_product(context):
    valid_product = ConfigReader.get_products()["valid_product"]
    assert context.search_page.results_contain_product(valid_product)
    context.feature_logger.info(f'Search results contain the valid product: {valid_product}.')


@when('I enter invalid product into the Search box field')
def step_when_enter_invalid_product(context):
    invalid_product = ConfigReader.get_products()["invalid_product"]
    context.home_page.enter_product_into_search_box_field(invalid_product)
    context.feature_logger.info(f'Entered invalid product: {invalid_product} into the Search box field.')


@then("I should see a message indicating no search product were found")
def step_then_no_search_results(context):
    no_results_message = ConfigReader.get_no_search_results_message()
    assert context.search_page.display_status_of_message(no_results_message)
    context.feature_logger.info('Saw a message indicating no search product were found.')


@when("I dont enter anything into Search box field")
def step_when_no_product_entered(context):
    context.home_page.enter_product_into_search_box_field("")
    context.feature_logger.info('Did not enter anything into the Search box field.')


@when("sorts the results by price in '{order}' order")
def step_when_sort_by_price(context, order):
    context.search_page.sort_by_order(order)
    context.feature_logger.info('Sorted the results by price.')


@then("the results are sorted by price in '{order}' order")
def step_then_result_sorted_by_price(context, order):
    assert context.search_page.are_all_products_sorted(order)
    context.feature_logger.info('Results are sorted in descending order by price.')
