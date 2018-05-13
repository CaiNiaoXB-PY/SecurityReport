# -*- coding: utf-8 -*-
# coding by kayserzhang
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import time
from binascii import b2a_hex,a2b_hex
from Crypto.Cipher import DES
import ld
import zip_md
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
from_addr ='发件邮箱地址'
username = '发件邮箱用户名'
cryppass='20afe42ce31026d0a7d66815fa7076fc'
obj = DES.new(username)
get_cryp = a2b_hex(cryppass)
after_text = obj.decrypt(get_cryp)
after_text=after_text.replace(" ","")
to_addr = '收件邮箱地址'
cc_addr = '抄送邮箱地址'
smtp_server = '发件服务器'
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Cc'] = cc_addr
msg['Subject'] = Header(u'安全简报检查项OA部分', 'utf-8').encode()
# add MIMEText:
ziptime = time.strftime('%Y%m%d%H',time.localtime(time.time()))
msg.attach(MIMEText(u'通用漏洞跟踪每日情况共' + ld.result_value + u'起' + u',附件为安全简报检查项OA部分截图，请查收！', 'plain', 'utf-8'))
# add file:
with open("C:\\Python27\\CheckResult\\SecureReport_OA_Image" + ziptime + ".zip", 'rb') as f:
    mime = MIMEBase('zip', 'zip', filename="SecureReport_OA_Image" + ziptime + ".zip")
    mime.add_header('Content-Disposition', 'attachment', filename="SecureReport_OA_Image" + ziptime + ".zip")
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,after_text)
server.sendmail(from_addr,[to_addr]+[cc_addr],msg.as_string())
server.quit()
