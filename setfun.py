fruits={"banana", "apple", "cherry", "mango", "orange","potato"}
# Display the set
print("Fruits Set:", fruits)

#function on set
# Adding an element
fruits.add("kiwi")
print("Fruits Set after adding kiwi:", fruits)

# Removing an element
fruits.remove("banana")
print("Fruits Set after removing banana:", fruits)

# Discarding an element
fruits.discard("apple")
print("Fruits Set after discarding apple:", fruits)

# Popping an element
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("Fruits Set after popping an element:", fruits)

# Checking membership
print("Is 'cherry' in fruits?", "cherry" in fruits)

# Length of the set
print("Length of fruits set:", len(fruits))

#union of sets
vegetables = {"carrot", "potato", "tomato", "cabbage", "spinach"}
print("Vegetables Set:", vegetables)
# Union of two sets
combined_set = fruits.union(vegetables)
print("Combined Set (Fruits ∪ Vegetables):", combined_set)  

# Intersection of two sets
intersection_set = fruits.intersection(vegetables)
print("Intersection Set (Fruits ∩ Vegetables):", intersection_set)