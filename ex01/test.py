import sys

s = ''
for w in sys.argv[1:]:
	s += w + ' '
s = s[:len(s)-1]

print(s) if len(s)>0 else 0
