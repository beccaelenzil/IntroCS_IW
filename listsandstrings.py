import sys;
print (sys.version)
# python 2
#
# Name:
#
# Homework 2, Problem 1a and 1b
# slicing and indexing challenges: Lists and Strings
pi = [3,1,4,1,5,9]
e = [2,7,1]
# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]
print answer0
answer1 = e[1:3]
print 'answer1 =', answer1
answer2 = pi[-1:1:-2]
print 'answer2 =', answer2
answer3 = pi[1::]
print 'answer3 =', answer3
answer4 = e[2::-2]+pi[0::2]
print 'answer4 =', answer4

# starting strings for Homework 1

h = 'harvey'
m = 'mudd'
c = 'college'

answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print 'answer5',answer5
answer6 = c[0:4]+m[1:3]+h[-2]
print 'answer6',answer6
answer7 = h[1::]+m[1::]
print 'answer7',answer7
answer8 = h[0:3]+m[-1]+c[-1]+h[0:3]*3
print 'answer8',answer8
answer9= c[3:6]+c[1]+m[0]+h[-1:-3:-1]+c[-2]+c[1]
print 'answer9',answer9
answer10= c[0:6:2]+h[1:3]+c[0]+h[1]+c[2:4]
print 'answer10',answer10

cs= 'computer'
s='science'
#using 'cs' and 's' print competent
print cs[0:4]+cs[-2:-4:-1]+s[-1:-5:-2]+cs[-3]
