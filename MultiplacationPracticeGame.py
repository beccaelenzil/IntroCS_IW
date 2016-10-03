import random
import math

def numrange():
    print ('What number range do you want to work with?')
    global high
    high='test'
    while high.isdigit()==False:
        high=raw_input('Please enter your high number:')
    global low
    low='test'
    while low.isdigit()==False:
        low=raw_input('Please enter your low number:')

def play():
    wrong=0
    for i in range(5):
        factor1 = random.randint(int(low),int(high))
        factor2 = random.randint(int(low),int(high))
        CorrectAnswer = factor1*factor2
        userAnswer = -1
        while userAnswer != CorrectAnswer:
            userAnswer = raw_input('Please enter the product of '+ str(factor1)+' and '+str(factor2)+':')
            try:
                userAnswer = int(userAnswer)
                if userAnswer == CorrectAnswer:
                    print 'Correct'
                else:
                    print 'Incorrect'
                    wrong+=1

            except:
                print ('Enter an integer')
    print 'Congradulations for answering 5 simple multiplication questions.  You guessed wrong',wrong,'times.'
def instructions():
    print 'here are 5 multiplication problems'

def main():
    instructions()
    raw_input('press enter to continue')
    numrange()
    play()
main()
