import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/channel.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup
r = requests.get(start_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('title').get_text().strip())

from pathlib import Path
stem = Path(start_url).stem
filename = f"{stem}.zip"
new_url = urllib.parse.urljoin(start_url, filename)
print(new_url)
r = requests.get(new_url)
with open(filename, 'wb') as f:
	f.write(r.content)

import zipfile
archive = zipfile.ZipFile(filename, 'r')
archive.extractall(stem)
import os
with open(os.path.join(stem, 'readme.txt'), 'r') as f:
	text = f.read()
nothing = text.splitlines()[-2].split(' ')[-1]
print(f"nothing={nothing}")
nothings = [nothing]
for i in range(len(os.listdir(stem))):
	with open(os.path.join(stem, f'{nothing}.txt'), 'r') as f:
		text = f.read()
	print(text)
	nothing = text.split(' ')[-1]
	if not nothing.isnumeric():
		break
	nothings.append(nothing)
	print(f"\tnothing={nothing}")

comments = [archive.getinfo(f"{nothing}.txt").comment.decode("utf-8") for nothing in nothings]
comments = ''.join(comments)
print(comments)

found = set()
solution = ''.join([c for c in comments if c.isalpha() and c not in found and (found.add(c) or True)]).lower()

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
