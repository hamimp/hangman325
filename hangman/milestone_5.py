import random
class Hangman:
    def __init__(self, word_list, num_lives):
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
            print(f"You have {self.num_lives} lives left.")
            for index in range(0,len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            
            self.num_letters.remove(guess)
        
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")



    def ask_for_input(self):
        while self.num_lives > 0:
            print('For the following word: '+' '.join(self.word_guessed) )
            guess = input("Please enter a single alphabetical character: ")
            print("\n")
        
            if len(guess) == 1 and guess.isalpha():
                pass
            else:
                print("Invalid letter.")
                continue
            if guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.check_guess(guess)
            self.list_of_guesses.append(guess)
            game_status = self.game_over()

            if game_status != None:
                break
    
    
    def game_over(self):
        if self.num_lives == 0:
            print("I'm sorry, you have lost")
            print("The word was: "+self.word)
            return False
        elif len(self.num_letters) == 0:
            print("Congratulations! You have won by guessing the word: " + ''.join(self.word_guessed)) 
            return True
        else:
            return None
    
    def play_game(self):
        self.ask_for_input()



if __name__ == '__main__':
    word_list = ["peach", "mango", "orange", "blackberry", "guava"]
    num_lives = 6
    hangnman_1 = Hangman(word_list, num_lives)
    hangnman_1.play_game()