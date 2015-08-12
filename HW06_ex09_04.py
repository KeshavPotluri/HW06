#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body

def uses_only(word, useCases):
	usesOnly = True
	for letter in word:
		if useCases.lower().find(letter.lower())<0:
			usesOnly = False
	return usesOnly

def words_with_acefhlo():
	fin = open("words.txt", "r")
	for line in fin:
		line = line.strip()
		if uses_only(line, "acefhlo") == True:
			print line


##############################################################################
def main():
	words_with_acefhlo()  # Call your function(s) here.

if __name__ == '__main__':
    main()
