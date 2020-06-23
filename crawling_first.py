import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200624&screencodes=&screenratingcode=&regioncode='
html = requests.get(url)
print(html.text)