import gspread
from google.oath2.service_account import Credentials

from words import words
from diagram import lifes_visual_dictionary

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('Creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

"""
 We create a function to get a valid word. It selects a random choice from the list
 and continues selecting a random choice if it contains 'space' or '-'.
"""

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

"""
We create a function with a set of letters from the alphabet that need to be guessed, 
another set with letters that the user has guessed during the game.
"""

def hangman():

    print("=======================================")
    print(" ¡Welcome To The Hangman Game! ")
    print("=======================================")

    word = get_valid_word(words)
    letters_to_guess = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    lives = 7



    # Get the answers from the user, create a while loop with the number of lives
    # and the pending letters to be discovered

    while len(letters_to_guess) > 0 and lives > 0:
        
        print(f"You have {lives} lives left and you have used these letters: {' '.join(guessed_letters)}")

        # Show the actual status of the game with a list comprehension 

        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print(lifes_visual_dictionary[lives])
        print(f"Word: {' '.join(word_list)}")

        # The user chooses a new letter
        user_letter = input('Choose one letter: ').upper()

        # If the letter chosen by the user is in the alphabet
        # and is not in the set of letters that have already been entered,
        # the letter is added to the set of entered letters.
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)

            # If the letter is in the word, remove the letter 
            # from the set of letters pending to be guessed
            if user_letter in letters_to_guess:
                letters_to_guess.remove(user_letter)
                print('')
            else:
                # If the letter is not in the word, take a life.
                lives -= 1
                print(f"\nYour letter, {user_letter}, is not in the word.")
        elif user_letter in guessed_letters:
            # If the letter chosen by the user has already been entered.
            print("\nYou already chose that letter. Please choose a new letter.")
        else:
            # If the letter is not valid.
            print("\nThis letter is not valid.")


    # The game reaches this line when the player's lives run out 
    # or when all the letters of the word are guessed.
    if lives == 0:
        print(lifes_visual_dictionary[lives])
        print(f"¡Hanged! You lost. I'm so sorry. The word was: {word}")
    else:
        print(f'¡Excellent! You guessed the word {word}!')

    if __name__ == '__main__':
        hangman()
