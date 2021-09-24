import requests
from requests.sessions import session

url = "https://nco.zjgsu.edu.cn/login"


my_headers1 = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36"
}

dat = {
    "name":"21020100024",
    "psswd":"034818",
}
session = requests.session()

resp = session.post(url,headers = my_headers1,data = dat)
print(resp.text)
print("-"*50)

url2 = "https://nco.zjgsu.edu.cn/"
dat2 = {
    "uuid": "1db683d9-0d2c-4f83-9341-c9478711151c",
    "locationInfo": "浙江省杭州市江干区",
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
print(resp2.text)

