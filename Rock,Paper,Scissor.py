#!/usr/bin/env python
# coding: utf-8

# ## ROCK, PAPER, SCISSORS

# In[4]:


import random

def valid(s):
    try:
        s=s.lower()
    except:
        s='none'
    a=["rock","paper","scissors"]
    if s==a[0] or s==a[1] or s==a[2]:
        s=s
    elif s not in a:
        print("Invalid move")
        move=input("Enter your move rock, paper or scissors: ")
        s=valid(move)
    return s
        
def randomn():
    a=["rock","paper","scissors"]
    computer=random.choice(a)
    return computer

def scorekeeper(comp_move,player_move):
    comp_score=0
    player_score=0
    moves=0
    lst=[comp_move,player_move]
    if lst[0]==lst[1]:
        comp_score+=0
        player_score=player_score+0
    elif (lst[0]=='rock' and lst[1]=='scissors'):
        comp_score+=1
    elif (lst[0]=='scissors' and lst[1]=='paper'):
        comp_score+=1
    elif (lst[0]=='paper' and lst[1]=='rock'):
        comp_score+=1
    else: 
        player_score+=1
            
    return [comp_score,player_score]

def result(comp_score,player_score):
    print("Your Score is {}".format(player_score))
    print("Computer Score is {}".format(comp_score))
    print("\n")
    if comp_score==player_score:
        print("Oops! It's a TIE. Break time! Play Again. :0")
    elif comp_score>player_score:
        print("You Lose. Better Luck next time! Try Again.")
    else:
        print("Hurrah! You WIN the game. Victory! :)")

# main program starts:
print("******************** ROCK, PAPER, AND SCISSORS ***************************\n")
print("LET'S PLAY THIS GAME: \n")
print("You have only 5 chances \n")
chance=0
x=0
y=0
while chance<5:
    chance=chance+1
    print("CHANCE {}: \n".format(chance))
    move=input("Enter your move rock, paper or scissors: ")
    player_move=valid(move)
    comp_move=randomn()
    print(f"Your move: {player_move.upper()}")
    print(f"Computer's move: {comp_move.upper()}")
    if chance==5:
        lst=scorekeeper(comp_move,player_move)
        if lst[0]==lst[1]:
            x+=0
            y+=0
            print("Nice Move. It's a Tie.  You have {} chance/s left.\n".format(5-chance))
                                    
        elif lst[0]<lst[1]:
            x+=0
            y+=1
            print("Woow! Wonderful, Great Move. You get 1 point. You have {} chance/s left.\n".format(5-chance))               
        
        else: 
            x+=1
            y+=0
            print("Computer gets 1 point. You have {} chance/s left.\n".format(5-chance))
        result(x,y)
        break
    else:
        lst=scorekeeper(comp_move,player_move)
        if lst[0]==lst[1]:
            x+=0
            y+=0
            print("Nice Move. Try Again.  It's a Tie.  You have {} chance/s left.\n".format(5-chance))
                                    
        elif lst[0]<lst[1]:
            x+=0
            y+=1
            print("Woow! Wonderful, Great Move. Keep it up. You get 1 point. You have {} chance/s left.\n".format(5-chance))               
        
        else: 
            x+=1
            y+=0
            print("Best of Luck Next time . Computer gets 1 point. Try Again. You have {} chance/s left.\n".format(5-chance))
        
   


# In[ ]:




