from requests import request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import random
import string
import re

sequence = 2


def dec2hex(text_string):
    return hex(text_string + 0).upper()[2:]


def dec2char(n):
    result = ''
    if n <= 0xFFFF:
        result += chr(n)
    elif n <= 0x10FFFF:
        n -= 0x10000
        result += chr(0xD800 | (n >> 10)) + chr(0xDC00 | (n & 0x3FF))
    else:
        result += f'dec2char error: Code point out of range: {dec2hex(n)}'
    return result


def convert_dec_ncr_to_char(str):
    str = re.sub(r'&#([0-9]{1,7});', lambda x: dec2char(int(x.group(1))), str)
    return str


def insert_keyword(filename, keyword):
    print(keyword, convert_dec_ncr_to_char(keyword))
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{convert_dec_ncr_to_char(keyword)}\n')
        f.close()


def get_keyword(html):
    bs = BeautifulSoup(html, 'html.parser')
    try:
        keyword = bs.select_one('meta[name=keywords i]')
        key = keyword.attrs['content']

        if key:
            insert_keyword('keyword.txt', key)
    except:
        pass


def get_url(url, user_agent=None):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }
        if user_agent:
            headers['User-Agent'] = user_agent
        resp = request("GET", url, headers=headers, timeout=15)
        resp.encoding = 'utf-8'
        print(url, resp.status_code)
        if resp.status_code == 200:
            get_keyword(resp.text)
    except Exception as e:
        print('An exception occurred: ', e)
        pass


def _generate_random(count=9):
    return ''.join(random.choice(string.ascii_lowercase + string.digits)
                   for _ in range(count))


def _generate_random_number(count=9):
    return ''.join(random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
                   for _ in range(count))


urls = [
    'dongxintieta.com'
]
with ThreadPoolExecutor(40) as ex:
    while True:
        base_url = random.choice(urls)
        subdomain = _generate_random(random.randrange(2, 3))
        path = _generate_random(9)
        lala = "www.quanxingshengtai.com"
        # random_date = f"{random.randrange(2020, 2023)}0{random.randrange(1, 9)}"

        for i in range(7000001,7015033):
            ex.submit(get_url, f"https://{lala}/n/n{i}.html")
