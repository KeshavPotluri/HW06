#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body

def is_abecedarian(word):
	isAbecedarian = True
	currentAscii = 0
	previousAscii = 0
	for letter in word:
		currentAscii = ord(letter.lower())
		if currentAscii < previousAscii:
			isAbecedarian = False
		previousAscii = currentAscii
	return isAbecedarian

def words_abecedarian():
	fin = open("words.txt", "r")
	count = 0
	for line in fin:
		if is_abecedarian(line) == True:
			count+=1
			print line
	print "The number of words that are abecedarian: " + str(count)


##############################################################################
def main():
    words_abecedarian() # Call your function(s) here.

if __name__ == '__main__':
    main()
