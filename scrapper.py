# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
# from pyvirtualdisplay import Display
#with Display() as display:
driver = webdriver.Chrome(r"C:\Users\SRI\Downloads\chromedriver_win32\chromedriver.exe")

i = int(194)
cha = 'P'
sec = 'D'
while i<=260:
	
	print(i)
	if(i%61 == 0):
		sec = chr(ord(sec)+1)
	if(i>100 and (i%10 == 0)):
		cha = chr(ord(cha)+1)

	if(i%10==i):
		st = '17K91A050'+str(i)
	elif(i<=99) :
		st = '17K91A05'+str(i)
	elif(i>99) :
		st = '17K91A05'+cha+str(int(i%10))
	
	i += 1
	if(st == '17K91A05P4'):
		continue

	driver.get('https://www.tkrcetautonomous.org/')

	select = driver.find_element_by_id('lnkLogins').click()

	studentBtn = driver.find_element_by_id('lnkStudent').click()

	usr = driver.find_element_by_id('txtUserId')
	usr.send_keys('17K91A05P0')

	psd = driver.find_element_by_id('txtPwd')
	psd.send_keys('17K91A05P0')

	login = driver.find_element_by_id('btnLogin').click()

	#k = driver.find_element_by_id('LinkButton2').click()
	#a = driver.find_element_by_id('lnkOverallMarks').click()
	driver.get('https://www.tkrcetautonomous.org/StudentLogin/Student/overallMarks.aspx')
	res = driver.execute_script("return document.documentElement.outerHTML")
	soup = BeautifulSoup(res,'lxml')

	table = soup.find('div',{'class':'grid_OverallMarks'})
	table_rows = table.find_all('tr')
	data = []
	
	for tr in table_rows:
	    td = tr.find_all('td')
	    row = [ele.text for ele in td]
	    data.append([ele for ele in row if ele]) # Get rid of empty values


	headers = data.pop(0)
	#df = pd.DataFrame(num,columns=headers)
	df = pd.DataFrame.from_records(data,columns=headers)
	#print(df)
	#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	#    print(df)
	df.to_csv(path_or_buf='/root/Desktop/Results/Results_Cse_'+sec+'/'+'17K91A05P0'+'.csv',na_rep='0')
	#driver.quit()