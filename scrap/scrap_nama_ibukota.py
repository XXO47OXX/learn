import grequests
from bs4 import BeautifulSoup
urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]
for (i, resp) in enumerate(grequests.imap((grequests.get(u) for u in urls), size=50)):
    if resp.status_code == 200: 
        soup = BeautifulSoup(resp.text, 'html.parser')
        file_name = urls[i].replace("http://", "").replace(',', '')
        with open(f'test/{file_name}.txt', 'w', encoding= 'utf-8') as f:
            f.write(f'{soup.prettify()}')