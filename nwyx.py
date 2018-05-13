#--utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import cookielib
import urllib
import re
import sys
import urllib2
import pytesseract
from PIL import Image
from binascii import b2a_hex,a2b_hex
from Crypto.Cipher import DES
username = '用户名(不足8位后补空格)'
cryppass='7df445b29a45f637'
obj = DES.new(username)
get_cryp = a2b_hex(cryppass)
after_text = obj.decrypt(get_cryp)
after_text=after_text.replace(" ","")
driver = webdriver.Firefox()
url='http://xxx.xx.xx.com/wps/portal/'
driver.get(url)
sleep(0.5)
driver.find_element_by_id("userID").send_keys("用户名")
driver.find_element_by_id("password").send_keys(加密后密码)
driver.find_element_by_id("login.button.login").click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
driver.find_element_by_id("undoInnerMail").click()
sleep(0.5)
driver.switch_to_window(driver.window_handles[-1])
sleep(1.5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\nwyx.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\nwyx.png')
im=im.crop((5,5,1250,250))
im.save('C:\\Python27\\CheckResult\\img\\nwyx.png')
sleep(2)
the_frame = driver.find_element_by_xpath("html/frameset[1]/frameset[1]/frameset[1]/frame[1]")
driver.switch_to.frame(the_frame)
driver.find_element_by_xpath("/html/body/table/tbody/tr[13]/td/small[2]/a").click()
driver.switch_to.window(driver.window_handles[-1])
sleep(3)
driver.switch_to.default_content()
the_frame = driver.find_element_by_xpath("html/frameset[1]/frameset[1]/frame[1]")
driver.switch_to.frame(the_frame)
driver.find_element_by_xpath("/html/body/form[1]/table[1]/tbody[1]/tr[2]/td/button").click()
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
txllist_gs = Select(driver.find_element_by_id("hdrCorpSel"))
txllist_gs.select_by_value("0")
txllist_bm = Select(driver.find_element_by_id("hdrDeptSel"))
txllist_bm.select_by_index(1)
sleep(2)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\nwyxtxl.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\nwyxtxl.png')
im=im.crop((5,5,1030,550))
im.save('C:\\Python27\\CheckResult\\img\\nwyxtxl.png')
driver.close()
driver.quit()
