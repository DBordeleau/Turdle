import random, sys

# Function that sets the secret word and starts the game
def main():
    # Opening word list file and choosing a random word for the secret word
    file = open("wordList.txt", "r")
    secret_word_list = file.readlines()
    secret_word = random.choice(secret_word_list).upper()
    # How many guesses we want the player to get
    turns = 6

    # Game instructions and calling the function to prompt user to input a guess
    print("Hello and welcome to Turdle, the shitty word game!")
    print("The goal of the game is to guess the secret 5-letter word in 6 guesses or less!")
    print("You will be provided feedback after each of your guesses using the following symbols:")
    print("X indicates that the guessed letter does not appear in the secret word.")
    print("! indicates that the guessed letter appears in the secret word, but not in the position you guessed.")
    print("+ indicates that the guessed letter appears in the same position of the secret word.")
    prompt_guess(turns, secret_word)


# Prompts user for input and ensures their guess is 5 letters long and contains no special characters
def prompt_guess(turns, secret_word):
    guess = input("\nTime to guess, there are " + str(turns) + " turns remaining."
                                                               "\nYour guess must be 5 letters long and contain no special characters or numbers: ").upper()
    while len(guess) != 5 or guess.isalpha() == False:
        guess_again(turns, secret_word)
    check_guess(turns, secret_word, guess)


# Function that is called and looped whenever the user makes an inappropriate guess
def guess_again(turns, secret_word):
    guess = input("Looks like you used an invalid character or didn't guess a 5-letter word. Try again! ")
    while len(guess) != 5 or guess.isalpha() == False:
        guess_again(turns, secret_word)
    check_guess(turns, secret_word, guess)

# Compared the user's guess to the secret word and prints appropriate game hints
# Also handles win and loss checks
def check_guess(turns, secret_word, guess):
    # A turn is spent every time the user guesses
    turns -= 1
    # If their guess matches the word they win.
    if guess == secret_word:
        print("Correct! The secret word was " + secret_word + "! You won with " + turns + "remaining!")
        sys.exit()

    # Comparing each letter of the guess with the secret word and printing the corresponding symbol
    for x in range(0, 5):
        if secret_word[x] == guess[x]:
            print("+", end="")
        elif guess[x] in secret_word:
            print("!", end="")
        else:
            print("X", end="")

    # If they run out of turns they lose.
    if turns == 0:
        print("You failed to guess the secret word in 6 turns. The secret word was: " + secret_word)
        print("You lose.")
        sys.exit()
    prompt_guess(turns, secret_word)

# starting the game
main()
