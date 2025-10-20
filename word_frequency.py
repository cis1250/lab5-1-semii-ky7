#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


def get_sentence():
    
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        else:
            print("Please enter a valid sentence (start with a capital and end with ., !, or ?).")


def calculate_frequencies(sentence):
    
    # Remove the ending punctuation (.!?)
    sentence = sentence[:-1]

    # Split the sentence into words
    words_in_sentence = sentence.split()

    # Create empty lists
    words = []
    frequencies = []

    # Count word frequencies
    for word in words_in_sentence:
        word = word.lower()  # make all words lowercase
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)

    return words, frequencies


def print_frequencies(words, frequencies):
    
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(words[i], ":", frequencies[i])


def main():
   
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)


# Only run main if this file is executed directly
if __name__ == "__main__":
    main()
