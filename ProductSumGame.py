import random

def instructions():
    print "Welcome to the Product Sum Game! I will give you two integers, the first is the product, and the second is the sum of two numbers."
    print "Your job is to guess the two numbers."

def play():
    numberofproblems = raw_input('How many problems would you like?')
    try:
        numberofproblems = int(numberofproblems)
    except:
        print "Enter an integer"
    for i in range(numberofproblems):
        number1 = random.randint(2,12)
        number2 = random.randint(2,12)

        product = number1*number2
        sum = number1 + number2
        correctanswer = [number1, number2]
        print [product, sum]

        useranswer1 = -1
        useranswer2 = -1
        useranswer = [useranswer1, useranswer2]
        score = 0

        while useranswer != correctanswer:
            useranswer1 = raw_input('Enter your first guess.')
            useranswer2 = raw_input('Enter your second guess.')
    #Try is used to see if user input is an integer
            try:
                useranswer1 = int(useranswer1)
                useranswer2 = int(useranswer2)
            # print "correctanswer1: ", correctanswer1
            # print "correctanswer1: ", correctanswer1
                if useranswer1 == number1 and useranswer2 == number2:
                    print 'Correct!'
                    score = score + 2
                    print "Your score is ", score
                    useranswer = correctanswer
                elif useranswer1 == number2 and useranswer2 == number1:
                    print 'Correct!'
                    score = score + 2
                    print "Your score is ", score
                    useranswer = correctanswer
                else:
                    print 'Incorrect, try again.'
                    score = score - 1
                    print "Your score is ", score
            except:
                print 'Enter integers'

def repeat():
    playagain = raw_input("Would you like to play again?")
    if playagain == 'yes':
        main2()
    else:
        print 'Goodbye!'

def main():
    instructions()
    play()
    repeat()

def main2():
    play()
    repeat()

main()


