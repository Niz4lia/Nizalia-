# hangman.py
import random

words = ["python", "computer", "programming", "developer", "keyboard", "hangman"]
stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """,
]

word = random.choice(words)
guessed = ["_"] * len(word)
tries = len(stages) - 1
used = []

print("🎯 Welcome to HANGMAN!")

while tries > 0 and "_" in guessed:
    print(stages[len(stages) - 1 - tries])
    print("Word: " + " ".join(guessed))
    print(f"Used letters: {', '.join(used)}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in used:
        print("You already guessed that letter.")
        continue

    used.append(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        tries -= 1
        print("❌ Wrong!")

if "_" not in guessed:
    print(f"\n🎉 You won! The word was '{word}'.")
else:
    print(stages[-1])
    print(f"\n💀 You lost! The word was '{word}'.")
