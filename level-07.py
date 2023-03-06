import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup
r = requests.get(start_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('title').get_text().strip())

filename = soup.find('img')['src']
new_url = urllib.parse.urljoin(start_url, filename)
print(new_url)
r = requests.get(new_url)
with open(filename, 'wb') as f:
	f.write(r.content)

from PIL import Image
img = Image.open(filename)

w,h = img.size
pxs = []
for i in range(0,w,7):
	px = img.getpixel((i,h//2))
	if px[0] != px[1]:
		break
	pxs.append(px[0])
#print(pxs)
msg = ''.join([chr(px) for px in pxs])
print(msg)

import re
msg2 = list(map(int,re.findall(r'(\d+)', msg)))
solution = ''.join([chr(c) for c in msg2])

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
