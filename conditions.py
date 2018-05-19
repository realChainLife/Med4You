from bot import conditions
import requests


def get_conditions():
	url='https://www.nhs.uk/conditions/Pages/hub.aspx'
	res=requests.get(url)
	
	while(res.status_code!=200):
		try:
			res=requests.get('url')
		except:
			pass

	conditions=Conditions(res.text,'lxml')
	short_list=conditions.find('ul',{'class':'topstr-list gap topmarging'}).find_all('a')
	long_list=conditions.find_all('div',{'class':'innerbox'})

	return (short_list,long_list)

def short_list():
	return(get_list()[0])

def long_list():
	return(get_list()[1])