import requests
import time

img_url=['https://www.dreamstime.com/photos-images/rotten-fruit.html']


for img_url in img_url:
    img_bytes=requests.get(img_url).content
    img_name=img_url.split('/')[3]
    img_name=f'{img_name}.jpg'

    with open(img_name,'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} downloading')