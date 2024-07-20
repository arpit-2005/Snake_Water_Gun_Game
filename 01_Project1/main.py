'''
step 1 = computer choice and user choice
step 2 = logic build 
step 3 = winner declare 
step 4 = want to play again or not

'''
print("WELCOME TO THE GAME.\nENJOY THE GAME.")
def game():
    
    import random

    choices = ["snake","water","gun"]
    computer_choice = random.choice(choices)
    print(choices)
    your_choice = input("Enter your choice from the above list: ").lower()
    if your_choice not in choices:
        print("Enter a valid choice")
        return
    else:
        print(end="")

    print(f"you choose: {your_choice}\ncomputer choose: {computer_choice}")

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


    play_again = input("Do you want to play again?\nChoose one from yes or no:").lower()
    if play_again=="no":
        print("Thanks for playing the game.\nCome again Whenever you feel to play this game.")
    else:
        print("WELCOME AGAIN\nENJOY THE GAME")
        game()    
        
game()
        







