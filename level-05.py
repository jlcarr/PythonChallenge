import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/peak.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup
r = requests.get(start_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('title').get_text().strip())

next_url = urllib.parse.urljoin(start_url, soup.find('peakhell')['src'])
print(next_url)
r = requests.get(next_url)
import pickle
p = pickle.loads(r.content)
p = '\n'.join([''.join(c[0]*c[1] for c in l) for l in p])
print(p)
solution = 'channel'

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
