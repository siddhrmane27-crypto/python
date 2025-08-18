per=int(input("enter the percentage of students="))

if per > 100 or per < 0:
	print("Invalid Percentage")

elif  per >= 90:
	print("Exellent Performance")

elif per >= 80:
	print("very Good Performance")
elif per >= 70:


	print("Good Performance")
elif per >= 60:
	print("average Performance")
elif per >= 50:
	print("poor Performance")

else:

 print("Fail")
