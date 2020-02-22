import sys
from time import sleep
# import time
# from scraper import get_driver, connect_to_base, parse_html
import requests
import traceback
import sys
# import tldextract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import scrapy
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import json
import numpy as np
import signal
import sys
import pandas as pd


# INITIALISE THE SELENIUM CHROME DRIVER
def get_driver():
    # initialize options
    options = webdriver.ChromeOptions()
    # pass in headless argument to options                                                                                                                          
    options.add_argument('--headless')
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('window-size=1920x1480')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")         
    options.add_argument('--disable-dev-shm-usage') 
    # Pass the argument 1 to allow and 2 to block
    options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)


    # initialize driver
    # driver = webdriver.Remote(
    #             command_executor=f'http://{address}:4444/wd/hub',
    #             desired_capabilities=DesiredCapabilities.CHROME,options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    return driver

# CHECK THE URL  CONNECTION AND IF OK GET THE URL HTML DATA ELSE IT WILL ATTEMPTS FOR 4 TIMES , IF 4 TIMES FAILED RETURN EMPTY OR ERROR.
def connect_to_base(browser, base_url):
    
    connection_attempts = 0
    while connection_attempts < 4:
        list_url = []
        # description = ''
        try:
            # flags = 0
            browser.get(base_url)
        # IF WANT TO USE SCRAPY SELECTOR UNCOMMENT AND USE IT
        #     response = scrapy.Selector(
        # text=browser.page_source)
            
        # THIS IS CODE WILL EXTRACT EVERY LINK IN THE HTML PAGE AND RETURN AS A LIST.YOU CAN ADD ANY STATEMENT REGARDING YOUR PROJECT
            # browser.find_element_by_tag_name('html').send_keys(Keys.END)
            # # print('base_url:',base_url)
            # # print('current_url:',browser.current_url)
            # elems = browser.find_elements_by_xpath("//a[@href]")
            # for elem in elems:
            #     string_href = elem.get_attribute("href")
            #     if 'http' not in string_href:
            #         string_href = browser.current_url + '/'+ string_href
            #     tldextract.extract().domain
            #     if tldextract.extract(browser.current_url).domain == tldextract.extract(string_href).domain:
            #         list_url.append(string_href)
            #         flags = 1
            # list_url.append(browser.current_url)
            
            #         pass
            
            # if flags == 0:
            #     return False,[]
            
            
            return True,list_url
        except Exception as ex:
            connection_attempts += 1
            print(f'Error connecting to {base_url}.')
            print(f'Attempt #{connection_attempts}.')
    return False,[]

# THIS FUNCTION IS USED TO PARSE THE HTML DATA.YOU CAN WRITE AS MUCH AS PARSE FUNCTION 
def parse_html(html):
    response = scrapy.Selector(
        text=html)
    # paragraph = response.xpath("//p//text()").extract()
    # li        = response.xpath("//li//text()").extract()
    # div       = response.xpath("//div/text()").extract()
    # paragraph = '. '.join(paragraph)
    # li = '. '.join(li) 
    # div = '. '.join(div) 
    return []#[paragraph,li,div]
    
    
# RUN PROCESS IS THE MAIN FUNCTION WHICH CONTAIN ALL OTHER FUNCTION
def run_process(browser,url):
    check,url_list = connect_to_base(browser, url)
    # print(check,'......................')
    # print(url_list,'::::::::::::::::::::::::::')
    # url_list = list(set(url_list))
    # new_url_list = []
    # parse_data_list = []
    # parse_title_list = []
    # parse_keyword_list = []
    # parse_description_list = []
    if check:
    #     sleep(1)
    #     for hrefss in url_list:
    #         browser.get(hrefss)
    #         browser.find_element_by_tag_name('html').send_keys(Keys.END)
    #         html = browser.page_source
    #         parsed_data,titles,keywords,description = parse_html(html)
    #         parse_data_list.append(parsed_data)
    #         new_url_list.append(hrefss)
    #         parse_title_list.append(titles)
    #         parse_keyword_list.append(keywords)
    #         parse_description_list.append(description)
    #     return new_url_list,parse_data_list,parse_title_list,parse_keyword_list,parse_description_list
        return ''
    else:
        return ''



if __name__ == '__main__':
    try: 
        browser = get_driver()
        # href,id = sys.argv[1:]
        href = 'https://www.example.com'
        id   = 'Id_for_syn'
        try:
            data = run_process(browser,href)
            #do anything with data
        except:                   # IF EXCEPTION OCCUR IT WILL CHECK FOR RESPONSE STATUS IF IT IS 200 MEANS THE WEBSITE IS BLOCKED.
                                    # ELSE WEBSITE IS DOWN , YOU HAVE TO CHECK FOR RESPONSE STATUS MEANING.
            r = requests.get(href)
            if r.status_code == 200:
                browser.get(href)
                html = browser.page_source
                response = scrapy.Selector(
        text=html)
                # check = response.css('#headerimage::attr(name)').extract()
            else:
                with open('http_error_code_url_list.txt','a+') as f:
                    f.write(href+','+str(r.status_code)+'\n') 
        
        print(f'Finished page {id}')
        browser.quit()
    except Exception as e:
        print(traceback.print_tb(e.__traceback__),'........................')
        browser.quit()
        sys.exit(-1)
