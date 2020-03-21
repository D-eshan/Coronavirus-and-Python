# Analyzing Coronavirus using Python?
# Basically getting the information from the official coronavirus website and diplaying it on the console.

# need to import the webdriver. For that 'pip inatall selenium' on the command line to the speific directory.

from selenium import webdriver

# can use a different method too. Sleep not preferable. kept it for the ease. 

from time import sleep


def GetInfo(browser): #get the information
    #getting the url and activating the webdriver object
    
    browser.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html')
    
    sleep(1)
    # sleep for 1 second before proceeding
    
    travel_related_cases = browser.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]').text
    
    # finding all the lements by the xpath method of the websdriver object
    
    close_contact_cases = browser.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]').text
    
    under_investiation_cases = browser.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').text
    
    # Just adding up the previous numbers
    
    total_cases = str(int(travel_related_cases) + int(close_contact_cases) + int(under_investiation_cases.replace(',','')))
    
    return travel_related_cases, close_contact_cases, under_investiation_cases, total_cases
    


def main():
    # creating the webdriver object
    
    browser = webdriver.Chrome(r'C:\Users\eshan dixit\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    travel, close, investigation, total = GetInfo(browser)
    # just simply printing everything out.
    print('''Travel related cases: {}
close contact cases: {}
under investigation cases: {}
total cases: {}
    '''.format(travel, close, investigation, total))

# calling the main function
    
main()

