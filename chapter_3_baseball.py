# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:16:31 2023

@author: jessi
"""

# welcome message

print('======================================================================')
print()
print("Baseball Team Manager")
print()
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit Program")
print()
print('======================================================================')

# menu choice
menu_option = int(input("Menu Option: "))

# options

if menu_option == 1:
    print("Calculate batting average...")
    #player_name = input("Player's name: ")
    at_bats = int(input("Official number of at bats: "))
    hits = int(input("Number of hits: "))
    player_average = round(hits / at_bats,3)
    print()
    print(f"Batting average: {player_average} ")
    #print(f"{player_name}'s batting average is {player_average}")
elif menu_option == 2:
    print("Bye!")
else:
    print("Not a valid option. Please try again.")

