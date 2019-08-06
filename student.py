import csv,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display

i=1
cha = 'A'

with Display() as display:

	driver = webdriver.Chrome(executable_path=r'C:\Users\SRI\Downloads\chromedriver_win32\chromedriver.exe')
	while i<120:
		driver.get('https://www.tkrcetautonomous.org')

		if(i>100 and (i%10 == 0) or cha == 'O' or cha == 'I'):
			cha = chr(ord(cha)+1)

		if(i%10==i):
			st = '17K91A010'+str(i)
		elif(i<=99) :
			st = '17K91A01'+str(i)
		elif(i>99) :
			st = '17K91A01'+cha+str(int(i%10))
		
		#print(st)
		driver.find_element_by_id('lnkLogins').click()
		driver.find_element_by_xpath('//*[@id="lnkStudent"]').click()
		driver.find_element_by_id('txtUserId').send_keys(st)#'17K91A05'+('0'+str(i))if i<10 else '17K91A05'+str(i))
		driver.find_element_by_id('txtPwd').send_keys(st)#'17K91A05'+('0'+str(i))if i<10 else '17K91A05'+str(i))
		driver.find_element_by_id('btnLogin').click()

		try:
			driver.find_element_by_id('lnkStuInfo').click()
			print(st)
		except :
			temp.clear()
			temp.append(st)
			temp.append('invalid user or wrong password')
			print(temp)
			with open('civil bio data.csv','a+',newline='') as g:
				writer = csv.writer(g)
				writer.writerow(temp)
				i+=1
				continue
		
		#with open ('temp var.txt') as f:

		res = driver.execute_script("return document.documentElement.outerHTML")
		soup = BeautifulSoup(res,'lxml')
		#print(soup.prettify())
		#f.write(str(soup.prettify()))
		table = soup.find('div',{'id':'cpStudCorner_PanelStuInfo'})
		#for tbody in soup.find_all('tbody'):
		#	print (tbody.find('.commentText'))#.get_text())
		#print(table )
		
		table_rows = table.find_all('tr')
		data = []
		temp = []

		y = table.find_all('input')
		for x in y:
			temp.append(str(x.get('value')))

		for tr in table_rows:
		    td = tr.find_all('td')
		    #print(td)
		    #print('\n\n\n')
		    row = [ele.text.replace('\n','') for ele in td]
		    #print(row)
		    data.append([ele for ele in row if ele]) # Get rid of empty values
		data.pop(0)
		data.pop(0)
		data.pop(0)
		driver.get('https://www.tkrcetautonomous.org/StudentLogin/Student/overallMarks.aspx')
		res = driver.execute_script("return document.documentElement.outerHTML")
		soup = BeautifulSoup(res,'lxml')

		temp.append(soup.find('span',{'id':'cpStudCorner_lblMarks'}).text)
		temp.append(soup.find('span',{'id':'cpStudCorner_lblDue'}).text)
		flat_list = []
		for sublist in data:
		    for item in sublist:
		        flat_list.append(item)


		flat_list.append('CGPA')
		flat_list.append('Due Subjects')
		with open('civil bio data.csv','a+',newline='') as g:
			writer = csv.writer(g)
			if i==1:
			 	writer.writerow(flat_list)
			writer.writerow(temp)

		i += 1



