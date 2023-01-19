from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('C:/Users/shubh/OneDrive/Desktop/Web Scraper/chromedriver.exe')
browser.get(start_url)
time.sleep(10)

planet_data =[]
def scrape():
    for i in range(0,10):
        print(f"scraping page {i+1}")
        
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for j in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = j.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try :
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
        
            planet_data.append(temp_list)
        
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        

scrape()
headers = ["name", "light years from earth", "planet mass", "stellar magnitude", "dicovery date"]
planet__ = pd.DataFrame(planet_data, columns= headers)
planet__.to_csv("planets.csv", index = True, index_label="id")
