import time
import sys
import os

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_c():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def show_c():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()


class ft_progress:
	def __init__(self,lst):
		self.lst = lst
		self.lim = len(lst)
		self.n = 1
		self.pourcent = 0 		
	
	def __iter__(self):
		self.a = self.lst[0]
		self.init_time = time.time()
		hide_c()
		return self
	def __next__(self):
		if self.n <= self.lim:
			self.actual_time = time.time()
			x = self.lst[self.n-1]
			dt_time = self.actual_time-self.init_time
			es_time = (self.lim/self.n)*dt_time
			n_bar = int(self.n*(30./self.lim))
			print('ETA : {:0=4.2f}s [{:0=5.2f}%] [{}>{}] {}/{} | elapsed time : {:0=4.2f}s'.format(es_time,self.actual_pourcent(),'='*n_bar,' '*(30-n_bar), self.n, self.lim, dt_time), end="\r")
			self.n += 1
			return x
		else:
			show_c()
			print()
			print('...',end="\r")
			raise StopIteration

	def actual_pourcent(self):
		return ((self.n*1.)/self.lim)*100

listy = range(500)
ret = 0

for x in ft_progress(listy):
	ret += x
	time.sleep(0.005)
print()
print(ret)
