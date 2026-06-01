score = int(input("Enter your score: "))
if score == 100:
	print ("Excellent you are successful")
elif score >=90 and score <=99:
	print ("Very Good you are successful")
elif score >=70 and score <90:
	print ("Good you are successful")
elif score >=50 and score <70:
	print ("Acceptable you are successful")
elif score <50:
	print ("You fail")
else:
	print ("An error occurred, make sure the result is entered correctly.")
