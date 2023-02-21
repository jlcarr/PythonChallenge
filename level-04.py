import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.html'
path_url = urllib.parse.urljoin(start_url, '.')

import requests
from bs4 import BeautifulSoup
r = requests.get(start_url)
next_url = urllib.parse.urljoin(start_url, r.text)
print(next_url)

r = requests.get(next_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find('title').get_text().strip())

next_url = urllib.parse.urljoin(start_url, soup.find('a')['href'])
print(next_url)

nothing = ''
for i in range(400):
	r = requests.get(next_url, params={'nothing': nothing} if nothing else {})
	print(r.text)
	if r.text.strip() == 'Yes. Divide by two and keep going.':
		nothing = str(int(nothing)//2)
	elif r.text.endswith('.html'):
		solution = r.text
		break
	else:
		nothing = r.text.strip().split(' ')[-1]
	print(f"\tnothing={nothing}")

solution_url = urllib.parse.urljoin(start_url, solution)
print(solution_url)
