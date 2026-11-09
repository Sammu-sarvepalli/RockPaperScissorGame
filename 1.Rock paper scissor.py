print("Let's play Rock,Paper,Scissors Game!")
import random
options = ("rock", "paper", "scissor")
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter your choice \nrock, paper, scissor : ")
    print(f"player: {player}")
    print(f"computer: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissor" and computer == "paper":
        print("you win!")
    else:
        print("computer win!")

    play_again = input("play again? (y/n):").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing")
