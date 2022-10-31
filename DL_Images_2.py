import requests
from bs4 import BeautifulSoup
import os

url='https://www.shutterstock.com/image-photo/ugly-organic-rotten-vegetables-mutations-on-1675520470'

r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')
print(soup.title.text)