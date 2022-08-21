from word import word_list
import random
import sys
from termcolor import colored
from title import title

title()
def chose_word_random():
    return random.choice(word_list)


word = chose_word_random()

for attempt in range(1, 7):
    guess = input().lower()

    for i in range(min(len(guess), 20)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[i], end="")

        if guess == word:
            print(colored(f"Congrats! You got the wordle in {i}", 'red'))
