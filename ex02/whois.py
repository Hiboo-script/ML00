#!/Users/porcedduvalentin/miniconda3/envs/42AI-porcedduvalentin/bin python
import sys
n = 0
zero = 'I\'m zero.'
even = 'I\'m Even.'
odd = 'I\'m Odd.'
noInt = 'AssertionError : argument is not an integer'
tooMuchArg = 'AssertionError : more than one argument are provided'
arg = sys.argv
if (len(arg)==2):
	try:
		n = int(arg[1])
		if (n == 0):
			print(zero)
		elif (n%2==0):
			print(even)
		else:
			print(odd)
	except:
		print(noInt)
elif (len(arg)==1):
	0
else:
	print(tooMuchArg)
