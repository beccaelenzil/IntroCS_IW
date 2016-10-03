import random
compnum=random.randint(1,100)
user='test'
x=0
print 'The computer will chose a number between 1 and 100, it will then ask you to input a number.'
print 'If the number you input is greater then the computers number the computer will tell you.'
print 'Best of luck. The computer will tell you how many guesses it took'
while user!=compnum:
    user='test'
    while user.isdigit()==False:
        user=raw_input('Guess The Number:')
    if int(user)>compnum:
        print user,'is greater then The Number'
        x+=1
    elif int(user)<compnum:
        print user,'is less then The Number'
        x+=1
    elif int(user)==compnum:
        print user, 'is The Number.  It took you', x, 'guesses.'
