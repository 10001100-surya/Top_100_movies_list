import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

request = requests.get(url=URL)
website_html = request.text

soup = BeautifulSoup(website_html, "html.parser")
movies_title_detail = soup.find_all(name='h3', class_ = "listicleItem_listicle-item__title__BfenH")
movies_list = [movie.getText() for movie in movies_title_detail]
movies = movies_list[::-1]

with open("movies.txt", mode= "w", encoding='utf-8') as file:

    for _ in movies:
        file.write(f"{_}\n")
