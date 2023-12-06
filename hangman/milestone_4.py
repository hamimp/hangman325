import random
class Hangman:
    def __init__(self, word_list, num_lives = 5 ):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):

        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for fruit in self.word:
                if fruit == guess:
                    self.word_guessed[self.word.index(fruit)] = guess
            self.num_letters.remove(guess)
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left.")




    def ask_for_input(self):
        while True:
            guess = input("Please enter a single alphabetical character: ")
            if len(guess) == 1 and  guess.isalpha():
                pass
            else:
                print("Invalid letter.")
                continue
            if guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.check_guess(guess)
            break

        return guess




word_list = ["peach", "mango", "orange", "blackberry", "guava"]

hangnman_1 = Hangman(word_list)
hangnman_1.ask_for_input() 
print(hangnman_1.word)
print(hangnman_1.word_guessed)
print(hangnman_1.num_letters)