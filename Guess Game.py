# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:31:26 2024

@author: thant
"""

print("Welcome to my quiz!")
 
play = input("Do you want to play this game?")
if play.lower() != "yes":
    quit()
    
print ("Okay! Let's play this game.")
score = 0

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does GPU stands for?")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does RAM stands for?")
if answer.lower() == "random access memory":
    print ("Correct!")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does HDD stands for?")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
print("You got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100) + " %")

