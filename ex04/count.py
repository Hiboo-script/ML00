import string

def analyzer_prompt(uppercase_letters,lowercase_letters,punctuation_marks,spaces):
	print(f"- {uppercase_letters} upper letter(s)")
	print(f"- {lowercase_letters} lower letter(s)")
	print(f"- {punctuation_marks} punctuation mark(s)")
	print(f"- {spaces} space(s)")

def text_analyzer(text = ""):
	"""
	This function counts the number of upper characters, 
	lower characters, punctuation and spaces in a given text.
	"""
	insertionError = "insertionError : the argument is not a string."
	if not isinstance(text,str):
		print(insertionError)
		return None
	elif not text: 
		text = input("What is the text to analize?\n>> ")
	
	uppercase_letters = 0
	lowercase_letters = 0
	punctuation_marks = 0
	spaces = 0
	for char in text:
		if char.isalpha():
			if (char.isupper()):
				uppercase_letters+=1
			elif (char.islower()):
				lowercase_letters+=1
		elif char in string.punctuation:
			punctuation_marks+=1
		elif char.isspace():
			spaces+=1
	analyzer_prompt(uppercase_letters,lowercase_letters,punctuation_marks,spaces)

usingError = """
usingError (too much argument) : python count.py <string>
"""

if __name__=="__main__":
	import sys

	if len(sys.argv)>2:
		print(usingError)
	elif (len(sys.argv)==2):
		text_analyzer(sys.argv[1])
