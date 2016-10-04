#Enhancement: After the game ends, computer diplays the number of tries it took to guess the number

import random

def play():

        compnumber = random.randint(1, 100)
        userguess = raw_input('Enter your guess.')
        counter = 1

        while userguess != compnumber:
            try:
                userguess = int(userguess)
                if userguess == compnumber:
                    print 'Correct! Good job.'
                    print 'It only took you', counter, 'guesses to guess my number!'
                else:
                     if userguess < compnumber:
                          print 'Incorrect, your guess is too low.'
                          counter = counter + 1
                          userguess = raw_input('Enter your guess.')

                     else:
                         print 'Incorrect, your guess is too high.'
                         counter = counter + 1
                         userguess = raw_input('Enter your guess.')

            except:
                userguess = raw_input('Enter an integer.')


def instructions():
    print "Welcome to Guess my Number! I will randomly choose a number between 1 and 100 and you have to guess what it is."
    print "If you guess correctly, you win! If you guess incorrectly, I will tell you your number is either too high or too low."
    print "Then, you can guess again."

def main():
    instructions()
    play()

main()
