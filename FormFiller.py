#! python3
# FormFiller.py - Fills out a form I made at this link:
# https://form.jotform.com/202688265614057

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def main():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://form.jotform.com/202688265614057")
    notes = driver.find_element_by_class_name('form-textarea')
    user_input = input("Form text: ")
    notes.send_keys(user_input)
    date_picker1 = driver.find_element_by_id('lite_mode_3')
    date_picker1.send_keys('09/04/2020')
    dropdown = Select(driver.find_element_by_id('input_7'))
    dropdown.select_by_visible_text('Revenge of the Sith')

    time.sleep(5)


def cf():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://communityfluency.com/office")
    email = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
    email.send_keys('akylecrosby@gmail.com')
    password.send_keys('$omewhere391Flag')
    sign_in = driver.find_elements_by_xpath('//button[@type="submit"]')[0]
    sign_in.click()
    driver.find_element_by_id('call-log-tab').click()
    dropdown = driver.find_elements_by_xpath('//*[@id="call-log-add"]/div[1]/div[1]/div[1]/select/option[23]')
    dropdown[0].click()
    time.sleep(5)


cf()


