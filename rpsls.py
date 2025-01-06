import random, os, sys           
WINS = {"ROCK": ["SCISSORS", "LIZARD"], "PAPER": ["ROCK", "SPOCK"], "SCISSORS": ["PAPER", "LIZARD"], "LIZARD": ["PAPER", "SPOCK"], "SPOCK": ["SCISSORS", "ROCK"]}
def clear(): os.system("cls" if os.name == "nt" else "clear")
def getChoice(prompt):
    while True:
        if choice := input(prompt).strip().upper() in ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]: return choice
        if choice in ["EXIT", "QUIT"]: sys.exit("GOODBYE!")
        if choice in ["CLEAR", "CLS"]: clear()
        else: print("INVALID CHOICE!")
def play(player1, player2):
    if player1 == player2: print("TIE!")
    elif player2 in WINS[player1]: print("PLAYER 1 WINS!")
    else: print("PLAYER 2 WINS!")
clear()
while True:
    if mode := input("SINGLEPLAYER | MULTIPLAYER: ").strip().upper() in ["SINGLE", "1"]:
        while True:
            play(getChoice("PLAYER: "), random.choice(["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]))
    elif mode in ["MULTI", "2"]:
        while True:
            play(getChoice("PLAYER 1: "), getChoice("PLAYER 2: "))
    else: print("INVALID MODE!")