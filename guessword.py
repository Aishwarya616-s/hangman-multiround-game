import random

# Word list with hints
word_list = [
    ("python", "A popular programming language"),
    ("elephant", "The largest land animal"),
    ("guitar", "A musical instrument with strings"),
    ("pizza", "An Italian dish with cheese and toppings"),
    ("volcano", "A mountain that erupts"),
    ("rainbow", "Appears after rain and contains 7 colors"),
    ("internet", "Global network for sharing information")
]

def play_hangman(secret_word, hint):
    guessed_letters = []
    lives = 6

    print("\n💡 Hint:", hint)
    print(f"You have {lives} lives to guess the word.")

    def display_word():
        return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

    while lives > 0:
        print("\nWord:", display_word())
        guess = input("Guess a letter (or type 'quit' to exit): ").lower()

        if guess == "quit":
            print("🚪 Exiting the current word...")
            return "quit"

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
        elif guess in secret_word:
            print("✅ Good guess!")
            guessed_letters.append(guess)
        else:
            print("❌ Wrong guess!")
            guessed_letters.append(guess)
            lives -= 1
            print("❤️ Lives left:", lives)

        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Well done! You guessed the word:", secret_word)
            return "won"

    print("\n💀 Out of lives! The word was:", secret_word)
    return "lost"

# Main game loop
random.shuffle(word_list)  # Randomize word order
print("🎮 Welcome to Multi-Round Hangman!")
score = 0

for word, hint in word_list:
    result = play_hangman(word, hint)

    if result == "quit":
        break
    elif result == "won":
        score += 1

print("\n🏁 Game Over!")
print("✅ Total Words Solved:", score, "out of", len(word_list))
