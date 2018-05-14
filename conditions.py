<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests


def get_news():
	url='https://www.nhs.uk/conditions/Pages/hub.aspx'
	res=requests.get(url)
	
	while(res.status_code!=200):
		try:
			res=requests.get('url')
		except:
			pass

	soup=BeautifulSoup(res.text,'lxml')
	short_news=soup.find('ul',{'class':'topstr-list gap topmarging'}).find_all('a')
	long_news=soup.find_all('div',{'class':'innerbox'})

	return (short_news,long_news)

def short_news():
	return(get_news()[0])

def long_news():
=======
from bs4 import BeautifulSoup
import requests


def get_news():
	url='https://www.nhs.uk/conditions/Pages/hub.aspx'
	res=requests.get(url)
	
	while(res.status_code!=200):
		try:
			res=requests.get('url')
		except:
			pass

	soup=BeautifulSoup(res.text,'lxml')
	short_news=soup.find('ul',{'class':'topstr-list gap topmarging'}).find_all('a')
	long_news=soup.find_all('div',{'class':'innerbox'})

	return (short_news,long_news)

def short_news():
	return(get_news()[0])

def long_news():
>>>>>>> f364c26d3d69a200eac51ead609856c10b1ce4e4
	return(get_news()[1])