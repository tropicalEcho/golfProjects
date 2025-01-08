import random, sys, os, time

def clear(): os.system("cls" if os.name == "nt" else "clear")

CHARACTERS = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]; COMMANDS = ["CLEAR", "CLS", "EXIT", "QUIT", "HELP", "H", "MANUAL", "GUIDE", "SHELDON"]; WINS = {"ROCK": ["SCISSORS", "LIZARD"], "PAPER": ["ROCK", "SPOCK"], "SCISSORS": ["PAPER", "LIZARD"], "LIZARD": ["PAPER", "SPOCK"], "SPOCK": ["SCISSORS", "ROCK"]}
regularHelp = "COMMANDS:\nCLEAR | CLS                  CLEARS THE SCREEN\nEXIT | QUIT                  KILLS THE GAME\nHELP | H                     PRINTS THIS\nMANUAL | GUIDE | SHELDON     SUMMONS SHELDON FOR HELP\n\nGUIDE:\nENTER ( SINGLE | SINGLEPLAYER | 1 | ONE | MONO ) IF YOU WANNA PLAY AGAINST COMPUTER\nENTER ( MULTI | MULTIPLAYER | 2 | TWO | BI | DUO ) IF YOU WANNA PLAY AGAINST A HUMAN"; sheldonHelp = "SCISSORS cuts PAPER\nPAPER covers ROCK\nROCK crushes LIZARD\nLIZARD poisons SPOCK\nSPOCK smashes SCISSORS\nSCISSORS decapitates LIZARD\nLIZARD eats PAPER\nPAPER disproves SPOCK\nSPOCK vaporizes ROCK\nand as it always has\nROCK crushes SCISSORS"

def handleCommands(command): clear() if command in ["CLEAR", "CLS"] else sys.exit("GOODBYE!") if command in ["EXIT", "QUIT"] else print(regularHelp) if command in ["HELP", "H"] else print(sheldonHelp) if command in ["MANUAL", "GUIDE", "SHELDON"] else ""; return True if command in ["CLEAR", "CLS", "EXIT", "QUIT", "HELP", "H", "MANUAL", "GUIDE", "SHELDON"] else False

def getChoice(prompt):
    while True:
        if handleCommands(choice := input(prompt).strip().upper()): continue
        if choice in CHARACTERS: return choice
        print("INVALID CHOICE!")

def playGame(p1, p2, single):
    if single: time.sleep(random.uniform(0.6, 1.6)); print(f"COMPUTER: {p2}")
    print("TIE!" if p1 == p2 else "YOU WON!" if p2 in WINS[p1] else "YOU LOST!" if single else "PLAYER 1 WINS!" if p2 in WINS[p1] else "PLAYER 2 WINS!")

clear()
while True:
    mode = input("SINGLEPLAYER | MULTIPLAYER: ").strip().upper()
    if handleCommands(mode): continue
    if mode not in ["SINGLE", "1", "MULTI", "2"]: print("INVALID CHOICE!"); continue

    single = mode in ["SINGLE", "1"]
    while True:
        if single: playGame(getChoice("PLAYER: "), random.choice(CHARACTERS), True)
        else: p1 = getChoice("PLAYER 1: "); clear(); p2 = getChoice("PLAYER 2: "); clear(); playGame(p1, p2, False)