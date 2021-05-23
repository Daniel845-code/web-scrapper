import urllib3
from bs4 import BeautifulSoup as bs4


class Scrapper:
	def __init__(self):
		self.query = input('movie name: ')
		url = 'https://www.google.com/search?hl=pt-BR&source=hp&biw=&bih=&q='+self.query+'+sinopse&btnG=Pesquisa+Google&iflsig=AINFCbYAAAAAYKrTabDwf_fFyV-nlvd8i9CD3mw62RnD&gbv=1'

		self.test_scrapper(url)

	def test_scrapper(self,url):
		http = urllib3.PoolManager()
		html = http.request('GET',url)
	
		soup = bs4(html.data,'html.parser')
		element = soup.find_all('div',class_='BNeawe tAd8D AP7Wnd')

		text = self.query+'\n'+element[0].text

		data = open(self.query+'.txt','w')
		data.write(text)

		print(text)
try:
	Scrapper()
except:
	print('A error occurred, please verify the name of movie and try again.')
