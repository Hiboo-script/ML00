import time
import os

def progress(lst):
	print('L ')
	return lst

for i in range(20):
	print('waaaaaaaaa')
	print(i)
	time.sleep(0.1)
	os.system('cls' if os.name == 'nt' else "printf '\033c'")

print('salut')
