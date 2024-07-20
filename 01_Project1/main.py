# welcoming the user
print("WELCOME TO THE GAME.\nENJOY THE GAME.")

# defining the function 
def game():
    #importing random 
    import random

    choices = ["snake","water","gun"]
    
    # creating computer choice
    computer_choice = random.choice(choices)
    print(choices)
    
    # creating user choice
    your_choice = input("Enter your choice from the above list: ").lower()
    if your_choice not in choices:
        print("Enter a valid choice")
        return
    else:
        print(end="")
    
    # displaying the choice of both players
    print(f"you choose: {your_choice}\ncomputer choose: {computer_choice}")


    # building the logic of the game
    if (computer_choice == your_choice):
        print("its a draw!")
    else:
        if (computer_choice=="snake" and your_choice=="water"):
            print("you loose")

        elif (computer_choice=="water" and your_choice=="gun"):
            print("you loose")

        elif (computer_choice=="gun" and your_choice=="snake"):
            print("you loose")

        elif (computer_choice=="water" and your_choice=="snake"):
            print("you win")

        elif (computer_choice=="snake" and your_choice=="gun"):
            print("you win")

        elif (computer_choice=="gun" and your_choice=="water"):
            print("you win")

        else:
            print("something went wrong!")

    # asking the user if he wants to play again or not
    play_again = input("Do you want to play again?\nChoose one from yes or no:").lower()
    if play_again=="no":
        print("Thanks for playing the game.\nCome again Whenever you feel to play this game.")
    else:
        print("WELCOME AGAIN\nENJOY THE GAME")
        game() # calling the game() function  
        
game() # function call
        







