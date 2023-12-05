import random
word_list = ["peach", "mango", "orange", "blackberry", "guava"]

word = random.choice(word_list)


guess = input("Plese enter a single letter: ")
if len(guess) == 1 and  guess.isalpha():
    print( "Good guess!")
    
else:
    print("Oops! That is not a valid input.")

