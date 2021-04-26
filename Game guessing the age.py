# Game guessing the age

import random as r
secret_age = r.randint(1, 10)
flag = False


def game_fun(guessed_age,secret):
    if guessed_age < secret:
        return 'Too low'
    elif guessed_age > secret:
        return 'Too high'
    else:
        return 'Correct'


for i in range(1, 6):
    print('Take a guess.You have '+str(6-i)+'guesses left.')
    guess = input()
    if game_fun(int(guess),secret_age) == 'Correct':
        print('You Won The Game')
        flag = True
        break

if not flag:
    print('You lost the game')
