import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/equality.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup, Comment
r = requests.get(start_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('title').get_text().strip())

cipher_tag = soup.findAll(text=lambda text:isinstance(text, Comment))[-1]
cipher_text = cipher_tag.extract().replace('\n','')
import re
solution = ''.join(re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', cipher_text))

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
