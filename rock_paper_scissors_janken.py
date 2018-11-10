"""
Janken ("Rock, Paper, Scissors")

Author: Mike Rassi
Date : 21.10.18

"""



import random

def game_load():
    print ()
    print ("Start Game")
    print ()
    contin = input("Press Enter to continue: ").lower()

def game_complete():
    print ()
    print ("You win!")
    print ()
    exit = input("Press Enter to exit: ").lower()

def game_draw():
    print("Draw!")
    print ()
    one = input("Please choose rock, paper or scissors: ").lower()
    while one != "rock" and one != "paper" and one != "scissors" and  one != "r" and one != "p" and one != "s":
        one = input("Invalid selection. Please choose rock, paper or scissors: ").lower()
    if one == "s":
        one = "scissors"
    elif one == "r":
        one = "rock"
    elif one == "p":
        one = "paper"
    janken(one)

def game_over():
    print ()
    print ("Computer Wins!")
    print ("You lose!")
    exit = input("Press Enter to exit: ").lower()

def janken(one):
    #The computer randomly generates one of the three options.
    two = computer[random.randint(0,2)]
    #The result, your selection and the computers'.
    print("You have " + one)
    print("The computer has " + two)

    if one == 'rock' and two == 'scissors':
        game_complete()
    elif  one == 'scissors' and two == 'paper':
        game_complete()
    elif  one == 'paper' and two == 'rock':
        game_complete()
    #If Draw, restart the loop.
    elif  one == two:
        game_draw()
    else:
        game_over()





game_load()

# Allows the player to select one of the options.
# "While" will make sure only "Rock", "Paper" or "Scissors" is selected

one = input("Please choose rock, paper or scissors: ").lower()
while one != "rock" and one != "paper" and one != "scissors" and  one != "r" and one != "p" and one != "s":
    one = input("Invalid selection. Please choose rock, paper or scissors: ").lower()
if one == "s":
    one = "scissors"
elif one == "r":
    one = "rock"
elif one == "p":
    one = "paper"
#The computer's options.
computer = ['rock', 'paper', 'scissors']

janken(one)
