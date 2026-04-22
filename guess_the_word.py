# Alexis Christiansen
# CIS256 Term Year Spring 2026
# Exercise Assignment 4

import random

def game():
    word = ['moose', 'mountain', 'horse', 'tiger', 'lamborghini', 'machine']
    word_selection = random.choice(word)
    display = ['_'] * len(word_selection)
    guesses = []
    attempts = 10
    
    print('Play guess the word!')
    