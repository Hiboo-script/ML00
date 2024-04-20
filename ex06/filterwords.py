import string
import sys

try:
	if len(sys.argv)>3:
		print("ERROR")
	else:
		str_arg = sys.argv[1].translate({ord(c):None for c in string.punctuation})
		int_arg = int(sys.argv[2])

		list_result = [word for word in str_arg.split(" ") if len(word)>=int_arg]
		print(list_result)
except:
	print("ERROR")
