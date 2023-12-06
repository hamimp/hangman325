import random

def ask_for_input():
    while True:
        guess = input("Please enter a single alphabetical character: ")
        if len(guess) == 1 and  guess.isalpha():
            break
        else:
            print("Invalid letter.")
    
    return guess

def check_guess(guess, word):

    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")



word_list = ["peach", "mango", "orange", "blackberry", "guava"]

word = random.choice(word_list)

guess = ask_for_input()

check_guess(guess, word)
    