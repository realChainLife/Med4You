from bot import remedies
from pprint import pprint
import json

c=remedies()

def remedies(desc):
	all_matches = c.matches()
	for match in all_matches:
		if match['mchdesc'].title() == desc:
			return match['id']
	else:
		return None


def get_remedies():
	match_data = c.matches()
	matches = []
	for match in match_data:
		matches.append(match['mchdesc'])
	return matches


def commentary(desc):
	mid = match_id(desc)
	data = c.commentary(mid)
	comm ={}
	comm['matchinfo'] = "{}, {}".format(data['matchinfo']['mnum'],data['matchinfo']['mchdesc'])
	comm['status'] = "{}, {}".format(data['matchinfo']['mchstate'].title(),data['matchinfo']['status'])
	comm['commentary'] = data['commentary']
	text =''
	text += comm['matchinfo'] + '\n' + comm['status'] + '\n\n'
	for com in comm['commentary']:
		text += "{}\n\n".format(com)

	return text


def main():
	matches = all_matches()
	print("\nALL MATCHES\n")
	for i,m in enumerate(matches,1):
		print("{}. {}".format(str(i),m))
	choice = int(input('\nEnter choice (number): '))
	while choice <1 or choice > len(matches):
		print('\nWrong choice')
		choice = int(input('\nEnter choice again: '))

	desc = matches[choice-1].title()
	print('\n')
	print('1. Live Score')
	print('2. Full Score Card')
	print('3. Commentary')
	choice = int(input('\nEnter choice (number): '))
	while choice <1 or choice > 3:
		print('\nWrong choice')
		choice = int(input('\nEnter choice again: '))
	print('\n')
	if choice ==1:
		ref = 'y'
		while ref =='y':
			print(live_score(desc))
			ref = input('\n\nDo you want to refresh:(y/n) ')
			print('\n')

	elif choice ==2:
		ref = 'y'
		while ref =='y':
			print(scorecard(desc))
			ref = input('\n\nDo you want to refresh:(y/n) ')
			print('\n')

	else:
		ref = 'y'
		while ref =='y':
			print(commentary(desc))
			ref = input('\n\nDo you want to refresh:(y/n) ')
			print('\n')



if __name__ == '__main__':
 	main()
