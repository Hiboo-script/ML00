def progress(lst):
	n = 0
	lim = len(lst) - 1
	def __iter__(self,lst):
		self.a = lst[0]
		return self
	def __next__(self,lst):
		if self.n<=self.lim:
			x = lst[self.n]
			print(x)
			self.n += 1
			return x
		else:
			raise StopeIterator

for x in progress(range(20)):
	print(x)		
