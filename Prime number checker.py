##Prime number checker
z = "yes"
lst = []
while z == "yes":
	x = int(input("Enter a whole number please: "))
	a = int(x/2) or int(x/2+0.5)
	y = range(2, a+1)
	for elem in y:
		if x/elem == int(x/elem):
			print("This is not a prime number")
			lst.append(elem)
			print(lst)
			lst.clear()
			z = input("Restart the sequence?(yes or no): ")
			if z == "no":
				exit()
			break
		if elem == a:
			print("This is a prime number")
			z = input("Restart the sequence?(yes or no): ")
			if z == "no":
				exit()
		##else:
			##elem += 1
			##lst.append(
			##if elem == x:
			##	if lst == [1, x]:
			##		print("This is a prime number")
			##		z = input("Restart the sequence?(yes or no): ")
			##		lst.clear()
			##	else:
			##		print("This is not a prime number")
			##		z = input("Restart the sequence?(yes or no): ")
			##		lst.clear()