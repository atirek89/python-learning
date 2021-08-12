# Letter Frequency
"""
You are making a program to analyze text.
Take the text as the first input and a letter as the
second input, and output the frequency of that letter
in the text as a whole percentage
"""

text = input("Enter text: ")
letter = input("Enter letter: ")

len_text = len(text)
count_letter = text.count(letter)

percent_frequency = (count_letter/len_text) * 100

print("Letter Frequency Percentage is:", int(percent_frequency))
