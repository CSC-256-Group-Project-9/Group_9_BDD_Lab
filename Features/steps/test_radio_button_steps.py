from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch the Firefox browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@given(u'Open the browser to the web app')
def open_webapp(context):
    context.driver.get("https://group-9-unofficial.vercel.app/testing")


@given(u'radio button 4 is not selected by default')
def radio_button_4(context):
    radio4 = context.driver.find_element(By.XPATH, '//*[@id="python"]')
    assert not radio4.is_selected()


@when(u'The user selects Python radio button and presses submit')
def select_radio_button_4(context):
    radio4 = context.driver.find_element(By.XPATH, '//*[@id="python"]')
    radio4.click()
    button = context.driver.find_element(By.XPATH, '//*[@id="test4-button"]')
    button.click()


@then(u'The user sees "Favorite Language: Python" is displayed')
def display_selection(context):
    text_displayed = context.driver.find_element(By.XPATH, '//*[@id="result"]')
    assert text_displayed.text == "Favorite Language: Python"


@given(u'Radio Button 4 is selected and "Favorite Language: Python" is displayed')
def radio_button_1(context):
    radio4 = context.driver.find_element(By.XPATH, '//*[@id="python"]')
    radio4.click()
    assert radio4.is_selected()
    button = context.driver.find_element(By.XPATH, '//*[@id="test4-button"]')
    button.click()
    text_displayed = context.driver.find_element(By.XPATH, '//*[@id="result"]')
    assert text_displayed.text == "Favorite Language: Python"


@when(u'The user selects Radio Button 1 and presses submit')
def select_radio_button_1(context):
    radio1 = context.driver.find_element(By.XPATH, '//*[@id="javascript"]')
    radio1.click()
    button = context.driver.find_element(By.XPATH, '//*[@id="test4-button"]')
    button.click()


@then(u'The user sees ""Favorite Language: JavaScript" is displayed')
def display_selection(context):
    text_displayed = context.driver.find_element(By.XPATH, '//*[@id="result"]')
    assert text_displayed.text == "Favorite Language: JavaScript"


@then(u'Close Browser')
def close_browser(context):
    context.driver.close()
