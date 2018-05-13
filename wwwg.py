from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import cookielib
import urllib
import re
import sys
import urllib2
import datetime
from PIL import Image
import re
import sys
from binascii import b2a_hex,a2b_hex
from Crypto.Cipher import DES
username = '用户名(不足8位后补空格)'
cryppass='62b9cc7481fd49794a4f956df95f24a3'
obj = DES.new(username)
get_cryp = a2b_hex(cryppass)
after_text = obj.decrypt(get_cryp)
after_text=after_text.replace(" ","")
driver = webdriver.Firefox()
url='https://homepage:' + after_text + '@xxx.xx.xx.xx/'
driver.get(url)
sleep(10)
driver.switch_to.frame("Header")
sleep(2)
driver.switch_to.parent_frame()
#s = driver.find_element_by_xpath("//frameset[@id='fs3']/frame")
driver.switch_to.frame("Feature")
driver.find_element_by_xpath("/html/body/div[@id='globalContainer']/div[@id='nexusAnchor']/div[1]/div[1]/ul[1]/li[6]/a").click()
sleep(5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\wwwg115.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\wwwg115.png')
#(left, top, left+width, top+height)
im=im.crop((15,180,685,550))
im.save('C:\\Python27\\CheckResult\\img\\wwwg115.png')
driver.close()
driver.quit()
driver = webdriver.Firefox()
url='https://homepage:' + after_text + '@xxx.xx.xx.xx/'
driver.get(url)
sleep(10)
driver.switch_to.frame("Header")
sleep(2)
driver.switch_to.parent_frame()
#s = driver.find_element_by_xpath("//frameset[@id='fs3']/frame")
driver.switch_to.frame("Feature")
driver.find_element_by_xpath("/html/body/div[@id='globalContainer']/div[@id='nexusAnchor']/div[1]/div[1]/ul[1]/li[6]/a").click()
sleep(5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\wwwg116.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\wwwg116.png')
#(left, top, left+width, top+height)
im=im.crop((15,180,685,550))
im.save('C:\\Python27\\CheckResult\\img\\wwwg116.png')
driver.close()
driver.quit()

