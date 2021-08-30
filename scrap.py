from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome('C:\class127\chromedriver_win32\chromedriver.exe')
browser.get(start_url)
time.sleep(15)

def scrap():
    headers=["name","distance","mass","radius"]
    planet_data=[]

    for i in range(1,448):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tags=ul_tag.find_all('li')

            temp_list=[]

            for index,li_tags in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tags.find_all('a')[0].contents[0])

                else:
                    try:
                        temp_list.append(li_tags.contents[0])

                    except:
                        temp_list.append(' ')

            planet_data.append(temp_list)

        browser.find_element_by_xpath('https://en.wikipedia.org/wiki/Apparent_magnitude').click()

    with open('scrapper.csv','w') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv.writerows(planet_data)

scrap()


    

                
                

            


