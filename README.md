# THE HANGMAN GAME 

The Hangman Game is a Python terminal Game, which runs in the Code Institute mock terminal on Heroku

Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses. Originally a paper-and-pencil game, there are now electronic versions.

**Here is the live version of my project**


![Hangman mockup](/img/all-devices-black%20(2).png)


## HOW TO PLAY 

One person will choose the word and draw the hangman. Other players will guess letters to try and identify the word the host picked. Every player can take turns being the host, or you can play multiple rounds with the same host. The host must know how to spell the words they choose for each round

### FEATURES

* Random selection of words from a provided word list.
* GUI interface with graphical representations of the hangman.
* Interactive gameplay that responds to user input.

![Features](/img/hangman%20representation.png)

* Tracking of correct and incorrect guesses.
* Win condition when the user guesses the word correctly.

![Features](/img/Hangman%20win%20Game%20.png)

* Resetting the game for a new round.

![Features](/img/hangman%20start.png)


### Future features 

*  It is an excellent way to practice spelling
* increase vocabulary
* and keep the mind focus on teaching learning process.


## Data Model

n the given code for the Hangman game, several data models are employed to manage the game's state and logic:

Set Data Model: Used for letters_to_guess, alphabet, and guessed_letters.

* letters_to_guess is a set of unique letters in the word that need to be guessed.
alphabet is a set of uppercase ASCII letters.
guessed_letters is a set of letters that the user has already guessed.
List Data Model: Used for word_list.

* word_list is a list where each element is either a correctly guessed letter or a placeholder ('-') for unguessed letters.
Dictionary Data Model: Used for lifes_visual_dictionary.

* lifes_visual_dictionary is a dictionary where the keys are the number of lives remaining, and the values are the corresponding visual representations of the hangman.
String Data Model: Used for the word to be guessed and the input from the user.

word is the randomly chosen word to be guessed.
user_letter is the letter input by the user during the game.
Here is a brief description of each data model's role in the game:

* Set: Efficient for membership tests (checking if a guessed letter is in the word or has already been guessed) and for keeping track of unique guessed letters.
* List: Suitable for creating and updating the visual representation of the word being guessed.
Dictionary: Ideal for mapping the number of lives to the corresponding visual hangman state.
String: Represents the word to be guessed and user input as sequences of characters.
These data models collectively help manage the game's state, handle user input, and update the game's visual representation and logic accordingly.


## testing 

i have manually testing this project by doing the following:

* passed the code trought PEP8, linter and confirmed theres as not problem 
* tested in my local terminal and the Code Institute Heroku Terminal.

### Bugs 

* When i wrote the project, i was getting problem with the Credentials , but was debugging by me,
* in the terminal run.py and not hangman.py so i modify the names.

### Remain Debugs

* no bugs Remaining 

### Validator Testing

* PEP8
    * no errors retunrned from PEP8

# Deployment 

this project was deployed using Code Institute Mock terminal for Heroku

* steps to deployed:
1. fork or clone this repository
2. Create a New Heroku app
3. set the buildbacks to python and Nodejs in that order
4. Link the Heroku app to the repository 
5. click on deploy 

# Credits 

* to my Colleagues from Slack och Tutors.
* Code institute for the information provide 
* Wikipedia for the information about hangman Game.







