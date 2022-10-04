import random
from re import A
from turtle import clear
from hangman_words import word_list
import os


chosen_word = random.choice(word_list)

lives = 6 #lives of player
end_of_game = False

# print(f"The solution is: {chosen_word}.")


#display
display = [] #create a list
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"  #add item string underscore _d
print(display)

while not end_of_game: 
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    #check if they guessed a letter
    if guess in display:
        print(f"You have already guessed. {guess}")

    #display the letter in the list if the user guessed right
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    #number of tries 6
    if guess not in chosen_word:
        print(f'You guessed {guess}, thats not in the word you lose a life. ')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")