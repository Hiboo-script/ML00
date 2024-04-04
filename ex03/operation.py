def operations(A,B):
	print("Sum : " + str(A+B))
	print("Difference : " + str(A-B))
	print("Product : " + str(A*B))
	if (B==0):
		print("Quotient ; ERROR (division by zero)" )
		print("Remainder : ERROR (modulo by zero)")
	else:
		print("Quotient : " + str(A/B))
		print("Remainder : " + str(A%B))

operations(5,10)
operations(3,0)
operations(7,-8)
