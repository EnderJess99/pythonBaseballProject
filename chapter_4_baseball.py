# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:15:53 2023

@author: jessi
"""

# welcome message
def print_welcome_message():
    print('======================================================================')
    print("Baseball Team Manager")
    print()
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit Program")
    print()
    print('======================================================================')    
    print()  
    

def calculate_batting_average():
    menu_option = int(input("Menu_Option: "))
    if menu_option == 1:
        print("Calculate batting average...")
        at_bats = int(input("Official number of at bats: "))
        hits = int(input("Number of hits: "))
        player_average = round(hits / at_bats,3)
        print()
        print(f"Batting average: {player_average}")
    elif menu_option == 2:
        print("Bye!")
    else:
        print("Not a valid option. Please try again.")
        
def main():
    print_welcome_message()
    again = "y"
    while again.lower() == "y":
        calculate_batting_average()
        print()
        again = input("Calculate another average? (y/n): ")
    print("Bye!")
    
if __name__ == "__main__":
    main()
