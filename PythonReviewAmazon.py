from bs4 import BeautifulSoup, NavigableString
import time
import pandas as pd
import math
import codecs
import datetime
import os
import requests
import re
import urllib2
from shutil import copyfile
from fake_useragent import UserAgent

'''

try:
	os.stat(BSROUTPUT)
	output=codecs.open(BSROUTPUT,'a','utf-8')	
except:
	output=codecs.open(BSROUTPUT,'a','utf-8')
	output.write('ASIN,Reviewer Name,Reviewer Star,Reviewer Date,Year,Reviewer Summary\n')
'''
ua = UserAgent()
#driver = webdriver.Chrome()
lines=['B00KM15VWY','B0055429GO']
for jj in lines:
	BSROUTPUT=str(jj)+" Review.csv"
	try:
		os.stat(BSROUTPUT)
		output=codecs.open(BSROUTPUT,'a','utf-8')	
	except:
		output=codecs.open(BSROUTPUT,'a','utf-8')
		output.write('ASIN,Reviewer Name,Reviewer Star,Reviewer Date,Year,Reviewer Summary\n')
	asinnumber=jj
	count=1
	soup=''
	v=[]
	while True:
		print count
		url='https://www.amazon.com/product-reviews/'+jj+'/ref=cm_cr_arp_d_paging_btm_'+str(count)+'?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(count)
		count=count+1
		response = requests.get(url, headers={'User-agent': ua.random})
		soup = BeautifulSoup(response.content,"lxml")
		#v=[]
		try:
			v=soup.findAll('div',{'class':'a-section review'})
			for i in v:
				output.write(str(asinnumber))
				output.write(",")
				name=i.find('div',{'class':'a-profile-content'})
				name=name.get_text()
				output.write(str(name))
				output.write(",")
				
				review=i.find('span',{'class':'a-icon-alt'})
				review=review.get_text()
				output.write(str(review))
				output.write(",")

				date=i.find('span',{'data-hook':'review-date'})
				date=date.get_text()
				print date
				output.write(str(date))
				output.write(",")
				review=""
				try:
					review=i.find('span',{'data-hook':'review-body'})
					review=review.get_text()
					review=review.replace(",","")					
					output.write(str(review))
				except:
					review=str("")
					output.write(str(review))
				output.write("\n")			
		except:
			break
		print len(v)
		if len(v)==0:
			print 'yes'
			break
		time.sleep(1)
		
	output.close()
