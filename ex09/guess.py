import random

win_number = random.randint(1,99)

presentation_game = """This is an interactive guessing game !
You have to enter a number between 1 and 99 to find the secret number.
type 'exit' to end the game.
good luck!\n"""
invite_text = 'What\'s your Guess between 1 and 99 ?\n>> '
entry_42 = 'The answer to the ultimate question of life, the universe and everything is 42.'

print(presentation_game)
try_number = input(invite_text)
number_try = 1

while try_number!='exit':
	try:
		try_number = int(try_number)
		if (try_number == win_number):
			if (win_number == 42):
				print(entry_42)
			if (number_try==1):
				print('Congratulation! You got it in your first try!')
			else:
				print('Congratulation you win in {} attemp(s) !\n'.format(number_try))
			print('###### NEW GAME ! ########\n')
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
