import urllib.parse
start_url = 'http://www.pythonchallenge.com/pc/def/0.html'
path_url = urllib.parse.urljoin(start_url, '.')

solution = 2**38

solution_url = urllib.parse.urljoin(start_url, f"{solution}.html")
print(solution_url)
