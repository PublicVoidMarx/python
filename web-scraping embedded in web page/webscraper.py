from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://www.digminecraft.com/search_results.php")

mob = input("ingresa nombre de mob")

WebDriverWait(driver,4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                        'input#terms')))\
    .send_keys('mob')

WebDriverWait(driver,2)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                        'button.btn.btn-primary')))\
    .click()          

WebDriverWait(driver,2)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                        'strong.text-success')))\
    .click()                             

WebDriverWait(driver,2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                        '/html/body/div[4]/div[2]/div[1]/div[1]/div/div[1]/div[2]/table')))\
                              

info_table= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[1]/div/div[1]/div[2]/table')
info_table = info_table.text

print(info_table)

driver.close







