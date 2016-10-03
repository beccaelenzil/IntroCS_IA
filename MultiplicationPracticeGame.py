import random

def instructions():

    print'Hello! Welcome to my multiplication game. I will give you two factors, and you have to enter the product.'
    print 'We will try five problems.'
    user_name = raw_input('Enter your name.')
    return user_name

def play(user_name):

    for i in range(5):

        factor1 = random.randint(0,12)
        factor2 = random.randint(0,12)

        user_answer = -1
        correct_answer = factor1*factor2


        while user_answer != correct_answer:
            user_answer = raw_input(user_name + ' please enter the product of ' + str(factor1) + ' and ' + str(factor2) +'.')
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print 'Correct!'
                else:
                    print 'Incorrect :('
            except:
                print 'Enter an integer'
    if raw_input('Good job! Type yes to play again') == 'yes':
        play(user_name)
    else:
        print 'Goodbye :('

def main():
    name = instructions()
    play(name)

main()

