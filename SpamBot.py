#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import threading
import os,sys
import os.path
import json
from crontab import CronTab
import subprocess
import requests
import selenium
import tldextract
from selenium import webdriver
import unittest 
import contextlib
import selenium.webdriver as webdriver
import numpy as np
import Gnuplot
from shutil import copyfile
import hashlib
import cPickle as pickle
import socket
import time
from random import randint
import robotparser
from selenium import webdriver
from PIL import Image
from cStringIO import StringIO
from pyvirtualdisplay import Display
from googletrans import Translator
import signal
import os
from random import random, randint
import getpass


mail = ''
paswd = ''
print "Default mails to login:\n"
i = 1
with open("creds/creds.txt","r") as file:
	for l in file:
		print "Mail N."+str(i)+": "+l.split(" ")[0]
		i+=1
print "\n------If you wish to login with one of these mails press the number you wish(else press ENTER)------\n"
number = raw_input()
if number:
	i = 0
	with open("creds/creds.txt","r") as file:
		for l in file:
			i+=1
			if int(number) == i:
				
				mail =  l.split(" ")[0]
				paswd = l.split(" ")[1]
				used = True
				break
else:	
	mail = raw_input("Mail:")
	pswd = getpass.getpass('Password:')

	used = False

msgtospam = raw_input("Spam message:")
os.system("killall -9 firefox")
options = Options()
options.add_argument("--headless")
profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(firefox_profile=profile,firefox_options = options)
driver.set_page_load_timeout(50)


driver.set_page_load_timeout(randint(35, 45))
#"dom.webnotifications.enabled", false
driver.get("https://www.facebook.com")


elems = driver.find_elements_by_xpath("//input[@id]")

for elem in elems:
	if elem.get_attribute("id") in "email":
		try:
			elem.send_keys(mail)
		except:
			continue
	if elem.get_attribute("id") in "password":
		try:
			elem.send_keys(pswd)
		except:
			continue
time.sleep(1)
elems[:] = []
print "Successfull login!"

if not used:
	with open("creds/creds.txt", "a+") as file:
		file.write(mail+' '+pswd+'\n')

elems = driver.find_elements_by_xpath("//input[@id]")
for elem in elems:
	if "u_0_" in elem.get_attribute("id"):
		try:
			elem.click()
			break
		except:
			continue

time.sleep(2)
elems[:] = []
driver.implicitly_wait(9)
elems = driver.find_elements_by_xpath("//input[@class]")
for elem in elems:
	if "_1frb" in elem.get_attribute("class"):
		try:
			print str(elem.get_attribute("class"))
			elem.click()
			elem.send_keys(str(sys.argv[1])+" "+str(sys.argv[2]))
			
			break
		except:
			print "Encode error"
			continue
elems = driver.find_elements_by_xpath("//button[@class]")
for elem in elems:
	if "42ft _4jy0 _4w98 _4jy3 _517h _51sy _4w97" in elem.get_attribute("class"):
		try:
			
			elem.click()
			
			break
		except:
			continue
driver.implicitly_wait(5)
elems[:] = []
elems = driver.find_elements_by_xpath("//a[@class]")
for elem in elems:
	if str(sys.argv[1])+" "+str(sys.argv[2]) in elem.text:
		try:
			
			elem.click()
			
			
			
		except:
			continue

messager = driver.current_url.split("/")[3]
print messager
driver.get("https://www.facebook.com/messages/t/"+messager)

time.sleep(3)
driver.implicitly_wait(9)
i = 50
for number in range(1,i):
	link = driver.current_url
	elems[:] = []
	elems = driver.find_elements_by_xpath("//div[@class]")
	for elem in elems:
		
		try:
			
			
			driver.implicitly_wait(1)
			elem.send_keys(msgtospam+str(number))
			driver.implicitly_wait(5)
			ActionChains(driver).key_down(Keys.ENTER).perform()
			print str(elem.get_attribute("class"))

		except:
			0
			continue
	
	driver.implicitly_wait(5)
	driver.get(link)
	driver.implicitly_wait(5)
	time.sleep(3)

time.sleep(40)
