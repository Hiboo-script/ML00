import sys
s = ''
for w in sys.argv[1:]:
	s += w + ' '
s = s[:len(s)-1]

f_s = ''
for c in s:
	f_s = c + f_s

print(f_s.swapcase()) if len(f_s)>0 else 0
