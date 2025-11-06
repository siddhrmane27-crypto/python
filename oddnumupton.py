n=int(input("Enter an even number up to which you want to print: "))
print("The even numbers are: ")
for i in range(1, n + 1, 2):
    print(i, end=' ')