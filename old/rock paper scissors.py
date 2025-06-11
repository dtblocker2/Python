import random
while True:
    lol = ["rock", "paper", "scissors"]
    player = input("enter your choice: ")
    computer = random.choice(lol)
    print("computer choice: " + computer)

    if player == "rock":
        if computer == "rock":
            print("its a tie")
        if computer == "paper":
            print("computer won")
        if computer == "scissors":
            print("you won")
    elif player == "paper":
        if computer == "paper":
            print("its a tie")
        if computer == "scissors":
            print("computer won")
        if computer == "rock":
            print("you won")
    elif player == "scissors":
        if computer == "scissors":
            print("its a tie")
        if computer == "rock":
            print("computer won")
        if computer == "paper":
            print("you won")
    elif player == "gun":
        print("you win by a large margin")
    else:
        print("enter a valid choice")

    play_again = input("do you want to play again? ")
    if play_again == "no":
        break

print("thanks for playing game with me")