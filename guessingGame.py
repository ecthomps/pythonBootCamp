import random

compNum = random.randint(1,10);

while True:
    userNum = int(input("Guess a number between 1 and 10: "))
    if userNum > compNum:
        print("Too high, try again!")
    elif userNum < compNum:
        print("Too low, try again!")
    else:
        print("YOU GOT IT!")
        userResp = input("Do you want to play again? (Y/N) ")
        if userResp[0] == "Y":
            compNum = random.randint(1,10)
            userNum = None
        else: 
            print("Thank you for playing!")
            break
