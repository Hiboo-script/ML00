import string

def analyzer_prompt(u,l,p,s):
	print("- "+str(u)+" upper letter(s)")
	print("- "+str(l)+" lower letter(s)")
	print("- "+str(p)+" punctuation mark(s)")
	print("- "+str(s)+" space(s)")

def text_analyzer(text):
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
