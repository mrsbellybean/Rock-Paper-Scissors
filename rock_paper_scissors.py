#Rock Paper Scissors App
import random
import string

shoot = ["rock", "paper", "scissors"]
player = ["rock", "paper", "scissors"]


def play():
    print ("Rock, paper, scissors...")
    pc_choice = random.randint(0,2)              #Generate a random number from 0 to 2
    pc_choice = shoot[pc_choice]             #Use the random number to reference rock, paper or scissors
    user_choice = input("Choosing one.... Enter rock, paper or scissors...\n").lower()
    print (f"PC chooses: {pc_choice}...")                       #Output what the computer chooses
    battle(user_choice, pc_choice)
    

def battle(user_choice, pc_choice):
    while True:
        try:
            if user_choice == "rock":
                if pc_choice == "rock":
                    print("Draw, try again...")
                    play()
                elif pc_choice == "paper":
                    print("Paper covers rock, you lose!")
                    main_menu()
                elif pc_choice == "scissors":
                    print ("Rock smashes scissors, you win!")
                    main_menu()
            elif user_choice == "paper":
                if pc_choice == "rock":
                    print("Paper covers rock, you win!")
                    main_menu()
                elif pc_choice == "paper":
                    print("Draw, try again")
                    play()
                elif pc_choice == "scissors":
                    print ("Scissors cut paper, you lose!")
                    main_menu()

            elif user_choice == "scissors":
                if pc_choice == "rock":
                    print("Rock smashes scissors, you lose!")
                    main_menu()
                elif pc_choice == "paper":
                    print("Scissors cut paper, you win!")
                    main_menu()
                elif pc_choice == "scissors":
                    print ("Draw, try again...")
                    play()
        except Exception as e:
            print(f"An error occurred: {e}. Please enter a valid input")
            continue
                
def main_menu():
    print("Welcome to Rock, Paper, Scissors...")
    p = (input("Press F to play, Q to quit\n")).lower()
    while True:
        try:
            if p == 'f':
                play()
            elif p == 'q':
                print ("Quitting the game...")
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please enter a valid input")
            continue

main_menu()
