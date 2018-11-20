

import random

highscore_var = 10
print("""------------------------------------
Welcome to our Number Guessing Game !!!
REMEMBER:The fewer attempts the better the score!
------------------------------------""")

def start_game():
    correct_num = random.randint(1,10)
    global attempts_var
    attempts_var = 0
    while 1 == True :
        try:
            answer = input("Please, pick a number between 1 and 10: ")
            answer = float(answer)
            if answer<1 or answer>10 :
                raise ValueError("Was the number from 1 to 10?")
            elif answer%1 !=0:
                raise ValueError("Did I mention we need an 'Integer Number'?")
            attempts_var += 1
        except ValueError as err:
            print("Ooops! We can't accept this answer!")
            print("{}".format(err))
        else:
            if answer > correct_num :
                print("It's lower")
            elif answer < correct_num :
                print("It's higher")
            elif answer == correct_num :
                print("Got it")
                print("You made it with {} attemts!".format(attempts_var))
                break

start_game()

while 1 == True:
    if attempts_var < highscore_var:
        highscore_var = attempts_var
    print("GAME OVER! The hiscore is : {} points!".format(highscore_var))
    play_again = input("Would you like to play again?Y/N  ")
    if play_again.upper()=="Y" :
        start_game()
    elif play_again.upper()=="N" :
        print("Thank you for playing! See you soon!")
        break
    else :
        print("Sorry! Invalid answer! Try again!")
        continue
