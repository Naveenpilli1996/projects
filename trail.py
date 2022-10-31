import requests
import urllib.request
from bs4 import BeautifulSoup
import os




url='https://www.dreamstime.com/photos-images/rotten-fruit.html?pg=1'
# print(url[-1])

urls=[]

for page in range(1,10):
    Rem_last_elemnt=url.rstrip(url[-1])
    New_url=Rem_last_elemnt+str(page)

    header=headers = {
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',}

    r=requests.get(url=New_url,headers=header)
    print(r) 

    soup=BeautifulSoup(r.text,'html.parser')

    os.makedirs("/home/ubuntu/Programming/Python/Downloading Images/Images/URL_"+str(page))

    print('Folder Created :',page)

    Links=soup.findAll('img')
    del Links[-1]
    # print(Links)
    # print('ALL Links are: ',Links)

    i=0
    # for img in soup.findAll('img'):
    for img in Links:
        i=i+1
        # print(img)
        imge_temp=img.get('data-src')
        #print(imge_temp)

        if imge_temp=='None':  # For only gettingt .jpg formate files
            print('No URL')
        # print(imge_temp)
        else :
            with open('Images/URL_'+str(page)+'/'+f'{i}.jpg','wb') as f:
                f.write(requests.get(url=imge_temp).content)
            

    print('Completd page :',page)

 

# # print(urls)
# print(urls)