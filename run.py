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



