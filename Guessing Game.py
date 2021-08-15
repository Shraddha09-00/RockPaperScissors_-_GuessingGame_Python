#!/usr/bin/env python
# coding: utf-8

# # GUESSING GAME

# In[2]:


import random

# function to check whether an integer is input

def check(x):
    try:
        x=int(x)
    except:
        x=-1
    return x

#function to take an input from user until user enters a positive value

def repeat(z):
    a=[]
    a.append(check(z))
    while (a[0]<0):
        z=input("Enter a positive number: ")
        a.clear()
        a.append(check(z))
        continue
    z=a[0]
    return z

# Main Program for game: Guessing game
count=0
print("////////////////////////////////////////////////////////")
print("***************** THE GAME BEGINS *********************")
print("///////////////////////////////////////////////////////")
n=input("Enter a minimum value for guessing game: ")
var1=check(n)
n=repeat(var1)
m=input("Enter a maximum value for guessing game: ")
var2=check(m)
m=repeat(var2)
# to get value greater than minimum from user
while m<=n:
    m=input("Enter a value greater than minimum value: ")
    var2=check(m)
    m=repeat(var2)
    continue
print(f"Minimum value: {n}  Maximum value: {m}")
computer=random.randrange(n,m+1)
print("\n")
print("You have total 7 Tries to guess the number correctly. All the Best!\n")
print("<<<<<<<<<<<<<<<< LET'S PLAY THE GAME >>>>>>>>>>>>>>>>>>>>>")
while count<7:
    print(f"GUESS {count+1}: ")
    player=input(f"Enter a number between {n} and {m}: ")
    player=check(player)
    count+=1
    if player not in range(n,m+1):
        print(f"Invalid choice! Attempt failed. You have {7-count} chance/s left. Choose between {n} and {m}.")
        print("\n")
        continue
    else:
        if player==computer:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
            print(f"   YOU WIN! You guessed it right, its {player}:)!\n")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            break
        elif player<computer:
            if count==7:
                print(f"You lost the game. Computer had chosen {computer}. Better luck next time!")
            else:
                print(f"Try Again! You guessed too Small. You have {7-count} chance/s left.")
                print("\n")
                continue
        else:
            if count==7:
                print(f"You lost the game. Computer had chosen {computer}. Better luck next time!\n")
            else:
                print(f"Try Again! You guessed too High. You have {7-count} chance/s left.")
                print("\n")
                continue
        
            

    


# 
