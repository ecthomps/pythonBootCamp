print("...rock...\n...paper...\n...scissors...")

p1Choice = input("Enter Player 1's choice: ")
p2Choice = input("Enter Player 2's choice: ")

if p1Choice == "rock" and p2Choice == "paper":
    print("player2 wins")
elif p1Choice == "rock" and p2Choice == "scissors":
    print("player1 wins")
elif p1Choice == "paper" and p2Choice == "rock":
    print("player1 wins")
elif p1Choice == "scissors" and p2Choice == "rock":
    print("player2 wins")
elif p1Choice == "scissors" and p2Choice == "paper":
    print("player1 wins")
elif p1Choice == "paper" and p2Choice == "scissors":
    print("player2 wins")
else:
    print("We have a draw!")