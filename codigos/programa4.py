#Ejemplo break and continue
# for i in 'manuel':
#     if i in 'aeiou':
#         continue
    
#     print(i)
# suma = 0
# while True:
#     p = input('Pres: ')
#     if p.isdigit():
#         suma += float(p)
#     else:
#         break
# print(suma)

# Ejemplos librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# tex = " "
driver = webdriver.Edge()

# driver.get('https://es.wikipedia.org')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.title)
# tex = soup.text
# print(type(tex))
# # element = driver.find_element(By.ID, 'sb_form_q')
# # element.send_keys('WebDriver')
# # element.submit()

# time.sleep(5)
# driver.quit()

import re
# print(re.search(r'.*@','kelvin.3kung@utp.ac.pa'))

driver.get('https://es.wikipedia.org')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.title)
tex = soup.text
print(re.search(r'\d{1} de [a-z A-Z]* de \d{4}',soup.text))

time.sleep(5)
driver.quit()