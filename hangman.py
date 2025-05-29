# Welcome
print("Welcome to hangman!")
print("=====" * 10)

# Setting the word
import choose_word as c_w
word = c_w.generate_word()
chances = len(word) + 6

# List implementing
guess_user = [' _ '] * len(word)

# Guessed letters
guessed = []

print("Let's start off with a", len(word), "letter word and")
print("You have", chances, "chances to guess the word")

# Win condition
def win():
    return guess_user.count(' _ ') == 0

# Validating input
def validate(string):
    global chances
    if len(string) == 1 and chances >= 0:
        calculate_pos(string)
    else:
        return False

# Print guessed letters
def print_letters_guessed(Str):
    global guess_user
    for i in guess_user:
        print(i, end=" ")
    print()

# Calculate positions
def calculate_pos(string):
    global word, guess_user, chances
    found = False

    for i in range(len(word)):
        if string == word[i]:
            guess_user[i] = string
            found = True

    if not found:
        chances -= 1

    print_letters_guessed(string)

# User guess input
def get_guess(n):
    global chances
    for i in range(n):
        guesses = input("Enter a letter: ")
        validate(guesses)

        print("You have", chances, "chances left")

        if guesses in guessed:
            print("You have guessed it already")
        else:
            guessed.append(guesses)
            print([i for i in guessed])

        if win():
            print("You WON!")
            print("You guessed the word")
            break

# Initial input
get_guess(chances)

# Main loop
while chances > 0 and not win():
    get_guess(chances)

# Game end
if win():
    pass
else:
    print("You lost")
    print("The word was", word)
