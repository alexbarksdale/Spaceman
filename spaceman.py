import random
import os
import re
from colorama import Fore, Back, Style

# TODO: Tell the user how many guesses they have left
# TODO: Remove line 65 later

# Acknowledgement: load_word() is from starter code


def load_word():
    f = open('./words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


# Stores the correct words and wrong words
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


def guess_checker(guess, secret_word):
    if guess in correct_list:
        print(Fore.GREEN +
              '\nYou already got that letter correct' + Fore.RESET)
    elif guess in incorrect_list:
        print(Fore.RED +
              '\nYou have already guessed that letter.' + Fore.RESET)
    elif guess in secret_word:
        correct_list.append(guess)
        print('\nYou guessed a letter' +
              Fore.GREEN + ' correctly!' + Fore.RESET)
    else:
        incorrect_list.append(guess)
        print('\nYou guessed' + Fore.RED + ' incorrectly!' + Fore.RESET)


# Line 62: Checks to see if the user has guessed less than 7 times. Returns False if they lost.
# Line 64: Loops through the letters of the secret_word
# Line 65-67: Checks to see if the player won. If the letter (i) is not in the correct_list the player hasn't won yet, so
# once the user has all of the letters in the correct_list it will loop out and return True. True = won


def win_checker(secret_word):
    if len(incorrect_list) >= 7:
        return False
    for i in secret_word:
        if i not in correct_list:
            return 'Player hasn\'t won yet'
    return True


# Line 76: Loops through the letters in the secret_word
# Line 77: If a letter is in correct_list it will replace the spot with the letter (i).
# Line 80: If there isn't a correct letter it will print '_' in position of the secret_word


def spaceman(secret_word):
    while True:
        print('------------------------------------------')
        print(Fore.MAGENTA + 'Guess the Spaceman\'s word!' + Fore.RESET)
        print(secret_word)
        print('\nCorrect letters: ')
        for i in secret_word:
            if i in correct_list:
                # end=' ' Appends a space after the print statement
                print(i, end=' ')
            else:
                print('_', end=' ')
        print('\n\nIncorrect letters: ')
        for i in incorrect_list:
            print(i, end=' ')
        print('\n-----------------------------------------')
        guess = user_input()
        guess_checker(guess, secret_word)
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
