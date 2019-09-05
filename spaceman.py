import random
import os

# Acknowledgement: load_word() is from starter code


def load_word():
    f = open('./words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


correct_list = []
guess_list = []


def user_input():
    while True:
        guess = input('Guess a letter: ').lower()

        if len(guess) > 1:
            print('Please use single letters only.')
        elif guess.isnumeric():
            print('Please guess using letters only.')
        else:
            return guess


guessCount = 0


def guess_checker(guess, secret_word):
    global guessCount
    if guessCount <= 6:
        if guess in guess_list:
            print('\nYou have alread guessed that letter.')
        elif guess in secret_word:
            correct_list.append(guess)
            print('\nYou guessed a letter correctly!')
        else:
            guess_list.append(guess)
            print('\nYou guessed incorrectly.')
            guessCount += 1

        print('Guess test: ' + str(guessCount))

    else:
        print('You ran out of guesses!')


def spaceman(secret_word):
    while True:
        print('-----------------------------------------')
        print(secret_word)
        print('\nCorrect letters: ')
        for i in secret_word:
            if i in correct_list:
                print(i, end=' ')
            else:
                print('_', end=' ')
        print('\n\nIncorrect letters: ')
        for i in guess_list:
            print(i, end=' ')  # end='' Appends a space
        print('\n-----------------------------------------')

        guess = user_input()
        guess_checker(guess, secret_word)


spaceman(load_word())
