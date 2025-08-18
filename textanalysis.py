text = input("Enter a paragraph: ")

# Convert to lowercase for consistency
text = text.lower()

# Remove punctuation (simple version)
for ch in ",.!?;:":
    text = text.replace(ch, "")

# Split into words
words = text.split()

# 1. Total number of words
print("Total number of words:", len(words))

# 2. Frequency of each word
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequencies:")
for word in freq:
    print(word, ":", freq[word])

# 3. Top 3 most frequent words
top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 most frequent words:")
for word, count in top_words:
    print(word, ":", count)

# 4. Count vowels
vowels = "aeiou"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

print("\nTotal number of vowels:", vowel_count)
