from bot import remedies
from pprint import pprint
import json

c=remedies()

def remedies(desc):
	all_matches = c.remedies()
	for match in all_matches:
		if match['mchdesc'].title() == desc:
			return match['id']
	else:
		return None


def get_remedies():
	remedies_data = c.remedies()
	remedies = []
	for remedies in remedies_data:
		remedies.append(remedies['mchdesc'])
	return remedies


def main():
	remedies = all_remedies()
	print("\nALL REMEDIES\n")
	for i,m in enumerate(remedies,1):
		print("{}. {}".format(str(i),m))
	choice = int(input('\nEnter choice (number): '))
	while choice <1 or choice > len(remedies):
		print('\nWrong choice')
		choice = int(input('\nEnter choice again: '))

	desc = remedies[choice-1].title()
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
