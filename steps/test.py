from behave import given, when
from framework.driver_base import DriverBase


@given('I open a browser instance')
def step_impl(context):
    # Create an instance of BaseTest and pass the browser name
    base_test = DriverBase()

    # Set up the driver
    base_test.setup_driver()

    # Store the driver in the context for use in other steps
    context.driver = base_test.driver


@when('I navigate to this "{url}"')
def step_impl(context, url):
    driver = context.driver

    driver.get(url)