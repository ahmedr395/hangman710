import random

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.num_letters = int(len(self.word))
        self.word_guessed = ["_"] * self.num_letters
        self.list_of_guesses = list()
        self.word_list = word_list
        self.num_lives = num_lives


def check_guess(self, guess):
    guess = guess.lower()
    # this part checks if the chosen letter is in the word.
    if guess in (self.word):
        print("Good guess!", guess , "is in the word.")
        position = -1
        for letter in self.word:
            position = position + 1
            if letter == guess:
                self.word_guessed[position] = guess
        self.num_letters = self.num_letters - 1
        print(self.word_guessed)
    else:
        print("Sorry, ", guess ,"is not in the word. Try again.")
        self.num_lives = self.num_lives - 1
        print("You have ", self.num_lives ," lives left.")
        print(self.word_guessed)
def ask_for_input(self):
    # this checks if the guess is ana lphabet or not.
    while True :
        guess = input("Please enter a letter: ")
        check = guess.isalpha()
        if check != True or len(guess) != 1:
            print("Invalid letter. please, enter a single alphabetical character")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            check_guess(self,guess)
            self.list_of_guesses.append(guess)
            break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list , num_lives)

    while True:
        if game.num_lives == 0:
            print("sorry!! you've lost the game.")
            break
        elif game.num_letters > 0:
            ask_for_input(game)
        elif game.num_lives != 0 and game.num_letters == 0:
            print("congrats, you've won the game")
            break

play_game(["apple","mango","bananna","kiwi"])