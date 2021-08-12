# Average Word Length

"""
Given a sentence as input, calculate and output the
average word length of that sentance.
To calculate the average word length, you need to
divide the sum of all word lengths by the number
of words in the sentence.
"""

sentence = input("Enter sentence: ")

total_letters = len(sentence) - sentence.count(" ")

print("Sentence:", sentence)
print("Total Letters in Sentence:", total_letters)

word_list = sentence.split(" ")

word_list_len = len(word_list)

print("Word list:", word_list)
print("Word list length:", word_list_len)

avg_word_len = total_letters / word_list_len

print("Average Word length:", avg_word_len)
