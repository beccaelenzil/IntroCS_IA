# python 2
#
# Name:
#
# Homework 2, Problem 1a and 1b
# slicing and indexing challenges: Lists and Strings
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]
print answer0

# Problem 1:
# Creating the list [7,1] from pi and e
answer1 = e[1:]
print answer1

# Problem 2:
# Use pi and/or e to create the list [9,1,1]
answer2 = pi[-1::-2]
print answer2

#Problem 3:
# Use pi and/or e to create the list [1,4,1,5,9]
answer3 = pi[1:]
print answer3

#Problem 4:
# Use pi and/or e to create the list [1,2,3,4,5]
answer4 = e[::-2] + pi[::2]
print answer4

# starting strings for Homework 1

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:
# Creating the string 'heyyou'
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5

# Problem 6:
# Create 'collude' and store this string in the variable answer6
answer6 = c[:4]+ m[1:3] + c[-1]
print answer6

#Problem 7:
# Create 'arveyudd' and store this string in the variable answer7
answer7 = h[1:] + m[1:]
print answer7

#Problem 8:
# Create 'hardeharharhar' and store this string in the variable answer8
answer8 = h[:3] + m[2] + c[-1] + h[:3]*3
print answer8

#Problem 9:
#Create 'legomyego' and store this string in the variable answer9
answer9 = c[3:6] + c[1] + m[0] + h[6:3:-1] + c[5::-4]
print answer9

#Problem 10:
#Create 'clearcall' and store this string in the variable answer10
answer10 = c[::3] + h[1:3] + c[0] + h[1] + c[2:4]
print answer10
