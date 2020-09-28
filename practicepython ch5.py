import random
z = 1
v = []
w = []
start = 1
while True:
	if not start == 1:	
		u = input("Restart? y/n: ")
		if u == "y":
			z = 1
			pass
		elif u == "n":
			break
		else:
			print("unknown input")
			break
	if start == 1:
		start = 0
	while z < 20:
		z = random.randint(1, 25)
		x = random.randint(1, 100)
		y = random.randint(1, 100)
		v.append(x)
		w.append(y)
	print(v)
	print(w)
	lst = []
	for elem in v:
		if elem in w:
			if elem not in lst:
				lst.append(elem)
	v.clear()
	w.clear()
	print (lst)
	lst.clear()
