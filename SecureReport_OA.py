# -*- coding:utf-8 -*-
# coding by kayserzhang
#环境要求：Python 2.7 selenium 2.53.1 firefox 46.0
#火狐浏览器下载：http://ftp.mozilla.org/pub/firefox/releases/
#手工安装selenium:解压缩安装包后，执行python setup.py install
#import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import cookielib
import urllib
import re
import sys
import urllib2
from binascii import b2a_hex,a2b_hex
from Crypto.Cipher import DES
username = '8位用户名(若长度不足，后补空格)'
cryppass='11f9767cc67fd163'
obj = DES.new(username)
get_cryp = a2b_hex(cryppass)
after_text = obj.decrypt(get_cryp)
after_text=after_text.replace(" ","")
driver = webdriver.Firefox()
url='http://xxx.xx.xx.xx/miradmin'
driver.get(url)
sleep(0.5)
driver.find_element_by_name("user").send_keys("用户名")
driver.find_element_by_name("password").send_keys(加密后密码)
driver.find_element_by_name("login").click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
s='防病毒'
driver.find_element_by_link_text(s).click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
s='Sophos Antivirus'
driver.find_element_by_link_text(s).click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
s='更新'
driver.find_element_by_link_text(s).click()
sleep(0.5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\fbd_23.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\fbd_23.png')
im=im.crop((100,100,660,620))
im.save('C:\\Python27\\CheckResult\\img\\fbd_23.png')
driver.close()
driver.quit()
driver = webdriver.Firefox()
url='http://xxx.xx.xx.xx/miradmin'
driver.get(url)
sleep(0.5)
driver.find_element_by_name("user").send_keys("用户名")
driver.find_element_by_name("password").send_keys(加密后密码)
driver.find_element_by_name("login").click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
s='防病毒'
driver.find_element_by_link_text(s).click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
s='Sophos Antivirus'
driver.find_element_by_link_text(s).click()
sleep(1.5)
driver.switch_to_window(driver.window_handles[-1])
s='更新'
driver.find_element_by_link_text(s).click()
sleep(1.5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\fbd_24.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\fbd_24.png')
im=im.crop((100,100,660,620))
im.save('C:\\Python27\\CheckResult\\img\\fbd_24.png')
driver.close()
driver.quit()
username = '用户名(不足8位后补空格)'
cryppass='7df445b29a45f637'
obj = DES.new(username)
get_cryp = a2b_hex(cryppass)
after_text = obj.decrypt(get_cryp)
after_text=after_text.replace(" ","")
driver = webdriver.Firefox()
url='http://xxx.xx.com/wps/portal/'
driver.get(url)
sleep(1.5)
driver.find_element_by_id("userID").send_keys("用户名")
driver.find_element_by_id("password").send_keys(加密后密码)
driver.find_element_by_id("login.button.login").click()
sleep(1.5)
driver.switch_to_window(driver.window_handles[-1])
driver.find_element_by_id("undoOuterMail").click()
sleep(3.5)
driver.switch_to_window(driver.window_handles[-1])
sleep(3.5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\wwyx.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\wwyx.png')
im=im.crop((5,5,1250,250))
im.save('C:\\Python27\\CheckResult\\img\\wwyx.png')
driver.switch_to.frame("s_MainFrame")
driver.find_element_by_xpath("//div[@id='e-mailoutline']/div[@id='e-mailoutline-content']/div[1]/table[1]/tbody[1]/tr[1]/td[3]").click()
driver.switch_to.window(driver.window_handles[-1])
sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame("s_MainFrame")
driver.find_element_by_xpath("//div[@id='e-$new-0-recipients']/table[1]/tbody[1]/tr[3]/td[1]/a").click()
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
driver.find_element_by_xpath("//div[@id='_easyui_tree_2']/span[1]").click()
sleep(1)
driver.find_element_by_xpath("//div[@id='_easyui_tree_3']/span[2]").click()
sleep(1.5)
driver.find_element_by_xpath("//div[@id='_easyui_tree_5']/span[1]").click()
sleep(2)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\wwyxtxl.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\wwyxtxl.png')
im=im.crop((5,5,1030,550))
im.save('C:\\Python27\\CheckResult\\img\\wwyxtxl.png')
driver.close()
driver.quit()
import nwyx
import wwwg
import email_md
