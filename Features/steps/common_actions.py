# These are the common actions all tests will do. These include launching the browser and
# opening to the specified webpage to test and finally closing the browser after the tests

from behave import *
from selenium import webdriver


@given(u'Launch the Firefox browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@given(u'Open the browser to the web app')
def open_webapp(context):
    context.driver.get("https://group-9-unofficial.vercel.app/testing")


@then(u'Close Browser')
def close_browser(context):
    context.driver.close()
