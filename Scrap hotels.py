#there are some time sleep funtions due to my slow internet that can be skiped

from os import write
import time
from typing import Counter
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

place = input("type place to look up for ")
driver.get('https://www.google.com/travel/hotels/'+place+'?')

time.sleep(3)

hoteles = driver.find_elements_by_class_name('PVOOXe')

counter = 0
amount = 0  #specific amount of hotels wanted

with open('Hoteles.csv','w') as file:
    writer = csv.writer(file)

    for hotel in hoteles:
        #if counter >= amount:        
        #    break
        
        hotel.click()       #goes for all the pages of each hotel found
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])

        row = []
            
        row.append(driver.find_element_by_xpath('//*[@id="overview"]/c-wiz/c-wiz/div/div[1]/div/div/c-wiz[1]/div/section[1]/div[1]/h1').text)
        try:
            row.append(driver.find_element_by_xpath('//*[@id="overview"]/c-wiz/c-wiz/div/div[1]/div/div/c-wiz[1]/div/section[1]/div[3]/div/span[1]').text)
        except:
            row.append("no address associated")
        try:
            row.append(driver.find_element_by_xpath('//*[@id="overview"]/c-wiz/c-wiz/div/div[1]/div/div/c-wiz[1]/div/section[1]/div[3]/div/span[3]').text)
        except:
            row.append("no phone associated")
    
        writer.writerow(row)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        counter += 1

driver.close()


    


