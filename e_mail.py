#发件人 -> MUA -> MTA -> 若干个MTA -> MTA -> MDA (企业的服务器)<- MUA（客户端，非网页版） <- 收件人
#编写MUA把邮件发到MTA；
#编写MUA从MDA上收邮件。

#MUA和MTA使用的协议就是SMTP
#MUA和MDA使用的协议有两种：
#POP：Post Office Protocol，称POP3；
#IMAP：Internet Message Access Protocol



#SMTP发送邮件
#smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#---------------------邮件正文------------传入'plain'表示纯文本-
#最后一定要用utf-8编码保证多语言兼容性。

然后，通过SMTP发出去：

# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())#as_string()把MIMEText对象变成str。
server.quit()


From: 13306523806@163.com
Password: 160103ABC.
To: 3160103035@zju.edu.cn
SMTP server: smtp.163.com

#------------------------------------------------------------------------














