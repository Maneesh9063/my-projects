import csv,os,time,urllib,requests,shutil
from selenium import webdriver
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display

i=12
cha = 'A'
def save_image_to_file(image, dirname, suffix):
	with open('{dirname}/img_{suffix}.jpg'.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
		shutil.copyfileobj(image.raw, out_file)


#with Display() as display:

driver = webdriver.Firefox()#(executable_path=r'C:\\Users\\SRI\\Downloads\geckodriver-v0.24.0-win64/geckodriver.exe')
while i<13:
	driver.get('https://www.tkrcetautonomous.org')

	if(i>100 and (i%10 == 0) or cha == 'O' or cha == 'I'):
		cha = chr(ord(cha)+1)

	if(i%10==i):
		st = '17K91A040'+str(i)
	elif(i<=99) :
		st = '17K91A04'+str(i)
	elif(i>99) :
		st = '17K91A04'+cha+str(int(i%10))
	
	#print(st)
	driver.find_element_by_id('lnkLogins').click()
	driver.find_element_by_xpath('//*[@id="lnkStudent"]').click()
	driver.find_element_by_id('txtUserId').send_keys(st)#'17K91A05'+('0'+str(i))if i<10 else '17K91A05'+str(i))
	driver.find_element_by_id('txtPwd').send_keys(st)#'17K91A05'+('0'+str(i))if i<10 else '17K91A05'+str(i))
	driver.find_element_by_id('btnLogin').click()

	try:
		driver.find_element_by_id('lnkStuInfo').click()
		print(st)
		i+=1
	except :
		temp.clear()
		temp.append(st)
		temp.append('invalid user or wrong password')
		print(temp)
		#with open('ECE bio data.csv','a+',newline='') as g:
		#	writer = csv.writer(g)
		#	writer.writerow(temp)
		i+=1
		continue
	

	res = driver.execute_script("return document.documentElement.outerHTML")
	soup = BeautifulSoup(res,'lxml')
	#print(soup.prettify())
	#f.write(str(soup.prettify()))
	table = soup.find('img',{'id':'ImgStudent'}).get('src')
	s= 'https://www.tkrcetautonomous.org/StudentLogin/Student/'+table
	print(s)
	r = requests.get(s,stream=True).content
	#save_image_to_file(r,'root/Desktop',st)
	#print(r)
	driver.get(s)
	k = urllib.request.urlretrieve(s)#,filename=os.path.basename(st)+'.jpeg')
	
	with open('aaa.png','wb') as f:
		f.write(r)
	driver.quit()



