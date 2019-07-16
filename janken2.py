"""
Janken ("Rock, Paper, Scissors")

Author: Mike Rassi

Date : 16.17.19
"""

import random
player = 0
cpu = 0
game = "on"


def game_load():
    print ("\nNEW GAME\n\nPlayer: %s\nCPU: %s"%(player,cpu))
    begin = input("\nSTART").lower()

def game_complete():
    global game
    global player
    player += 1
    print ("\nYou win!\n\nPlayer: %s\nCPU: %s\n"%(player,cpu))
    replay = input("Will You Play Again? (Y/N): ").lower()
    if replay == "n":
        game = "off"
        end = input("Thank You For Playing").lower()



def game_draw():
    print("\nDraw!\n")

    one = input("\nPlease choose rock, paper or scissors: ").lower()

    while one != "rock" and one != "paper" and one != "scissors" and  one != "r" and one != "p" and one != "s":
        one = input("Invalid selection. Please choose rock, paper or scissors: ").lower()
    adjust(one)
    calculation(one)

def game_over():
    global game
    global cpu
    cpu += 1
    print ("\nComputer Wins!\nYou lose!\n\nPlayer: %s\nCPU: %s\n"%(player,cpu))
    replay2 = input("Will You Play Again? (Y/N): ").lower()
    if replay2 == "n":
        game = "off"
        end = input("Thank You For Playing").lower()

def adjust(one):
    if one == "s":
        one = "scissors"
    elif one == "r":
        one = "rock"
    elif one == "p":
        one = "paper"

def calculation(one):
    two = computer[random.randint(0,2)]
    print("\nYou have",one,"\nThe computer has",two)
    if one == 'rock' and two == 'scissors':
        game_complete()
    elif  one == 'scissors' and two == 'paper':
        game_complete()
    elif  one == 'paper' and two == 'rock':
        game_complete()
    elif  one == two:
        game_draw()
    else:
        game_over()


game_load()

while game == "on":
    computer = ['rock', 'paper', 'scissors']
    one = input("\nPlease choose rock, paper or scissors: ").lower()

    while one != "rock" and one != "paper" and one != "scissors" and  one != "r" and one != "p" and one != "s":
        one = input("Invalid selection. Please choose rock, paper or scissors: ").lower()
    adjust(one)
    calculation(one)
