def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def compute_series(n):
    result = 1.0  # Start with 1 (i.e., 1/0!)
    for i in range(1, n + 1):
        result += 1 / factorial(i)
    return result

# Input
n = int(input("Enter the value of n: "))
series_sum = compute_series(n)
print(f"The sum of the series up to 1/{n}! is: {series_sum}")
