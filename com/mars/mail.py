#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器:这个是qq邮箱服务器，直接复制就可以
mail_pass = "qkdbhygvhkvkebhd"  # 授权码
sender = 'mars-robot@qq.com'  # 你的邮箱地址
receivers = ['210087652@qq.com']  # 收件人的邮箱地址，可设置为你的QQ邮箱或者其他邮箱，可多个


# subject主题 /content内容
def send(subject, content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("mars-robot", 'utf-8')
    message['To'] = Header("210087652@qq.com", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败', e)


def sendHtml(subject, content):
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = Header("mars-robot", 'utf-8')
    message['To'] = Header("210087652@qq.com", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败', e)


if __name__ == '__main__':
    send('test', '小伙子你很危险啊！！！')
