def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n = int(input("Enter the value of n: "))

sum = 0.0
for i in range(0, n + 1):
    sum += 1 / factorial(i)

print("Sum of the sequence is:", sum)
