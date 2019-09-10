import random
import os
import re
from colorama import Fore, Back, Style

# TODO: Ask the user to play again
# TODO: remove secret_word print

# Acknowledgement: load_word() is from starter code
# Starter code: https://github.com/Make-School-Courses/CS-1.1-Intro-to-Programming/blob/master/Projects/Spaceman/spaceman.py


def load_word():
    f = open('./words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


correct_list = []
incorrect_list = []

# user_input uses REGEX to look through the user's input and checks to see if there are only letters (A-Z)


def user_input():
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) <= 1 and guess.isalpha():
            if re.match(r'^[a-zA-Z]*$', guess):
                return guess
        else:
            print(Fore.RED + 'Please use single letters only.' + Fore.RESET)


def guess_checker(guess, secret_word, guessCounter):
    print('\n------------------------------------------')
    if guess in correct_list:
        print(Fore.GREEN +
              'You already guessed that letter correctly!' + Fore.RESET)
    elif guess in incorrect_list:
        print(Fore.RED +
              'You have already guessed that letter.' + Fore.RESET)
    elif guess in secret_word:
        correct_list.append(guess)
        print('You guessed a letter' +
              Fore.GREEN + ' correctly!' + Fore.RESET)
    else:
        incorrect_list.append(guess)
        guessCounter -= 1
        print('You guessed' + Fore.RED + ' incorrectly!' + Fore.RESET +
              '\nGuesses left: ' + Fore.YELLOW + str(guessCounter) + Fore.RESET)

    return guessCounter


def win_checker(secret_word):
    # Checks to see if the user has guessed less than 7 times. Returns False if they lost.
    if len(incorrect_list) >= 7:
        return False
    # Checks to see if the player won. If the letter (i) is not in the correct_list the player hasn't won yet, so
    # once the user has all of the letters in the correct_list it will loop out and return True. True = won
    for i in secret_word:
        if i not in correct_list:
            return 'Player hasn\'t won yet'
    return True


def spaceman(secret_word):
    guessCounter = 7
    while True:
        print('------------------------------------------')
        print(Fore.MAGENTA + 'Guess the Spaceman\'s word!' + Fore.RESET)
        print(secret_word)
        print('\nCorrect letters: ')
        # If a letter is in correct_list it will replace the spot with the letter (i).
        for i in secret_word:
            if i in correct_list:
                # end=' ' Appends a space after the print statement
                print(i, end=' ')
            # If there isn't a correct letter it will print '_' in position of the secret_word
            else:
                print('_', end=' ')
        print('\n\nIncorrect letters: ')
        for i in incorrect_list:
            print(i, end=' ')

        print('\n-----------------------------------------')
        guess = user_input()
        guessCounter = guess_checker(guess, secret_word, guessCounter)
        win = win_checker(secret_word)

        if win == False:
            print(
                Fore.RED + f'\nYou lost! The word was: {secret_word}' + Fore.RESET)
            break
        elif win == True:
            print(
                Fore.GREEN + f'\nYou won! The word was: {secret_word}' + Fore.RESET)
            break


spaceman(load_word())
