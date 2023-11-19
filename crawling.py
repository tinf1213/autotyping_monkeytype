import requests
from bs4 import BeautifulSoup

url = 'https://scholars.ncu.edu.tw/zh/persons/chia-yu-lin'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'lxml')

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post(url, data=payload)
# if r.status_code == requests.codes.ok:  
#     print(r.text)