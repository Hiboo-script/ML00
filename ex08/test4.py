import time

for x in range(20):
	bar = ' {}/20:[{}>{}] ...progress'.format(x+1,'='*x,' '*(19-x))
	print(bar, end="\r")
	time.sleep(0.1)
print()
