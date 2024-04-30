import time
import sys

def hide_c():
	sys.stdout.write("\033[?25l")
	sys.stdout.flush()
def show_c():
	sys.stdout.write("\033[?25h")
	sys.stdout.flush()

class ft_progress:
	def __init__(self,lst):
		self.lst = lst
		self.lim = len(lst)
		self.n = 0
		self.pourcent = 0 		
	
	def __iter__(self):
		self.a = self.lst[0]
		hide_c()
		return self
	def __next__(self):
		if self.n < self.lim:
			x = self.lst[self.n]
			print(' [{:0=5.2f}%]'.format(self.actual_pourcent()), end="\r")
			self.n += 1
			return x
		else:
			show_c()
			raise StopIteration

	def actual_pourcent(self):
		return ((self.n*1.)/self.lim)*100
	
listy = range(1000)
ret = 0

for x in ft_progress(listy):
	ret += (x+3)%5
	time.sleep(0.01)
print()
print(ret)
