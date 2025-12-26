import random

# Predefined words
words = ["python", "coding", "intern", "alpha", "project"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!")
    else:
        print("✅ Correct guess!")

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("\n💀 Game Over! The word was:", word)
