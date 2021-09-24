import requests

query = input("please write a name")
url = "https://www.sogou.com/web?query={query}"

my_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
resp = requests.get(url,headers=my_headers)

print(resp)
print(resp.text)