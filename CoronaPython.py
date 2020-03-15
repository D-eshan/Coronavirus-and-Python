# Analyzing Coronavirus using Python?

from selenium import webdriver
from time import sleep


def GetInfo(browser): #get the information
    browser.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html')
    
    sleep(1)
    
    travel_related_cases = browser.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]').text
    
    close_contact_cases = browser.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]').text
    
    under_investiation_cases = browser.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').text
    
    total_cases = str(int(travel_related_cases) + int(close_contact_cases) + int(under_investiation_cases.replace(',','')))
    
    return travel_related_cases, close_contact_cases, under_investiation_cases, total_cases
    


def main():
    browser = webdriver.Chrome(r'C:\Users\eshan dixit\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    travel, close, investigation, total = GetInfo(browser)
    print('''Travel related cases: {}
close contact cases: {}
under investigation cases: {}
total cases: {}
    '''.format(travel, close, investigation, total))
    
main()

