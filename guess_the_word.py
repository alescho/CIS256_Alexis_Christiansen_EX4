# Alexis Christiansen
# CIS256 Term Year Spring 2026
# Exercise Assignment 4

#import random for random word selection
import random

#creating game function
def game():
    word = ['moose', 'mountain', 'horse', 'tiger', 'lamborghini', 'machine'] 
    word_selection = random.choice(word)
    display = ['_'] * len(word_selection)
    guesses = []
    attempts = 10
    
    #printing game name for user
    print('Play guess the word!')

    while attempts > 0 and '_' in display: 
        print(display)
        guess = input('Guess a letter in the word: ')

        if guess in word_selection:
            for i, letter in word_selection
                if letter == guess: 
                    display[i] = guess

        else: 
            attempts -= 1

    if '_' not in display:
        print('You guessed the word right: {word_selection}')
    else: 
        print('Sorry the word was: {word_selection}')
