import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve

for x in range(1,6):
    url = 'https://tabelog.com/tw/osaka/rstLst/' + str(x) + '/'
    res = requests.get(url, params={'SrtT':'rt'})
    ans = BeautifulSoup(res.text)
    print('現在進行到%d頁' %(x))

    rst = ans.find_all('li', class_='list-rst')
    for i in rst:
        jp = i.find('small', class_='list-rst__name-ja').text
        point = i.find('b', class_='c-rating__val').text
        img = i.find('img', class_='c-img')['src']
        print(jp,point,img)

        cut = img.split('/')[-1]

        if not os.path.exists('picture'):
            os.mkdir('picture')

        address = 'picture/第' + str(x) + '頁/'
        if not os.path.exists(address):
            os.mkdir(address)

        final = address + cut
        urlretrieve(img, final)