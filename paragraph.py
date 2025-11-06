text = input("Enter a paragraph: ")

text_lower = text.lower()
words = text_lower.split()
total_words = len(words)

word_count = {}
for word in words:
    word = word.strip('.,!?')
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

top_3 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]

vowels = 'aeiou'
vowel_count = sum(1 for char in text_lower if char in vowels)

print("\nTotal number of words:", total_words)

print("\nFrequency of each word:")
for word, count in word_count.items():
    print(f"{word}: {count}")

print("\nTop 3 most frequent words:")
for word, count in top_3:
    print(f"{word}: {count}")

print("\nTotal number of vowels:", vowel_count)
