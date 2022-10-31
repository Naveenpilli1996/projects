import requests
import urllib.request
from bs4 import BeautifulSoup

url='https://www.dreamstime.com/photos-images/rotten-fruit.html?pg=6'

header=headers = {
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

r=requests.get(url=url,headers=header)
print(r) 

soup=BeautifulSoup(r.text,'html.parser')
i=0

for img in soup.findAll('img'):
    i=i+1
    # print(img)
    imge_temp=img.get('data-src')
    #print(imge_temp)

    # if imge_temp[:1]=='/':   # creating full URL link or path to every image
    #     image_path='https://www.dreamstime.com/photos-images/rotten-fruit.html'+imge_temp
    # else:
    #     image_path=imge_temp


    # print(image_path)

    if '.jpg' in imge_temp:  # For only gettingt .jpg formate files
        with open('Images/URL_6/'+'{}.jpg'.format(i),'wb') as f:
            f.write(requests.get(url=imge_temp).content)
        # print(imge_temp)
    else :
        pass

    # img=requests.get(url=imge_temp).content
    # with open()
    

print('Downloading done')

