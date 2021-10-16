from re import sub
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/meinvtupian/"
resp = requests.get(url)
resp.encoding = "utf-8"
#print(resp.text)

main_page = BeautifulSoup(resp.text,"html.parser")
alist = main_page.find("div",class_ = "TypeList").find_all("a")
#print(alist)
url1 ="https://www.umei.cc"
for a in alist:
    href = url1 + a.get("href")
    #print(href)
    sub_page_resp = requests.get(href)
    sub_page_resp.encoding = "utf-8"
    sub_page_text = sub_page_resp.text
    #print(sub_page_text)
    sub_page = BeautifulSoup(sub_page_text,"html.parser")
    p = sub_page.find("div",class_ = "ImageBody").find("p")
    img = p.find("a").find("img")
    src_url = img.get("src")
    #download src
    img_resp = requests.get(src_url)
    #img_resp.content #字节码
    img_name = src_url.split("/")[-1]
    with open("/Users/wofeishenling/Pictures/"+img_name, mode="wb") as f:
        f.write(img_resp.content)
    
    print("over!",img_name)
    time.sleep(1)
