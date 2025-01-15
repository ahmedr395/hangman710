import milestones_2 as word_guess

# function to check the guess
def check_guess(guess):
    guess = guess.lower()
       # this part checks if the chosen letter is in the word.
    if guess in word_guess.word:
        print("Good guess!", guess , "is in the word.")
    else:
        print("Sorry, ", guess ,"is not in the word. Try again.")

def ask_for_input(guess):
    # this checks if the guess is ana lphabet or not.
    while True :
        check = guess.isalpha()
        if check == True:
            break
        else:
            print("Invalid letter. please, enter a single alphabetical character")
    check_guess(guess)
    
ask_for_input(word_guess.guess)