#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e(word):
	hasNoE = True
	for letter in word:
		if letter.lower() == "e":
			hasNoE = False
	return hasNoE

def print_Words():
	fin = open("words.txt", "r")
	count = 0
	countOfWords = 0
	for line in fin:
		countOfWords+=1
		if has_no_e(line) == True:
			count+=1
	percentage = float(count)*100/countOfWords
	print "The percentage of words without the letter 'e' is : " + str(percentage) + "%"





##############################################################################
def main():
   print_Words()  # Call your function(s) here.

if __name__ == '__main__':
    main()
