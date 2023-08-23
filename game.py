import random
#the while loop is to enable us ask if the player will play again
while True:
    pick = ["rock", "papar", "scissor"]
    #computer choice
    computer = random.choice(pick)

    #initerlizing player
    player = None

    #players choice
    while player not in pick:
        player = input("rock, papar, scissor: ").lower()
        if player != ("rock, papar, scissor"):
            print("invalid option DUMMY!!!!")

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("it's a tie")
    elif player == "rock":
        if computer == "papar":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose: ")
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("you win: ")
    elif player == "scissor":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose: ")
        if computer == "papar":
            print("computer: ", computer)
            print("player: ", player)
            print("you win: ")
    elif player == "papar":
        if computer == "scissor":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose: ")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win: ")
    play_again = input("will you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("thanks for playing! ")




