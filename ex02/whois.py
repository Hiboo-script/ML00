#!/Users/porcedduvalentin/miniconda3/envs/42AI-porcedduvalentin/bin python
import sys
n = 0
arg = sys.argv
if (len(arg)==2):
	try:
		number = int(arg[1])
		print('good')
	except:
		print('error 2')
elif (len(arg)==1):
	0
else:
	print('error')
