import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup, Comment
r = requests.get(start_url)
soup = BeautifulSoup(r.text, 'html.parser')
cipher_tag = soup.findAll(text=lambda text:isinstance(text, Comment))[-1]
cipher_text = cipher_tag.extract()
from collections import Counter
counts = Counter(cipher_text)
solution = ''.join(c for c in cipher_text if counts[c]<counts['\n'])

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
