import random

# Predefined list of 5 words
word_list = ["apple", "house", "robot", "music", "green","icecream","health","data science","artificial intelligence"]

# Randomly select a word
word_to_guess = random.choice(word_list)
word_display = ["_"] * len(word_to_guess)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_incorrect and "_" in word_display:
    print("Word: " + " ".join(word_display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                word_display[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Incorrect guess. {max_incorrect - incorrect_guesses} guesses left.\n")

# Game over
if "_" not in word_display:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game over! The word was:", word_to_guess)
