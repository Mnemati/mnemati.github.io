import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('file:///C:/Users/nmmhm/OneDrive/Desktop/New%20folder/html5up-massively/clubs.html')
#driver.get('file:///C:/Users/nmmhm/OneDrive/Desktop/New%20folder/html5up-massively/articles.html')
print(driver.title)

main = driver.find_element_by_id('main')
clubs = main.find_elements_by_tag_name('article')
#print(articles.text)
#print(main.text)
TeamName = []
for club in clubs:
	header = club.find_element_by_class_name('entry_title')
	TeamName = np.append(TeamName, header.text)
	
print(TeamName)
#time.sleep(2)
driver.quit()
#search = driver.find_element_by_name('q')
#print('search')