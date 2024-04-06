import string

def analyzer_prompt(u,l,p,s):
	print("- "+str(u)+" upper letter(s)")
	print("- "+str(l)+" lower letter(s)")
	print("- "+str(p)+" punctuation mark(s)")
	print("- "+str(s)+" space(s)")

def text_analyzer(text = ""):
	"""
	This function counts the number of upper characters, 
	lower characters, punctuation and spaces in a given text.
	"""
	if(type(text)!=type("s")):
		print("insertionError : the argument is not a string.")
		return None
	elif (len(text)==0): 
		text = input("What is the text to analize?\n>> ")
	
	up = 0
	lo = 0
	pu = 0
	sp = 0
	for c in text:
		if (c.isupper()):
			up+=1
		elif (c.islower()):
			lo+=1
		elif (c in string.punctuation):
			pu+=1
		elif (c==" "):
			sp+=1
	analyzer_prompt(up,lo,pu,sp)
