#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body

def uses_all(word, letters):
	usesAll = True
	for letter in letters:
		if word.lower().find(letter.lower()) < 0:
			usesAll = False
	return usesAll

def words_aeiou():
	fin = open("words.txt", "r")
	count = 0
	for line in fin:
		if uses_all(line, "aeiou") == True:
			count+=1
	print "The number of words that use all aeiou: " + str(count)

def words_aeiouy():
	fin = open("words.txt", "r")
	count = 0
	for line in fin:
		if uses_all(line, "aeiouy") == True:
			count+=1
			print line
	print "The number of words that use all aeiouy: " + str(count) 


##############################################################################
def main():
    words_aeiou()  # Call your function(s) here.
    words_aeiouy()

if __name__ == '__main__':
    main()
