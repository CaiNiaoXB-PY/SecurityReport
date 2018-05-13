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

driver = webdriver.Ie()
url='http://www.cnvd.org.cn/flaw/statistic'
driver.get(url)
sleep(1.5)
driver.switch_to_window(driver.window_handles[-1])
th = Select(driver.find_element_by_id("threadId"))
th.select_by_value("7")
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
lastweek = today - datetime.timedelta(days=7)
js = "$('input[id=startDate]').attr('readonly','')"
driver.execute_script(js)
driver.find_element_by_id('startDate').send_keys(yesterday)
sleep(2)
js = "$('input[id=endDate]').attr('readonly','')"
driver.execute_script(js)
driver.find_element_by_id('endDate').send_keys(yesterday)
sleep(2)
driver.find_element_by_xpath("//div[@id='flawDisSearchDiv']/input[3]").click()
sleep(5)
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\ldfb.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\ldfb.png')
#(left, top, left+width, top+height)
im=im.crop((280,225,1000,680))
im.save('C:\\Python27\\CheckResult\\img\\ldfb.png')
js = "$('input[id=trendStartDate]').attr('readonly','')"
driver.execute_script(js)
driver.find_element_by_id('trendStartDate').send_keys(lastweek)
sleep(2)
js = "$('input[id=trendEndDate]').attr('readonly','')"
driver.execute_script(js)
driver.find_element_by_id('trendEndDate').send_keys(yesterday)
sleep(2)
driver.find_element_by_xpath("//div[@id='searchDiv']/input[3]").click()
sleep(5)
find_element = driver.find_element_by_xpath("//div[@id='trendLineContent']/object/param[5]")
element_value = find_element.get_attribute("value").replace("%0A","%3B")
element_value = urllib.unquote(element_value).replace(";",",") + "end"
element_value = element_value.split(',')
result_value = element_value[-2]
driver.get_screenshot_as_file('C:\\Python27\\CheckResult\\img\\ldqs.png')
im=Image.open('C:\\Python27\\CheckResult\\img\\ldqs.png')
im=im.crop((280,725,1000,1210))
im.save('C:\\Python27\\CheckResult\\img\\ldqs.png')
driver.close()
driver.quit()
