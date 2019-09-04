import random
import os


def load_word():
    f = open('./words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


correct_list = []
guess_list = []
maxGuess = 7


def user_input():
    while True:
        guess = input('Guess a letter: ').lower()

        if len(guess) > 1:
            print('Please use single letters only.')
        elif guess.isnumeric():
            print('Please guess using letters only.')
        else:
            return guess


def guessChecker(guess, secret_word):
    guessCount = 0
    while guessCount <= 6:
        if guess != secret_word:
            guess_list.append(guess)
            print('You guessed incorrectly.')
            guessCount += 1
        elif guess in guess_list:
            print('You have already guessed that letter.')
        elif guess in secret_word:
            correct_list.append(guess)
            print('You guess a letter correctly!')
        else:
            print('EUPHORIC')


def spaceman(secret_word):
    while True:
        print('-----------------------------------------')
        print('You have guessed the following letters: ')
        for i in guess_list:
            print(i, end=' ')  # end='' Appends a space
        print('\n-----------------------------------------')

        guess = user_input()
        guessChecker(guess, secret_word)


secretKey = load_word()
print(secretKey)
spaceman(load_word())
