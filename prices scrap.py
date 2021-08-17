import xlsxwriter
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd


workbook = xlsxwriter.Workbook('Ofertas.xlsx')
worksheet = workbook.add_worksheet()

money = workbook.add_format({'num_format': '#,##0.00'})
bold = workbook.add_format({'bold': True})
worksheet.write('A1','item',bold)
worksheet.write('B1','price',bold)

row = 1
col = 0

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.mercadolibre.com.ar/ofertas#c_id=/home/promotions-recommendations/element&c_uid=cab07659-e283-417e-a3c0-009cf4732627')

products = driver.find_elements_by_class_name("promotion-item__description")

for product in products:
    worksheet.write(row,col,product.find_element_by_class_name("promotion-item__title").text)
    worksheet.write(row,col+1,product.find_element_by_class_name('promotion-item__price').text, money)
    row+=1
    
driver.close()
workbook.close()