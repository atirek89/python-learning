# You need to make a program that counts the number of vowels in a given text.
# The vowels are a, e, i, o, and u.

# Given text
text = "Given text"
text = "The vowels are a, e, i, o, and u."

# Vowels
vowels = ["a", "e", "i", "o", "u"]

# Counter
count = 0

for item in text:
    if item in vowels:
       count += 1

print("Vowels in " + text + " are:", count)
