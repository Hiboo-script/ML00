#!/Users/porcedduvalentin/miniconda3/envs/42AI-porcedduvalentin/bin python
import sys

arg = sys.argv
if (len(arg)==2):
	if (type(arg[1])==type(1)):
		print('good')
	else:
		print('error 2')
elif (len(arg)==1):
	0
else:
	print('error')
