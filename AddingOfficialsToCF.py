#! python3
# AddingOfficialsToCF.py - Inputs officials from list into CF.

from selenium import webdriver
import bs4
import time
import re


def main():
    #file = open('C:/Users/kerry/Documents/Comerford Internship/Officials_Not_In_CF_Final.txt')
    #info_list = get_info_from_file(file)
    upload_list = [
        {'Name': 'Derek Shea', 'Email': 'AldrichCA@arps.org', 'Town': 'Amherst', 'Position': '', 'Title': ''},
        {'Name': 'Bob Clancy', 'Email': 'clancyb@pvrsdk12.org', 'Town': 'Bernardston', 'Position': '', 'Title': ''},
        {'Name': 'Tina Gemme', 'Email': 'tina.gemme@frsu38.org', 'Town': 'Deerfield', 'Position': '', 'Title': ''},
        {'Name': 'George Lanides', 'Email': 'Darius.Modestow@frsu38.org', 'Town': 'Deerfield', 'Position': '',
         'Title': ''},
        {'Name': 'Lisa Candito', 'Email': 'candito@erving.com', 'Town': 'Erving', 'Position': '', 'Title': ''},
        {'Name': 'Greg Runyan', 'Email': 'grunyan@gcvs.org', 'Town': 'Greenfield', 'Position': '', 'Title': ''},
        {'Name': 'Christopher Buckland', 'Email': 'cbuckland@hatfieldps.net', 'Town': 'Hatfield', 'Position': '',
         'Title': ''},
        {'Name': 'Annie Leonard', 'Email': 'annie.leonard@gmrsd.org', 'Town': 'Montague', 'Position': '', 'Title': ''},
        {'Name': 'Beth Choquette', 'Email': 'bchoquette@northampton-k12.us', 'Town': 'Northampton', 'Position': '',
         'Title': ''},
        {'Name': 'Lesley Wilson', 'Email': 'lwilson@northampton-k12.us', 'Town': 'Northampton', 'Position': '',
         'Title': ''},
        {'Name': 'Lori Vaillancourt', 'Email': 'lorivaillancourt@northampton-k12.us', 'Town': 'Northampton',
         'Position': '', 'Title': ''},
        {'Name': 'Joseph Bianca', 'Email': 'jbianca@smithtec.org', 'Town': 'Northampton', 'Position': '', 'Title': ''},
        {'Name': 'Jean Bacon', 'Email': 'baconj@pvrsdk12.org', 'Town': 'Northfield', 'Position': '', 'Title': ''},
        {'Name': 'Eric P Dion', 'Email': 'shemlin@rcmahar.org', 'Town': 'Orange', 'Position': '', 'Title': ''},
        {'Name': 'Douglas A Daponde', 'Email': 'ddaponde@shschools.com', 'Town': 'South Hadley', 'Position': '',
         'Title': ''},
        {'Name': 'Henry John Skala', 'Email': 'hskala@shschools.com', 'Town': 'South Hadley', 'Position': '',
         'Title': ''},
        {'Name': 'Diana L Bonneville', 'Email': 'dbonneville@shschools.com', 'Town': 'South Hadley', 'Position': '',
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
        {'Name': 'Martin J McEvoy Jr', 'Email': 'dr.mjmcevoy@gmail.com', 'Town': 'Hatfield',
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
        {'Name': 'Robert H Haigh Jr', 'Email': 'robh@greenfield-ma.gov', 'Town': 'Greenfield',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Greenfield'},
        {'Name': 'Joseph P Camden', 'Email': '', 'Town': 'New Salem', 'Position': 'Police Chiefs',
         'Title': 'Chief of Police, New Salem'},
        {'Name': 'Jody Kasper', 'Email': 'jkasper@northamptonma.gov', 'Town': 'Northampton',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Northampton'},
        {'Name': 'Daniel Fernandes', 'Email': 'police.chief@shutesbury.org', 'Town': 'Shutesbury',
         'Position': 'Police Chiefs', 'Title': 'Chief of Police, Shutesbury'},
        {'Name': 'Evan Briante', 'Email': 'briante@hadleyma.org', 'Town': 'Hadley', 'Position': 'Fire Chiefs',
         'Title': 'Deputy Fire Chief, Hadley'},
        {'Name': 'Larry Eaton', 'Email': 'deputychief@newsalemfire.org', 'Town': 'New Salem', 'Position': 'Fire Chiefs',
         'Title': 'Deputy Fire Chief, New Salem'},
        {'Name': 'Robert J Flaherty Jr', 'Email': 'ambulance@townofhatfield.org', 'Town': 'Hatfield',
         'Position': 'Fire Chiefs', 'Title': 'Fire Chief, Hatfield'},
        {'Name': 'Duane Nichols', 'Email': 'dnichols@northamptonma.gov', 'Town': 'Northampton',
         'Position': 'Fire Chiefs', 'Title': 'Fire Chief, Northampton'},
        {'Name': 'Raymond A Murphy Jr', 'Email': '', 'Town': 'Pelham', 'Position': 'Fire Chiefs', 'Title': ' '},
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
    login_cf(driver)
    upload_to_cf(upload_list, driver)


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


def get_info_from_file(file):
    file_text = file.read()
    line_list = file_text.split('\n')
    info_list = []
    for line in line_list:
        person_list = line.split(',')
        line_dict = identify_values(person_list)
        info_list.append(line_dict)
    print(info_list)
    return info_list


def identify_values(person_list):
    line_dict = {'Name': '', 'Email': '', 'Town': '', 'Position': '', 'Title': ''}
    town_list = ['Amherst', 'Bernardston', 'Colrain', 'Deerfield', 'Erving', 'Gill', 'Greenfield', 'Hadley', 'Hatfield',
                 'Leverett', 'Leyden', 'Ludlow', 'Montague', 'New Salem', 'Northampton', 'Northfield', 'Orange',
                 'Pelham', 'Royalston', 'Shutesbury', 'South Hadley', 'Sunderland', 'Warwick', 'Wendell', 'Whately']
    email_regex = re.compile('\S+@\S+')
    #print(person_list)
    for value in person_list:
        value_s = value.strip()
        if person_list.index(value) == 0:
            line_dict['Name'] = value_s
            continue
        if value_s == line_dict['Name']:
            continue
        for town in town_list:
            if value_s == town:
                line_dict['Town'] = value_s
                continue
        for email in email_regex.findall(value):
            line_dict['Email'] = email.strip()
            continue
    for value in person_list:
        value_s = value.strip()
        if value_s != line_dict['Name'] and value_s != line_dict['Email'] and value_s != line_dict['Town']:
            line_dict['Title'] = value_s
            if 'Fire' in line_dict['Title'] or 'Police' in line_dict['Title'] or 'Water' in line_dict['Title']:
                if 'Fire' in line_dict['Title']:
                    line_dict['Position'] = 'Fire Chiefs'
                    line_dict['Title'] += ', %s' % line_dict['Town']
                if 'Police' in line_dict['Title']:
                    line_dict['Position'] = 'Police Chiefs'
                    line_dict['Title'] += ', %s' % line_dict['Town']
                if 'Water' in line_dict['Title']:
                    line_dict['Position'] = 'Water District Officials'
                    line_dict['Title'] += ', %s' % line_dict['Town']
            else:
                line_dict['Position'] = 'Muni officials: ' + line_dict['Town']

    return line_dict


def edit_list(info_list):
    upload_list = []
    for info_dict in info_list:
        new_dict = {'Name': '', 'Email': '', 'Town': '', 'Position': '', 'Title': ''}
        print('\n')
        print(info_dict)
        user_input = input('Press 1 to edit: ')
        if user_input == '1':
            for value in info_dict:
                print('%s: %s' % (value, info_dict.get(value)))
                user_value = input('Press Enter to keep the same value, or type in a new value to add that. ')
                if user_value != '':
                    new_dict[value] = user_value
                else:
                    new_dict[value] = info_dict[value]
            print(new_dict)
            upload_list.append(new_dict)
        else:
            upload_list.append(info_dict)
    return upload_list


def upload_to_cf(upload_list, driver):
    for info_dict in upload_list:
        driver.get('https://communityfluency.com/office/constituents/new')
        name_value_list = split_name(info_dict['Name'])
        # Input first name.
        driver.find_element_by_xpath('//*[@id="contact_form"]/table/tbody/tr[1]/td[2]/input').send_keys(name_value_list[0])
        # Input last name.
        driver.find_element_by_xpath('//*[@id="contact_form"]/table/tbody/tr[2]/td[2]/input').send_keys(name_value_list[-1])
        # Click position checkbox.
        if info_dict['Position'] != '' and info_dict['Position'] != ' ':
            id_num = find_position_checkbox(driver, info_dict['Position'])
            driver.find_element_by_id(id_num).click()
            if info_dict['Title'] != ' ' and info_dict['Title'] != '':
                # Input title.
                driver.find_element_by_xpath('//*[@id="title_%s"]' % id_num).send_keys(info_dict['Title'])
        # Click first save button.
        driver.find_element_by_xpath('//*[@id="contact_form"]/div[1]/div/input').click()
        # Input middle initial
        if len(name_value_list) > 2:
            driver.find_element_by_xpath('//*[@id="contact_form"]/table/tbody/tr[2]/td[2]/input[2]').send_keys(name_value_list[1])
        # Input email.
        driver.find_element_by_xpath('//*[@id="contact_form"]/table/tbody/tr[6]/td[2]/div[1]/input').send_keys(info_dict['Email'])
        # Click second save button.
        driver.find_element_by_xpath('//*[@id="contact_form"]/div[2]/input[2]').click()


def split_name(name):
    name_value_list = []
    last_name = ''
    name_list = name.split(' ')
    for i in range(len(name_list)):
        if i == 0:
            name_value_list.append(name_list[i])
        if i == 1 and len(name_list[i]) == 1:
            name_value_list.append(name_list[i])
        if i >= 1 and len(name_list[i]) > 1:
            last_name += ' ' + name_list[i]
    name_value_list.append(last_name)
    return name_value_list


def find_position_checkbox(driver, position):
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    id_num = ''
    for i in range(1, 90):
        selector = '#contact_form > div.flex.mt-2 > div:nth-child(1) > div.mt-2.text-sm > div:nth-child(%s) > div.flex-grow.mr-4 > label' % str(i)
        elem = soup.select(selector)
        if elem:
            if elem[0].text == position:
                elem_str = str(elem[0])
                str_list = list(elem_str)
                str_list.reverse()
                symbol_count = 0
                append = False
                for c in str_list:
                    if symbol_count == 2:
                        append = True
                    if c == '>':
                        symbol_count += 1
                    if append is True:
                        if c == '=':
                            break
                        id_num += c
                id_num = id_num[::-1]
                id_num = id_num[1:-1]
                break
    return id_num


main()
