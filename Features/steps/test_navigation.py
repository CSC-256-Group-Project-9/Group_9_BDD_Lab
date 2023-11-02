# This will test if the navigation buttons work ('COMMENTS CUT OUT AFTER LINE 25 DUE TO REPETITION' - David)
# Written by: Owen Cawlfield, David Smedberg

from behave import *
from selenium.webdriver.common.by import By


"""Test if the page title is as expected"""
@given(u'User starts on the Testing page of the web app')
def page_start(context):
    # Tests the title of the page
    assert context.driver.title == "Testing"


"""Click the API button to go to a different page"""
@when(u'User clicks the API button on the navigation bar')
def click_API(context):
    # Clicks the button to navigate to the API page
    context.driver.find_element(By.XPATH, '/html/body/a[3]').click()


"""Test if the page title is as expected on the new page"""
@then(u'The user sees the API page of the web app')
def page_API(context):
    # tests the title of the page
    assert context.driver.title == "API Endpoints"

@when(u'User clicks the About Us button on the navigation bar')
def click_about_us(context):
    context.driver.find_element(By.XPATH, '/html/body/a[4]').click()

@then(u'The user sees the About Us page of the web app')
def page_about_us(context):
    assert context.driver.title == "About us"

@when(u'User clicks the Contact Us button on the navigation bar')
def click_contact_us(context):
    context.driver.find_element(By.XPATH, '/html/body/a[5]').click()

@then(u'The user sees the Contact Us page of the web app')
def page_contact_us(context):
    assert context.driver.title == "Contact us"

@when(u'User clicks the Home button on the navigation bar')
def click_home(context):
    context.driver.find_element(By.XPATH, '/html/body/a[1]').click()

@then(u'The user sees the Home page of the web app')
def page_home(context):
    assert context.driver.title == "Home"

@when(u'User clicks the Testing button on the navigation bar')
def click_testing(context):
    context.driver.find_element(By.XPATH, '/html/body/a[2]').click()

@then(u'The user is back at the testing page of the web app')
def page_testing(context):
    assert context.driver.title == "Testing"
