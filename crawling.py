from datetime import datetime

def run(url) :
    url = 'https://news.naver.com/main/main.naver'
    today = datetime.today().strftime("%Y_%m_%d")
    params = {'mode' : 'LSD', 'mid' : 'shm'}
    category = {'sid1' : '101'}
    # params2 = {'date' :f'%{today}', 'page' : 1}
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

    params.update(category)
    # params.update(params2)
    res = requests.get(url, params=params, headers=headers)

    # beutifulsoup 4는 html을 파싱 가능한 형태로 만들어주는 객체
    soup = BeautifulSoup(res.text, 'html.parser')
    t = soup.find('td', {'class' :'content'})
    textlist = t.findAll('a', {'class' : "cluster_text_headline nclicks(cls_eco.clsart)"})
    news = []
    for text in textlist :
        news.append(text.attrs['href'] + '\n' + text.text + '\n\n')

    with open(myfolder + '\\' + today + '_news.txt', 'w', encoding='utf-8-sig') as f:
        f.writelines(news)

if __name__ == "__main__":
    run()