#Enhancement: play again function
#Enhancement: diplays the player's score. Player gets two points for each correct answer, and loses one point for each incorrect answer
#Enhancement: Player gets to pick the number of problems

import random

def instructions():
    print "Welcome to the Product Sum Game! I will give you two integers, the first is the product, and the second is the sum of two numbers."
    print "Your job is to guess the two numbers."
    print
    print "For example, if the product is 54 and the sum is 15, you would enter 9 and 6."
    print "For each correct answer, you get two points. Each wrong answer makes you lose a point."
    print

def play():

#Asks user for number of problems
    numberofproblems = raw_input('How many problems would you like?')
    try:
        numberofproblems = int(numberofproblems)
    except:
        raw_input("Enter an integer")

#Set score = 0
    score = 0

#User gets to chose their difficulty level
    difficulty = raw_input("Would you like level 1, 2, or 3?")

    try:
        difficulty  = int(difficulty)
        if difficulty == 1:
            low = 1
            high = 5
        elif difficulty == 2:
            low = 1
            high = 10
        elif difficulty == 3:
            low = 1
            high = 15
        else:
            difficulty = raw_input("Enter a number in range 1-3. Would you like level 1, 2, or 3?")
    except:
        difficulty = raw_input("Enter a number in range 1-3. Would you like level 1, 2, or 3?")

#For loop that gives the user the requested number of problems
    for i in range(numberofproblems):
        number1 = random.randint(low,high)
        number2 = random.randint(low,high)

        product = number1*number2
        sum = number1 + number2
        correctanswer = [ number1, number2]

        useranswer1 = -1
        useranswer2 = -1
        useranswer = [useranswer1, useranswer2]

#While loop that asks user for their answer and determines if it is correct
        while useranswer != correctanswer:
            print
            print 'product:', product, 'sum:', sum
            useranswer1 = raw_input('Enter your first guess.')
            useranswer2 = raw_input('Enter your second guess.')
    #Try is used to see if user input is an integer
            try:
                useranswer1 = int(useranswer1)
                useranswer2 = int(useranswer2)

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
                print 'Enter integer'

def repeat():
#Function asks the user if they would like to play again, and if so, calls main2 which leaves out the instructions
    print
    playagain = raw_input("Would you like to play again?")
    if playagain == 'yes':
        main2()
    else:
        print 'Goodbye!'

def main():
#Function for the first time a user plays the game
    instructions()
    play()
    repeat()

def main2():
#Function that lets the user play again for the second time without repeating the instructions
    play()
    repeat()

main()


