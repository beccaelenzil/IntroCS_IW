import random
import math

print ('What number range do you want to work with?')
high= 'afejn'
low ='iwegbr'
while isinstance(high,int) is True:
    high=raw_input('High Number:')
while isinstance(low,int) is True:
  low = raw_input('Low Number:')
def play():
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
            except:
                print ('Enter an integer')

    print 'Congradulations for answering 5 simple multiplication questions'
def instructions():
    print 'here are 5 multiplication problems'

def main():
    instructions()
    raw_input('press enter to continue')
    play()
main()
