x = int(input("Write a number please: "))
y = list(range(1, x+1))
lst = []
for elem in y:
 if x/elem == int(x/elem):
 	lst.append(elem)
 if elem == x:
 	print(lst)