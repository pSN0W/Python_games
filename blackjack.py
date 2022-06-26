from art import logo
from os import system
import random

system('clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
play = input("Do you want to play this game or not. Type 'y' or 'n': ")
if play=='y':
    random.shuffle(cards)
    a = random.choice(cards)
    b = random.choice(cards)
    players_card = [a,b]
    computers_card = random.choice(cards)
    print(f"Your card = {players_card}")
    print(f"Computer card = {computers_card}")
    choose = input("Do you want to draw the next card or not? Type'y' or 'n': ")
    c = 0
    if choose=='y':
        c = random.choice(cards)
        print(f"You draw the card {c}")
    computers_second_card = random.choice(cards)
    let_computer_draw = True
    if a+b+c<21:
        print(f"Computer drew the card {computers_second_card}")
    if a+b+c>21:
            print("You lose")
    elif computers_card+computers_second_card>21:
        print("You Win")
    elif a+b+c>computers_card+computers_second_card:
        print("You Win")
    else:
        print("You Lose")
print("Game Over!")