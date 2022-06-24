import random
x = True
a = 0
b = 0

while x:
    Roll = random.randint (1,3)
    Guess = input ("\nRock, Paper, or Scissors:\n\n")

    if Roll == 1:
        comproll = "Rock"
    if Roll == 2:
        comproll = "Paper"
    if Roll == 3:
        comproll = "Scissors"
    print ("\nComputer Rolls:", comproll)


    if Guess == ("Rock"):
        Userguess = 1
        if Roll == 2:
            print ("Lose")
            b+= 1
        elif Roll == 3:
            print ("Win")
            a+= 1
        elif Roll == 1:
            print ("tie")

    elif Guess == ("Paper"):
        Userguess = 2
        if Roll == 3:
            print ("Lose")
            b+= 1
        elif Roll == 1:
            print ("Win")
            a+= 1
        elif Roll == 2:
            print ("tie")

    elif Guess == ("Scissors"):
        Userguess = 3
        if Roll == 1:
            print ("Lose")
            b+= 1
        elif Roll == 2:
            print ("Win")
            a+= 1
        elif Roll == 3:
            print ("tie")
    elif Guess != ("Rock" or "Paper" or "Scissors"):
        x = False
    print ("Computer's Wins:", b)
    print ("Your Wins:", a)
