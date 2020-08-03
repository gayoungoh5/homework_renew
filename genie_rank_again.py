import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div > div > table > tbody > tr')

for music in musics:
    rank_select = music.select_one('td.number').text[0:2].strip()
    # text[m:n]의 의미는 m번째 자리부터 n개를 추출한다는 의미로 이해했음.
    title_select = music.select_one('td.info > a.title').text.strip()
    artist_select = music.select_one('td.info > a.artist').text
    print(rank_select,title_select,artist_select)
    db.musicchart.insert_one({'rank':rank_select,'title':title_select,'artist':artist_select})