import random

word_list = ['kiwi' , 'pomegranet' , 'apple' , 'bananas' , 'grapes']
print(word_list)

# generate a randome word out of the sequence
word = random.choice(word_list)
print(word)

# ask the user for a letter and checks if the input is a valid letter
guess = input("Please enter a letter: ")
if len(guess) == 1:
    print("Good guess!!!")
elif len(guess) > 1 or len(guess) < 1:
    print("Oops! That is not a valid input.")