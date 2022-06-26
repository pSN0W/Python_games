import random
from hangman_words import word_list
from hangman_art import *
from os import system

system('clear')
print(logo)
word = random.choice(word_list)
word_len = len(word)
display = []
alphabets = []
for _ in range(word_len):
    display+='_'
lives = 6
end_of_game = False
guess = input("Guess an character : ").lower()
while not end_of_game:
    system('clear')
    if guess in alphabets:
        print(f"You have already guessed {guess}. Please choose another alphabet")
    elif guess in word:
        print("Yay you chose a currect alphabet")
        for i,character in enumerate(word):
            if character==guess:
                display[i] = guess
        
    else:
        print(f"You guessed {guess} which is not in the word. You lose a life")
        lives-=1
    alphabets+=guess    
    if '_' not in display:
        end_of_game = True
        print("You Win !!")
    
    if lives==0:
        print("You Lose :(")
        end_of_game = True
    
    print(' '.join(display))
    print(stages[lives])
    if not end_of_game:
        guess = input("Guess an character : ").lower()

print(f"The correct word is {word}")
