import requests
import uuid
import time
from requests.sessions import session
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

url = "https://nco.zjgsu.edu.cn/login"

my_headers1 = {
    # 模拟移动端环境
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36"
}

dat = {
    "name":"21020100024", #student id
    "psswd":"034818",# maybe the last six digits of id
}
session = requests.session() #用session自动记录上下午cookie

resp = session.post(url,headers = my_headers1,data = dat)
#print(resp.text)
#print("-"*50)

time.sleep(5)

url2 = "https://nco.zjgsu.edu.cn/"
my_uuid = uuid.uuid1() #随机生成一个uuid

dat2 = {
    "uuid": my_uuid,
    "locationInfo": "浙江省杭州市钱塘区", #所在地
    "currentResd": "浙江省杭州市浙江工商大学下沙校区",
    "fromHbToZjDate": "",
    "fromHbToZj": "C",
    "fromWtToHzDate": "",
    "fromWtToHz": "B",
    "meetDate": "",
    "meetCase": "C",
    "travelDate": "",
    "travelCase": "D",
    "medObsvReason": "",
    "medObsv": "B",
    "belowCaseDesc": "",
    "belowCase": "D",
    "temperature": "",
    "notApplyReason": "",
    "hzQRCode": "A",
    "specialDesc": "",
}
resp2 = session.post(url2,data=dat2,headers=my_headers1)
#print(resp2.text)

#------------------------------------


smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com', 587)#这里使用163来发送邮件qq的话改为smtp.qq.com
username = '805456875@qq.com'#你的邮箱名
password = '******'#你的动态密码（注意这里不是你的密码而是你在163开启的smtp的动态码）
smtp.login(username, password)
sender = '805456875@qq.com'#发送人邮箱名
receiver = 'wofeishenling@hotmail.com'#接收者邮箱
#发送邮件文本内容
subject = '打卡通知！'#文件内容
msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = 'wofeishenling'
msg['To'] = 'wofeishenling@hotmail.com'
text = resp2.text #文件内容
text_plain = MIMEText(text, 'plain', 'utf-8')#邮件内容
msg.attach(text_plain)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

