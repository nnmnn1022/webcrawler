from datetime import datetime
import bs4, re
import requests
from bs4 import BeautifulSoup

def run(word) :
    url = 'https://www.google.com/search'
    params = {'q' : word}
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

    res = requests.get(url, params=params, headers=headers)

    # beutifulsoup 4는 html을 파싱 가능한 형태로 만들어주는 객체
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.find('div', {'id' :'res'})
    data = []
    for link in text.find_all('a') :
        data.append(link.get_text())
        data.append(link.get('href'))

    return data

if __name__ == "__main__":
    run('바보')