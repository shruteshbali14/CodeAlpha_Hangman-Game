import random

# List of words
words = ["hello", "tiger", "code", "learn", "world", "letter", "dog", "cat"]

# Select a random word
word = random.choice(words)

# Create display with underscores
display = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Rules: Guess one letter at a time.")
print("You have 6 wrong attempts.\n")

# Main game loop
while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)
    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        attempts -= 1
        print("Wrong guess!")

# Game result
print("\n" + "=" * 30)

if "_" not in display:
    print(" Congratulations! You won!")
    print("The word was:", word)
else:
    print("Game Over!")
    print("The word was:", word)

input("\nPress Enter to exit...")
