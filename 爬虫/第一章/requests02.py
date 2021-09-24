import requests

url = "https://fanyi.baidu.com/sug"

s = input()
dat = {
    "kw": s
}

resp = requests.post(url,data = dat)
print(resp.json())