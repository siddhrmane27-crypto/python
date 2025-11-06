import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if root * root == num and is_prime(root):
    print("Square root is prime")
else:
    print("Square root is not prime")