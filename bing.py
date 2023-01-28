#! /usr/bin/python3

import Xlib.display
import webbrowser
import os
import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import searchTerms

os.environ['DISPLAY'] = ':0'
os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
items = len(searchTerms.terms) - 1

def setBrowserOptions(userAgent):
	chromeOptions = Options()

	if(userAgent == 'edge'):
		chromeOptions.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"')
	elif(userAgent == 'mobile'):
		chromeOptions.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"')
	
	chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
	#chromeOptions.add_experimental_option("detach", True)
	chromeOptions.add_argument(ADD_PATH_HERE)
	driver = webdriver.Chrome(options=chromeOptions)
	return driver

def pcSearches():
	driver = setBrowserOptions('edge')
	googleCount = 0

	clear = lambda: os.system('cls')

	while googleCount < 35:
		index = random.randint(0,items)
		cooldown = random.randint(6, 19)
		driver.get(searchTerms.searchURL + searchTerms.terms[index].lower())
		googleCount += 1
		time.sleep(cooldown)

	driver.quit()

def edgeSearches():
	driver = setBrowserOptions('edge')
	edgeCount = 0
	
	while edgeCount < 8:
		index = random.randint(0,items)
		cooldown = random.randint(6, 19)
		driver.get(searchTerms.searchURL + searchTerms.terms[index].lower())
		edgeCount += 1
		time.sleep(cooldown)

	driver.quit()

def mobileSearches():
	driver = setBrowserOptions('mobile')
	mobileCount = 0
	
	while mobileCount < 28:
		index = random.randint(0,items)
		cooldown = random.randint(6, 19)
		driver.get(searchTerms.searchURL + searchTerms.terms[index].lower())
		mobileCount += 1
		time.sleep(cooldown)

	driver.quit()



pcSearches()
edgeSearches()
mobileSearches()







