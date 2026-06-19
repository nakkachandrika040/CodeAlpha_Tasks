import random

# List of predefined words
words = ["python", "internship", "computer", "programming", "developer"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
incorrect_guesses = 0

print("🎮 Welcome to Hangman!")
print(f"You have {max_attempts} incorrect guesses.\n")

while incorrect_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        remaining = max_attempts - incorrect_guesses

        print("❌ Wrong guess!")
        print(f"Attempts remaining: {remaining}")

# Game over condition
if incorrect_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)