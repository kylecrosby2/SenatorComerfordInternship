#! python3

from selenium import webdriver
import time
import bs4


def main():
    upload_list = [
        {'Name': 'Eric Dion', 'Email': 'shemlin@rcmahar.org', 'Town': 'Orange', 'Position': '', 'Title': ''},
        {'Name': 'Douglas Daponde', 'Email': 'ddaponde@shschools.com', 'Town': 'South Hadley', 'Position': '',
         'Title': ''},
        {'Name': 'Henry John Skala', 'Email': 'hskala@shschools.com', 'Town': 'South Hadley', 'Position': '',
         'Title': ''},
        {'Name': 'Diana Bonneville', 'Email': 'dbonneville@shschools.com', 'Town': 'South Hadley', 'Position': '',
         'Title': ''},
        {'Name': 'Kristina Cloutier Kirton', 'Email': 'Kristina.Kirton@frsu38.org', 'Town': 'Whately', 'Position': '',
         'Title': ''},
        {'Name': 'Melissa Eaton', 'Email': 'melissa.eaton@northquabbinchamber.com', 'Town': '', 'Position': ' ',
         'Title': ' '},
        {'Name': 'Alec Wade', 'Email': 'awade@townoforange.org', 'Town': 'Orange', 'Position': '', 'Title': ''},
        {'Name': 'Andrea Llamas', 'Email': 'allamas@northfieldma.gov', 'Town': 'Northfield',
         'Position': 'Muni officials: Northfield', 'Title': 'Town Administrator'},
        {'Name': 'Mike Sullivan', 'Email': 'msullivan@southhadleyma.gov', 'Town': 'South Hadley',
         'Position': 'Muni officials: South Hadley', 'Title': 'Town Administrator'},
        {'Name': 'Brian Domina', 'Email': 'townadmin@whately.org', 'Town': 'Whately',
         'Position': 'Muni officials: Whately', 'Title': 'Town Administrator'},
        {'Name': 'Michael Blaine', 'Email': 'mblaine.waterpros@gmail.com', 'Town': 'Deerfield',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Deerfield'},
        {'Name': 'Kristin Gordon', 'Email': 'KRISTEN.GORDON@FRSU38.ORG', 'Town': 'Deerfield',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Deerfield'},
        {'Name': 'Rachel McLean', 'Email': 'HFCDC@LEVERETTNET.NET', 'Town': 'Leverett',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Leverett'},
        {'Name': 'Lawrence Ramsdel', 'Email': 'RAMSDELL@SWIFTRIVERSCHOOL.ORG', 'Town': 'New Salem',
         'Position': 'Water District Officials', 'Title': 'Water District Official, New Salem'},
        {'Name': 'Tim Brandi', 'Email': 'brandlt@pvrsdk12.org', 'Town': 'Northfield',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Northfield'},
        {'Name': 'Steve Malsh', 'Email': 'fairviewgardens@comcast.net', 'Town': 'Northfield',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Northfield'},
        {'Name': 'Patty Goclowski', 'Email': 'PATTY.GOCLOWSKI@FIRSTLIGHTPOWER.COM', 'Town': 'Northfield',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Northfield'},
        {'Name': 'Linda Tims', 'Email': 'ltims@rhwhite.com', 'Town': 'Sunderland',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Sunderland'},
        {'Name': 'Wayne Hukoski', 'Email': 'water@whately.org', 'Town': 'Whately',
         'Position': 'Water District Officials', 'Title': 'Water District Official, Whately'},
        {'Name': 'Betsy Sicard', 'Email': 'health@erving-ma.gov', 'Town': 'Erving',
         'Position': 'Muni officials: Erving', 'Title': ' '},
        {'Name': 'Valerie Bird', 'Email': 'Valerie.Bird@greenfield-ma.gov', 'Town': 'Greenfield',
         'Position': 'Muni officials: Greenfield', 'Title': ' '},
        {'Name': 'Daniel Wasiuk', 'Email': 'healthdir@montague-ma.gov', 'Town': 'Montague',
         'Position': 'Muni officials: Montague', 'Title': ' '},
        {'Name': 'Robert MacEwen', 'Email': 'bob2atnfld@gmail.com', 'Town': '', 'Position': ' ', 'Title': ' '},
        {'Name': 'Geoffrey David Sharp', 'Email': 'gdsharp@zurnsharpandheyman.com', 'Town': 'Deerfield',
         'Position': 'Muni officials: Deerfield', 'Title': 'U-Rep'},
        {'Name': 'Trevor McDaniels', 'Email': 'trevor.d.mcdaniel@gmail.com', 'Town': 'Deerfield',
         'Position': 'Muni officials: Deerfield', 'Title': 'CES Rep'},
        {'Name': 'Timmie Smith', 'Email': 'timmie.smith@gmrsd.org', 'Town': '', 'Position': ' ', 'Title': ' '},
        {'Name': 'Sasha Figueroa', 'Email': 'FigueroaS@arps.org', 'Town': '', 'Position': ' ', 'Title': ' '},
        {'Name': 'Sheryl Stanton', 'Email': 'sstanton@mtrsd.org', 'Town': 'Colrain',
         'Position': 'Muni officials: Colrain', 'Title': ' '},
        {'Name': 'Karen Totman', 'Email': 'ktotman@mohawkschools.org', 'Town': 'Colrain',
         'Position': 'Muni officials: Colrain', 'Title': ' '},
        {'Name': 'Jennifer Culkeen', 'Email': 'culkeen@erving.com', 'Town': 'Wendell',
         'Position': 'Muni officials: Wendell', 'Title': ' '},
        {'Name': 'Blanchard Sabrina', 'Email': 'sabrina.blanchard@gmrsd.org', 'Town': 'Montague',
         'Position': 'Muni officials: Montague', 'Title': ' '},
        {'Name': 'Martin McEvoy Jr', 'Email': 'dr.mjmcevoy@gmail.com', 'Town': 'Hatfield',
         'Position': 'Muni officials: Hatfield', 'Title': 'Superintendent of Schools'},
        {'Name': 'Riley Malinowski', 'Email': 'rmalinowski@hatfieldps.net', 'Town': 'Hatfield',
         'Position': 'Muni officials: Hatfield', 'Title': 'Administrative Assistant to the Superintendent'},
        {'Name': 'Darcy Fernandes', 'Email': 'dfernandes@arrsd.org', 'Town': 'Royalston',
         'Position': 'Muni officials: Royalston',
         'Title': 'Superintendent Ã¢â‚¬â€œ Director of Educational Services, Athol-Royalston School District'},
        {'Name': 'Jennifer Culkeen', 'Email': 'culkeen@erving.com', 'Town': 'Shutesbury',
         'Position': 'Muni officials: Shutesbury', 'Title': 'Superintendent of Schools, Erving School Union #28'},
        {'Name': 'Diana Bonneville', 'Email': 'dbonneville@shschools.com', 'Town': 'South Hadley',
         'Position': 'Muni officials: South Hadley', 'Title': 'Interim Superintendent of Schools'},
        {'Name': 'Lorie Cowan', 'Email': 'lorie.brooks@greenfield-ma.gov', 'Town': 'Greenfield',
         'Position': 'Muni officials: Greenfield', 'Title': 'Administrative Assistant'},
        {'Name': 'Jon Davine', 'Email': 'jdavine@northamptonma.gov', 'Town': 'Northampton', 'Position': 'Fire Chiefs',
         'Title': 'Assistant Fire Chief, Northampton'},
        {'Name': 'Christopher Blair', 'Email': 'police.christopher.blair@erving-ma.org', 'Town': 'Gill',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Gill'},
        {'Name': 'Robert Haigh Jr', 'Email': 'robh@greenfield-ma.gov', 'Town': 'Greenfield',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Greenfield'},
        {'Name': 'Joseph Camden', 'Email': '', 'Town': 'New Salem', 'Position': 'Police Chiefs',
         'Title': 'Chief of Police, New Salem'},
        {'Name': 'Jody Kasper', 'Email': 'jkasper@northamptonma.gov', 'Town': 'Northampton',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Northampton'},
        {'Name': 'Daniel Fernandes', 'Email': 'police.chief@shutesbury.org', 'Town': 'Shutesbury',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Shutesbury'},
        {'Name': 'Evan Briante', 'Email': 'briante@hadleyma.org', 'Town': 'Hadley', 'Position': 'Fire Chiefs',
         'Title': 'Deputy Fire Chief, Hadley'},
        {'Name': 'Larry Eaton', 'Email': 'deputychief@newsalemfire.org', 'Town': 'New Salem', 'Position': 'Fire Chiefs',
         'Title': 'Deputy Fire Chief, New Salem'},
        {'Name': 'Robert Flaherty Jr', 'Email': 'ambulance@townofhatfield.org', 'Town': 'Hatfield',
         'Position': 'Fire Chiefs', 'Title': 'Fire Chief, Hatfield'},
        {'Name': 'Duane Nichols', 'Email': 'dnichols@northamptonma.gov', 'Town': 'Northampton',
         'Position': 'Fire Chiefs', 'Title': 'Fire Chief, Northampton'},
        {'Name': 'Raymond Murphy Jr', 'Email': '', 'Town': 'Pelham', 'Position': 'Fire Chiefs', 'Title': ' '},
        {'Name': 'Chelsea JordanMakely', 'Email': 'griswold@colrain-ma.gov', 'Town': 'Colrain',
         'Position': 'Muni officials: Colrain', 'Title': ' '},
        {'Name': 'Barbara Friedman', 'Email': 'barbara.friedman@erving-ma.gov', 'Town': 'Erving',
         'Position': 'Muni officials: Erving', 'Title': ' '},
        {'Name': 'Lisa Downing', 'Email': 'director@forbeslibrary.org', 'Town': 'Northampton',
         'Position': 'Muni officials: Northampton', 'Title': ' '},
        {'Name': 'Jodi Levine', 'Email': 'library.pelham@gmail.com', 'Town': 'Pelham',
         'Position': 'Muni officials: Pelham', 'Title': ' '},
        {'Name': 'Katherine Hand', 'Email': 'director@sunderlandpubliclibrary.org', 'Town': 'Sunderland',
         'Position': 'Muni officials: Sunderland', 'Title': ' '},
        {'Name': 'Cyndi Steiner', 'Email': 'whatelypubliclibrary@gmail.com', 'Town': 'Whately',
         'Position': 'Muni officials: Whately', 'Title': ' '}]
    path = "C:/Users/kerry/Documents/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver2 = webdriver.Chrome(path)
    login_cf(driver)
    login_cf(driver2)
    add_email(driver, upload_list, driver2)


# Logs into cf with the webdriver.
def login_cf(driver):
    driver.get("https://communityfluency.com/office")
    email = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
    # Must input your email and password into the quotations below.
    email.send_keys('akylecrosby@gmail.com')
    password.send_keys('$omewhere391Flag')
    sign_in = driver.find_elements_by_xpath('//button[@type="submit"]')[0]
    sign_in.click()
    driver.find_element_by_id('call-log-tab').click()


def add_email(driver, upload_list, driver2):
    name_elem_num = ''
    for d in upload_list:
        finish = True
        if d['Email'] != '' and d['Email'] != ' ':
            name = d['Name']
            name_field = driver.find_element_by_id('call-subject')
            #name_field.clear()
            for i in list(name):
                name_field.send_keys(i)
            time.sleep(3)
            try:
                name_elem_num = get_constituent_number(driver)
            except IndexError:
                finish = False
            if finish is True:
                driver2.get('https://communityfluency.com/office/constituents/' + name_elem_num)
                driver2.find_element_by_xpath('//*[@id="main"]/div[1]/a/button').click()
                email_input = driver2.find_element_by_xpath('//*[@id="contact_form"]/table/tbody/tr[6]/td[2]/div[1]/input')
                email_input.send_keys(d['Email'])
                driver2.find_element_by_xpath('//*[@id="contact_form"]/div[2]/input[2]').click()
            driver.refresh()
            driver.find_element_by_id('call-log-tab').click()


def get_constituent_number(driver):
    html_text = driver.page_source
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    elems = soup.select('.ml-2')
    name_elem = elems[5]
    name_elem_num = ''
    start_value = ''
    append = False
    print(name_elem)
    for i in list(str(name_elem)):
        start_value += i
        if start_value == '<label class="ml-2" for="add-person-':
            append = True
            continue
        if append is True:
            if i == '>':
                break
            name_elem_num += i
    return name_elem_num[:-1]


main()
