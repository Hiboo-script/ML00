import sys

arg = sys.argv
n_arg = len(arg)
globalError = """syntaxError : python operations.py <number 1> <number 2>
Example:
	python operations.py 10 3"""
err_modZero = "Remainder : ERROR (modulo by zero)"
err_divZero = "Quotient ; ERROR (division by zero)"

def operations(A,B):
	print("Sum : " + str(A+B))
	print("Difference : " + str(A-B))
	print("Product : " + str(A*B))
	if (B==0):
		print(err_divZero)
		print(err_modZero)
	else:
		print("Quotient : " + str(A/B))
		print("Remainder : " + str(A%B))


if (n_arg==1):
	0
elif (n_arg==2) or (n_arg>3):
	print(globalError)
else:
	try:
		a = int(arg[1])
		b = int(arg[2])
		
		operations(a,b)
	except:
		print(globalError)

# operations(5,10)
# operations(3,0)
# operations(7,-8)
