#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
import base64
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'


def getLocalHostPublicIP():
    """
    :return:本机公网IP地址
    """
    headers = {}
    headers['User-Agent'] = USER_AGENT
    url = 'http://members.3322.org/dyndns/getip'  # 通过接口获取公网IP
    req = requests.get(url, headers=headers)
    res = req.text
    
    ip = res.strip()  # 去除空白符
    return ip

def sendMsgFromText(content):
    """
    :param body:邮件内容,纯文本格式
    :return: Bool, 返回是否成功
    """
    # This works for textfiles,pdffiles,images,audio files, and video files
    # with a sender, a receiver and subject line
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP("smtp.live.com", 587)
    server.starttls()  # There's a security function needed to connect to the Gmail server
    account = b'UVlRMTE1NDRAaG90bWFpbC5jb20='
    passwd = b'TWFjaW50b3NoMTU4OTY4'
    # server.login("QYQ11544@hotmail.com", "Macintosh158968")
    # bytes to string
    server.login(base64.b64decode(account).decode('ascii'), base64.b64decode(passwd).decode('ascii'))
    toEmail, fromEmail = "chyiyaqing@gmail.com", "QYQ11544@hotmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = "Subject ;-) Chyi + Public IP"  # 邮件标题

    body = '''
        这是一封定时(10:00)执行的任务!
        [Ubuntu 16.04.3] Public IP is {}
        如果还有其他问题,请发邮件联系! ;-)
        '''.format(content)  # contain message
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromEmail, toEmail, text)
    server.quit()
    return True
    
if __name__ == '__main__':
    ip = getLocalHostPublicIP()
    if sendMsgFromText(ip):
        print('Send Public IP address: {} to email Success!'.format(ip))
    else:
        print('Send Msg Fail!')
