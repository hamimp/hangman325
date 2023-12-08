import random
class Hangman:
    """
    A class to represent a game of Hangman.

    Attributes
    ----------
    word : (str) randomly chosen word from a word list

    word_guessed : (list) list of underscores representing the word to guess

    num_letters : (set) a set of letters present in the word

    num_lives : (int) the number of lives the player has

    word_list : (list) a list of words to choose the word from

    list_of_guesses : (list) a list of letters guessed by the player

    Methods
    -------
    check_guess(guess): Checks if the guessed letter is in the word.
    ask_for_input(): Asks the player for their guess and checks it.
    """


    def __init__(self, word_list, num_lives):
        """
            Constructs all the necessary attributes for the hangman object.

            Parameters
            ----------
            word_list : (list) a list of words to choose from
            num_lives : (int) the number of lives the player has
        """
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
            Checks if the guessed letter is in the word 
            and updates the game state accordingly.

            Parameters
            ----------
            guess : (str) the letter guessed by the player
        """

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
        """
            Asks the player for their guess and checks it.

        """

        print('For the following word: '+' '.join(self.word_guessed) )
        guess = input("Please enter a single alphabetical character: ")
        print("\n")
    
        if len(guess) == 1 and guess.isalpha():
            pass
        else:
            print("Invalid letter.")
            
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            
        else:
            self.check_guess(guess)
        self.list_of_guesses.append(guess)



def play_game():
    """
        Starts a game of Hangman with a list of words and a number of lives.
    """
    word_list = ["peach", "mango", "orange", "blackberry", "guava"]
    num_lives = 5
    hangnman_game = Hangman(word_list, num_lives)
    while True:
        if hangnman_game.num_lives > 0 and len(hangnman_game.num_letters) != 0:
            hangnman_game.ask_for_input()
        elif hangnman_game.num_lives == 0:
            print("I'm sorry, you have lost.")
            print("The word was: " + hangnman_game.word)
            break
        elif len(hangnman_game.num_letters) == 0:
            print("Congratulations! You have won by guessing the word: " + ''.join(hangnman_game.word_guessed)) 
            break
        else:
            continue


if __name__ == '__main__':
    play_game()

