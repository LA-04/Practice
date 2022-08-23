from pyeda.inter import *

def minimize(n,func):
	X = ttvars('x', n)
	#func = list(bin(53)[2:].zfill(2**n))
	#print(func)
	str_func = ''.join(func)
	#print(str_func)
	print(X)
	f1 = truthtable(X, str_func)
	print(f1)
	f2 = truthtable(X, str_func)
	f1m, f2m = espresso_tts(f1, f2)
	print(f1m)
	return f1m

n = 3
func = list(bin(53)[2:].zfill(2**n))

minimize(n,func)