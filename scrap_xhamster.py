from bs4 import BeautifulSoup
import requests

url = 'https://zh.xhamster3.com/search/pov?quality=1080p&min-duration=10&max-duration=20'
with open('link_xhamster.txt', 'w', encoding='utf-8') as f:
    pass
for i in range(1,21):
    if i > 1 :
        url = f'{url}&page={i}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    allvideos = soup.find_all('div', attrs={'class':'thumb-list__item video-thumb'})
    with open('link_xhamster.txt', 'a', encoding='utf-8') as f:
        data = f.write(f'page - {i}\n\n')
        for a in allvideos:
            for i in a.find_all('a', href=True):
                link_image = i.find('img', {'class': "thumb-image-container__image"})
                if not link_image:
                    continue
                f.write(f"link - image : {link_image['src']}")
                f.write('\n')
                f.write(f"title : {str(link_image['alt'])}")
                f.write('\n')
                f.write(f"link - video : {i['href']}")
                f.write('\n\n = = = = = = = = = = =\n\n')