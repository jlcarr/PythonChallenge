import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/map.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup
r = requests.get(start_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('title').get_text().strip())

cipher_tag = soup.find('font', attrs={'color':'#f000f0'})
cipher_text = cipher_tag.get_text().strip()
ord_a = ord('a')
decipher = lambda s: ''.join(chr((ord(c)-ord_a+2)%26+ord_a) if 0<=ord(c)-ord_a<26 else c for c in s)
clear_text = decipher(cipher_text)
print(clear_text)

from pathlib import Path
cipher_text = Path(start_url).stem
solution = decipher(cipher_text)

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
