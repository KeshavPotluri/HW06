# write ten random numbers to a file
import random

fout = open("Random.txt", "w")

for index in range(10):
	randomNumber = random.randint(1, 100)
	fout.write(str(randomNumber) + "\r\n")

fout.close()

# read from roster.txt and print 

fin = open("roster.txt")

numberOfNames = 0

for line in fin:
	name = line.strip()
	if name.find("e") > -1 or name.find("E")> -1:
		print name
		numberOfNames +=1

print "The number of names with the letter 'e' are : " + str(numberOfNames) 



#modify to write to a file

fin = open("roster.txt")
fout = open("roster_with_e.txt","w")

numberOfNames = 0

for line in fin:
	name = line.strip()
	if name.find("e") > -1 or name.find("E")> -1:
		fout.write(str(name) + "\r\n")
		numberOfNames +=1

fout.write("The number of names with the letter 'e' are : " + str(numberOfNames) + "\r\n")




