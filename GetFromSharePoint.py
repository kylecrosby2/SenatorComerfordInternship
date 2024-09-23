#! python3
# GetFromSharePoint.py - Open email data directly from MS Sharepoint.

from selenium import webdriver
from selenium.webdriver import ActionChains
import bs4
import time


def main():
    path = "C:/Users/kerry/Documents/chromedriver.exe"
    driver = webdriver.Chrome(path)
    login_sharepoint(driver)
    click_on_emails(driver)
    #get_email_data(driver)


def login_sharepoint(driver):
    driver.get('https://malegislature.sharepoint.com/sites/MAGC-SenatorComerford')
    # Input email.
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="i0116"]').send_keys('akylecrosby@gmail.com')
    # Click Next button.
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    # Input password.
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="i0118"]').send_keys('6tRXib4c$rsn3HNSQV9!8Nkb$3')
    # Click sign in.
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    # Click no on remember account if it shows up.
    try:
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="idBtn_Back"]').click()
    except Exception:
        pass
    # Get code from user input.
    time.sleep(1)
    user_input = input('Number texted to you: ')
    driver.find_element_by_xpath('//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(user_input)
    # Click Verify
    driver.find_element_by_xpath('//*[@id="idSubmit_SAOTCC_Continue"]').click()
    # Go to Constituent emails.
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="spLeftNav"]/div[2]/nav/div/div/ul/li[8]/div/a').click()
    time.sleep(2)


def get_email_data(driver):
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    contact_elem_list = soup.select('.ms-List-page')
    print(contact_elem_list)
    specific_contact_elem_list = []
    for elem in contact_elem_list:
        for name in elem:
            if 'Kyle' in str(name):
                specific_contact_elem_list.append(name)
    for elem in specific_contact_elem_list:
        print(str(elem))


def get_data_from_html():
    file = open('SharePointHTML.txt')
    soup = bs4.BeautifulSoup(file.read(), 'html.parser')


def click_on_emails(driver):
    print('Scroll down to bottom of emails now.')
    time.sleep(12)
    driver.find_element_by_xpath('//*[@id="appRoot"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[29]/div/div[1]/div/div/i[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="appRoot"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[29]/div/div[2]/div[3]/div/div[2]/div/button[2]/span/i').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/ul/li[1]/button/div/span').click()
    time.sleep(60)


main()
