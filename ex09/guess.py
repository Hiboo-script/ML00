import random

win_number = random.randint(1,99)

presentation_game = """ """
invite_text = 'What\'s your Guess between 1 and 99 ?\n>> '
entry_42 = ''

print('presentation game')
try_number = input(invite_text)
number_try = 1

while try_number!='exit':
	try:
		try_number = int(try_number)
		if (try_number == win_number):
			if (win_number == 42):
				print(entry_42)
			print('Congratulation you win in {} attemp(s) !'.format(number_try))
			print('###### NEW GAME !')
			win_number = random.randint(0,99)
		elif (try_number > win_number):
			print('Too high !')
		elif (try_number < win_number):
			print('Too low')
	except:
		print('It\'s not a number !')
	try_number = input(invite_text)
	number_try += 1
print('Goodbye!')
