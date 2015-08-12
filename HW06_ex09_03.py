#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body

def avoids(word, forbidden):
	doestUse = True
	for letter in forbidden:
		if word.lower().find(letter.lower()) > -1 :
			doestUse = False
	return doestUse

def user_input_avoids():
	while True:
		countOfWords = 0
		userInput = raw_input("Please enter the forbidden characters : ")

		if userInput == "done":
			break
		else:
			fin = open("words.txt", "r")
			for line in fin:
				word = line.strip()
				if avoids(word, userInput) == True:
					countOfWords+=1
		print "The number of words that don't contain the forbidden characters are : " + str(countOfWords)

# Still doing the third one. Will upload later. 

##############################################################################
def main():
    user_input_avoids()  # Call your function(s) here.

if __name__ == '__main__':
    main()
