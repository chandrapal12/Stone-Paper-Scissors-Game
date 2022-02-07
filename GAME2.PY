# This is Stone Paper Scissors.
# This is similar to Snake Water Gun Game.

print('''
                                                        __________________________________________________
                                                        ****** WELCOME TO ROCK PAPER SCISSORS GAME ******
                                                        __________________________________________________
                                                        Rules for this game: 
                        
                                                            1. Paper beats Rock but lose against Scissors
                                                            2. Scissors beats Paper but lose against Rock
                                                            3. Rock beats Scissors but lose against Paper
                        
                                                            * Here computer automatically takes the values
                                                            that is, "r", "s", "p"
                        
                                                        __________________________________________________
                        

''')

import random

def game(computer,you):

    if computer==you:
        return None

# Rock beats Scissors but lose against Paper
    elif computer=="r":
        if you=="p":
            return True
        elif you =="s":
            return False

# Scissors beats Paper but lose against Rock
    elif computer=="s":
        if you=="r":
            return True
        elif you =="p":
            return False

# Paper beats Rock but lose against Scissors
    elif computer=="p":
        if you=="s":
            return True
        elif you =="r":
            return False 
            
# This function will generate number from 1 to 3 once at a time
randNum=random.randint(1,3)
if randNum==1:
    computer="r"
elif randNum==2:
    computer="p"
elif randNum==3:
    computer="s"

# Score variable 
Score=0

# On loop 
while True:
    
# <====================Calculating total score in the high _score.txt file====================================>
# <====================read previous highscore form the high _score.txt file====================================>
    with open("high_score.txt", "r") as f:
        highScore = f.read()

# <=================if score breaks the previous high score then start printing score===========================>
    if  highScore<str(Score):
        with open("high_score.txt", "w") as f:
            f.write(str(Score))
# <===================if score doesn't break  the previous high score then keep printing previous high score=====================>
    else:
        with open("high_score.txt", "w") as f:
            f.write(highScore)




    
    print("\n\n\n\n\n\n****************************")
    print(f"Total score is {Score}")
    print("****************************")
    you = input("It's your turn: ")
    print("********Game result*********")
   

    a=game(computer,you)

    if a==None:
        print("\n*The Game is a Tie!\n")

    elif a==True:
        print("\n*You win!\n")
        Score = Score + 50
        

    else:
        print("\n*You lose!\n")

    # <========History==========>
    print("********Game history********")
    print(f"You chose '{you}'")
    print(f"Computer chose '{computer}'")
    print("****************************")
   
    





