

# List functions and methods
# Define the lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "apple", 3.14, True]

# Length of lists
print("Length of numbers:", len(numbers))
print("Length of fruits:", len(fruits))
print("Length of mixed_list:", len(mixed_list))

# Sum, min, max (only for numbers)
print("Sum of numbers:", sum(numbers))
print("Min of numbers:", min(numbers))
print("Max of numbers:", max(numbers))

# Append elements
numbers.append(6)
print("Numbers after append:", numbers)

# Insert element
fruits.insert(1, "orange")
print("Fruits after insert:", fruits)

# Remove element
fruits.remove("banana")
print("Fruits after remove:", fruits)

# Pop element
popped = numbers.pop()
print("Popped from numbers:", popped)
print("Numbers after pop:", numbers)

# Sort and reverse
numbers.sort()
print("Numbers after sort:", numbers)
numbers.reverse()
print("Numbers after reverse:", numbers)

# Index and count
print("Index of 'apple' in fruits:", fruits.index("apple"))
print("Count of 1 in mixed_list:", mixed_list.count(1))
