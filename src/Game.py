import re
import sys
import random
import os

# Taking input from the user
UserSelection = input("Rock / Paper / Scissor\n").lower()

# Validate the user input
ValidAnswer = 0

while ValidAnswer==0:
    if  UserSelection=="rock" or UserSelection=="paper" or UserSelection=="scissor":
        print("wait for me...")
        ValidAnswer=1

    else:
        print("Incorrect input...\n") 
        UserSelection = input("Rock / Paper / Scissor\n").lower()
       

# Generating computer input using random function
Options = ["rock","paper","scissor"]
CompSelection = random.choice(Options)

# Apply game rules using if-elif-else statement
if UserSelection=="rock":
    if CompSelection=="rock":
        print(f"We both select {CompSelection}!")
    elif CompSelection=="paper":
        print(f"You selected {UserSelection} and I selected {CompSelection}, so I am the winner!")
    else:
        print(f"You selected {UserSelection} and I selected {CompSelection}, so you are the winner!\n Congrats!")
elif UserSelection=="paper":
    if CompSelection=="paper":
        print(f"We both select {CompSelection}!")
    elif CompSelection=="scissor":
        print(f"You selected {UserSelection} and I selected {CompSelection}, so I am the winner!")
    else:
        print(f"You selected {UserSelection} and I selected {CompSelection}, so you are the winner!\n Congrats!")
else:
    if CompSelection=="scissor":
        print(f"We both select {CompSelection}!")
    elif CompSelection=="rock":
        print(f"You selected {UserSelection} and I selected {CompSelection}, so I am the winner!")
    else:
        print(f"You selected {UserSelection} and I selected {CompSelection}, so you are the winner!\n Congrats!")

# Generate the output