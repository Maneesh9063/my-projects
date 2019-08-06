from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from pyvirtualdisplay import Display
import pandas as pd
import csv
import os
import datetime
#with Display():
a = datetime.datetime.now()
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/root/Desktop')#os.getcwd())#+str(a))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk",'image/png')# "file/png")

driver = webdriver.Firefox(firefox_profile=profile)

driver.get('https://chartink.com/screener/top-gainer-12')

res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res,'lxml')

table = soup.find('table',{'id':'DataTables_Table_0'})
table_rows = table.find_all('tr')
data = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [ele.text for ele in td]
    data.append([ele for ele in row if ele]) # Get rid of empty values

data.pop(0)

df = pd.DataFrame.from_records(data)#columns=headers)
df.drop([0])
df.to_csv(path_or_buf='/root/Desktop/17K91A05P0.csv',na_rep='0',index=False)

with open('17K91A05P0.csv') as csvfile:
	readIt = csv.reader(csvfile,delimiter=',')
	for row in readIt:
		if row[2] != '2':
			driver.get('https://chartink.com/stocks/'+row[2]+'.html')
			driver.switch_to.frame(driver.find_element_by_id('ChartImage'))
			driver.find_element_by_css_selector('div#saverbutton').click()

driver.quit()
#soumith852@gmail.com
#soumithchartink
