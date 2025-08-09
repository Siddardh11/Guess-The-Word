import random

def load_words(file_path):
    """
    Loads words from a given file.
    Each line in the file should contain a single word.
    Only words containing alphabetic characters are kept.
    """
    with open(file_path, 'r') as f:
        words = [line.strip().lower() for line in f if line.strip()]
    # Optionally filter out words with non-alphabetic characters
    words = [word for word in words if word.isalpha()]
    return words

def get_random_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and the rest as underscores."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_guess(guessed_letters):
    """Get a valid guess from the player."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def hangman():
    # Specify the path to your dictionary file.
    # Make sure that the file (e.g., words.txt) is in the same directory as this script
    dictionary_file = 'words.txt'
    
    try:
        word_list = load_words(dictionary_file)
    except FileNotFoundError:
        print(f"Dictionary file '{dictionary_file}' not found. Please create the file with your word list.")
        return

    max_incorrect_guesses = 6  # Number of incorrect guesses allowed
    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    while True:
        word = get_random_word(word_list)
        guessed_letters = set()
        incorrect_guesses = 0
        
        print("\nNew game started!")
        print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
        
        while incorrect_guesses < max_incorrect_guesses:
            print("\nWord: ", display_word(word, guessed_letters))
            guess = get_guess(guessed_letters)
            guessed_letters.add(guess)
            
            if guess in word:
                print(f"Good guess! {guess} is in the word.")
                # Check if every letter in the word has been guessed
                if all(letter in guessed_letters for letter in word):
                    print(f"Congratulations! You guessed the word: {word}")
                    break
            else:
                incorrect_guesses += 1
                print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
                incorrect_letters = [g for g in guessed_letters if g not in word]
                print("Incorrect guesses so far:", ', '.join(incorrect_letters))
            
        if incorrect_guesses == max_incorrect_guesses:
            print(f"Game over! The word was: {word}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    hangman()
