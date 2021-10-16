import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com', 25)#这里使用163来发送邮件qq的话改为smtp.qq.com
username = '805456875@qq.com'#你的邮箱名
password = 'qmgyrirxsttgbeej'#你的动态密码（注意这里不是你的密码而是你在163开启的smtp的动态码）
smtp.login(username, password)
sender = '805456875@qq.com'#发送人邮箱名
receiver = 'wofeishenling@hotmail.com'#接收者邮箱
#发送邮件文本内容
subject = '打卡通知！'#文件内容
msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = 'wofeishenling'
msg['To'] = 'wofeishenling@hotmail.com'
text = '打卡通知！'#文件内容
text_plain = MIMEText(text, 'plain', 'utf-8')#邮件内容
msg.attach(text_plain)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()