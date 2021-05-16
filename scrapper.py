import urllib3
from bs4 import BeautifulSoup as bs4

class Main:
    def build():
        url = 'https://www.fandango.com/'
        elements = Scrapper.scrapping(url)
        data = []
        for element in elements:
            data.append(element)
        return data

class Scrapper:
    def scrapping(url):
        http = urllib3.PoolManager()
        html = http.request('GET',url)

        soup = bs4(html.data,'html.parser')
        element = []
        elements = soup.find_all('a', class_='js-movie-link heading-style-1 heading-size-s heading__movie-carousel')
        for data in elements:
            element.append(data.text)
        return element

