import time
import sys
class progress:
	def __init__(self,lst):
		self.lst = lst
		self.n = 0
		self.limit = len(lst)-1
	def __iter__(self):
		self.a = self.lst[0]
		return self
	def __next__(self):
		if self.n<=self.limit:
			x = self.lst[self.n]
			sys.stdout.write('{}/{}'.format(self.n,self.limit))
			time.sleep(0.1)
			sys.stdout.flush()
			self.n += 1
			return x
		else:
			raise StopIteration

for x in progress(range(20)):
	print(x)
