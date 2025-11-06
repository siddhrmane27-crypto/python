a=input("Enter a charctaer").lower()
if a in 'aeiou':
    print(a, "is a vowel")
elif a.isalpha():
    print(a, "is a consonant")
else:
    print("Invalid input")
