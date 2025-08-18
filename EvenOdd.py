n=int(input("Enter a number: "))

print("even numbers")
for i in range(1 ,n+1):
	if i%2==0:
		print(i, end=" ")

print("\nodd numbers")		
for i in range(1 ,n+1):
	if i%2==1:
	 print(i,end=" ")