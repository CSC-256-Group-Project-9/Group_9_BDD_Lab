# This will test if the navigation buttons work
# Written by: Owen Cawlfield

from behave import *
from selenium.webdriver.common.by import By

"""Test if the page title is as expected"""


@given(u'User starts on the testing page of the web app')
def page_start(context):
    # tests the title of the page
    assert context.driver.title == "Testing"


"""Click the navigation button to go to a different page"""


@when(u'User clicks the Home button on the navigation bar')
def click_home(context):
    # clicks the button to navigate to the Home page
    context.driver.find_element(By.XPATH, '/html/body/a[1]').click()


"""Test if the page title is as expected on the new page"""


@then(u'The user sees the home page of the web app')
def page_home(context):
    # tests the title of the page
    assert context.driver.title == "Home"
