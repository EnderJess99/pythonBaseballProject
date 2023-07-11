# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:01:16 2023

@author: jessi
"""

# welcome message

print('======================================================================')
print()
print("Baseball Team Manager")
print("This program calculates the batting average for a player based")
print("on the player's official number of bats and hits.")
print()
print('======================================================================')

#variables needed to calculate average
player_name = input("Player's name: ")
at_bats = int(input("Official number of at bats: "))
hits = int(input("Number of hits: "))

# calculation 
print()
player_average = round(hits / at_bats,3)

print(f"{player_name}'s batting average is {player_average}")

