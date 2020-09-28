print ("Welcome to the random questions quiz")
print ("Ready for the first question?")
y = input ("Yes or no: ")
if y == "Yes" or y == "yes":
	print ("Great! Let's start with the first question!")
	print ("What is 2 + 2?")
	f = input ("Answer here please: ")
	if f == "4":
		print ("That's correct!")
		t = print ("Let's continue! \n What is the tallest mountain on land?")
		f = input ("Answer here please: ")
		if f == "Mount Everest" or f == "mount everest":
			print ("Great job!")
	else:
		print ("That's incorrect :(")
		print (t)
		f = input ("Answer here please: ")
		if f == "Mount Everest" or f == "mount everest":
			print ("Good!")
elif y == "no" or y == "No":
	exit()