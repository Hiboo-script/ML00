transcripter = {
	" " : "/",
	"A" : ".-",
	"B" : "-...",
	"C" : "-.-.",
	"D" : "-..",
	"E" : ".",
	"F" : "..-.",
	"G" : "--.",
	"H" : "....",
	"I" : "..",
	"J" : ".---",
	"K" : "-.-",
	"L" : ".-..",
	"M" : "--",
	"N" : "-.",
	"O" : "---",
	"P" : ".--.",
	"Q" : "--.-",
	"R" : ".-.",
	"S" : "...",
	"T" : "-",
	"U" : "..-",
	"V" : "...-",
	"W" : ".--",
	"X" : "-..-",
	"Y" : "-.--",
	"Z" : "--..",
	"0" : "-----",
	"1" : ".----",
	"2" : "..---",
	"3" : "...--",
	"4" : "....-",
	"5" : ".....",
	"6" : "-....",
	"7" : "--...",
	"8" : "---..",
	"9" : "----."
}

def traduction(message,transcripter):
	try:	
		upper_message = message.upper()
		transcripted_message = ''
		for c in upper_message:
			transcripted_message += transcripter[c] + ' '
		return transcripted_message[:len(transcripted_message)-1]
	except:
		return 'ERROR'	

if __name__=="__main__":
	
	import sys
	if len(sys.argv)>1:
		message = ''
		for w in sys.argv[1:]:
			message+=w+' '
		message=message[:len(message)-1]
		print(traduction(message,transcripter))
