from pprint import pprint
import requests
import json
from time import sleep
from conditions import *
from remedies import *

token = 'your access token'
url = 'https://api.telegram.org/bot{}/'.format(token)


def getme():
	res=requests.get(url+"getme")
	d = res.json()
	username = d['result']['username']


def get_updates(offset = None):
	while True:
		try:
			URL = url + 'getUpdates'
			if offset:
				URL += '?offset={}'.format(offset) 

			res = requests.get(URL)
			while (res.status_code !=200 or len(res.json()['result'])== 0):
				sleep(1)
				res = requests.get(URL)
			print(res.url)
			return res.json()
		
		except:
			pass;

	
def ask_conditions(chat_id):
	print('Ask conditions')
	text ='Send conditions'
	keyboard = [[{"text":"conditions","request_conditions":True}]]
	reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
	send_message(chat_id,text,json.dumps(reply_markup))


def ask_remedies(chat_id):
	print('Ask remedies')
	text ='Send remedies'
	keyboard = [[{"text":"remedies","request_remedies":True}]]
	reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
	send_message(chat_id,text,json.dumps(reply_markup))


def get_remedies(update_id):
	print('Get remedies')
	updates = get_updates(update_id+1)
	remedies = get_last(updates)['message']['remedies']
	chat_id,text,update_id = get_last_id_text(updates)
	return lat,lon,update_id


def conditions(chat_id,update_id):

	message = 'Select'
	commands =['Short List','Long List']
	reply_markup = reply_markup_maker(commands)
	send_message(chat_id,message,reply_markup)
	chat_id,text,update_id= get_last_id_text(get_updates(update_id+1))	

	while text.lower() == 'list':
		chat_id,text,update_id= get_last_id_text(get_updates(update_id+1))	
		sleep(0.5)
	print(text)

	if text.lower() == 'short list':
		message= ''
		list = short_list()
		for i,n in enumerate(list,1):
			message += str(i) + ". " + n.text + '\n\n'
		send_message(chat_id,message)

	elif text.lower() == 'long list':
		message= ''
		list = long_list()
		for i,n in enumerate(list[:10],1):
			message += str(i) + ". " + n.text + '\n\n'
		send_message(chat_id,message)

def remedies(chat_id,update_id):
	message = 'Select'
	commands = all_remedies()
	reply_markup = reply_markup_maker(commands)
	send_message(chat_id,message,reply_markup)
	chat_id,desc,update_id= get_last_id_text(get_updates(update_id+1))
	print(desc)

	commands =['Index','Common','Guide']
	reply_markup = reply_markup_maker(commands)
	send_message(chat_id,message,reply_markup)
	chat_id,text,update_id= get_last_id_text(get_updates(update_id+1))	
	print(text)	

	if text.lower()=='index':
		text = index(desc)
		send_message(chat_id,text)

	elif text.lower() == 'common':
		text = common(desc)
		print(text)
		send_message(chat_id,text)

	elif text.lower() == 'guide':
		text = commentary(desc)
		send_message(chat_id,text)


def welcome_note(chat_id, commands):
	text = "Bot Welcomes You"
	send_message(chat_id,text)
	text = 'Select'
	reply_markup = reply_markup_maker(commands)
	send_message(chat_id,text,reply_markup)


def start(chat_id):
	message = 'Wanna Start'	
	reply_markup = reply_markup_maker(['Start'])
	send_message(chat_id,message,reply_markup)
	
	chat_id,text,update_id= get_last_id_text(get_updates())	
	while(text.lower() != 'start'):
		chat_id,text,update_id= get_last_id_text(get_updates(update_id+1))	
		sleep(0.5)

	return chat_id,text,update_id


def end(chat_id,text,update_id):
	message = 'Do you wanna end?'
	reply_markup = reply_markup_maker(['Yes','No'])
	send_message(chat_id,message,reply_markup)
	
	new_text =text
	while(text == new_text):
		chat_id,new_text,update_id= get_last_id_text(get_updates(update_id+1))	
		sleep(1)

	if new_text =='Yes':
		return 'y'
	else:
		return 'n'


def menu(chat_id,text,update_id):

	commands = ['conditions','remedies']
	welcome_note(chat_id, commands)
	
	while( text.lower() =='start'):
		chat_id,text,update_id= get_last_id_text(get_updates(update_id+1))	
		sleep(0.5)
	print(text)
	while text.lower() not in commands:
		chat_id,text,update_id= get_last_id_text(get_updates(update_id+1))	
		sleep(0.5)

	if text.lower()=='conditions':
		list(chat_id,update_id)

	elif text.lower()=='remedies':
		saavn(chat_id,update_id)


def main():
	text= ''
	chat_id,text,update_id= get_last_id_text(get_updates())	
	chat_id, text,update_id = start(chat_id)
	print('Started')
	
	while text.lower() != 'y':
		sleep(1)
		text = 'start'
		menu(chat_id,text,update_id)
		text ='y'
	
		chat_id,text,update_id= get_last_id_text(get_updates())	
		text = end(chat_id,text,update_id)
	

if __name__ == '__main__':
	main()
