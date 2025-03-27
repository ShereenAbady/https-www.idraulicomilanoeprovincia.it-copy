import requests
from bs4 import BeautifulSoup

url = 'https://www.idraulicomilanoeprovincia.it/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

img_urls = [img['src'] for img in img_tags]
for img_url in img_urls:
    print(img_url,"-----")
