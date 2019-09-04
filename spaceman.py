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


def guess_checker(guessCount, guess, secret_word):
    if guessCount <= 7:
        if guess in guess_list:
            print('\nYou have already guessed that letter.')
        elif guess in secret_word:
            guess_list.append(guess)
            print('\nYou guessed a letter correctly!')
        else:
            guess_list.append(guess)
            print('\nYou guessed incorrectly.')
            guessCount += 1
    else:
        print('rofl')


def spaceman(secret_word):
    while True:
        print('-----------------------------------------')
        print(secret_word)
        print('\nYou have guessed the following letters: ')
        for i in guess_list:
            print(i, end=' ')  # end='' Appends a space
        print('\n-----------------------------------------')

        guess = user_input()
        guess_checker(0, guess, secret_word)


spaceman(load_word())
