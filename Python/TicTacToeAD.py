import random


Continue = True





while Continue:

#Making grid
    Box =[*range(0,10,1)]
    def Grid():
        print (Box[1],"|", Box[2], "|", Box[3])
        print ("-----------")
        print (Box[4],"|", Box[5], "|", Box[6])
        print ("-----------")
        print (Box[7],"|", Box[8], "|", Box[9])

#X or O
    ToPlay = input ("Would you like to play tic tac toe?\n").lower()
    if ToPlay == ("yes"):
        Team = input ("Would you like X or O\n")
        if Team == ("x" or "X"):
            Team =1
        elif Team == ("o" or "O"):
            Team =2

        Grid()
        print("\n\n")
        j=0
#Placing X and O
        while j<=9:

            if Team == 1:

                RawPick = input ("Pick a number where you would like to place an X\n")


                #while RawPick not in range(0,10):
                    #RawPick = int(input ("Try another square\n"))
                    #print (RawPick)

                Pick = int(RawPick)
                while Box[Pick] not in range(1,10):
                    Pick = int(input("Try again\n"))
                Box[Pick] = ("X")
                j+=2


                if j<9:
                    BotPick = random.randint (1,9)
                    while Box[BotPick] not in range(1,9):
                        BotPick = random.randint (1,9)
                    Box[BotPick] = ("O")

                    Grid()


            elif Team == 2:


                BotPick = random.randint (1,9)
                while Box[BotPick] not in range(1,9):
                    BotPick = random.randint (1,9)
                Box[BotPick] = ("X")
                j+=1
                Grid()

                RawPick = input ("Pick a number where you would like to place an O\n")
                Pick = int(RawPick)
                while Box[Pick] not in range(1,10):
                    Pick = int(input("Try again\n"))
                Box[Pick] = ("O")
                j+=1





#win or lose for X
            if Team == 1:
                if Box[1]==Box[2]==Box[3]==("X"):
                    j+=10
                    print("Win")
                elif Box[4]==Box[5]==Box[6]==("X"):
                    j+=10
                    print("Win")
                elif Box[7]==Box[8]==Box[9]==("X"):
                    j+=10
                    print("Win")
                elif Box[1]==Box[4]==Box[7]==("X"):
                    j+=10
                    print("Win")
                elif Box[2]==Box[5]==Box[8]==("X"):
                    j+=10
                    print("Win")
                elif Box[3]==Box[6]==Box[9]==("X"):
                    j+=10
                    print("Win")
                elif Box[1]==Box[5]==Box[9]==("X"):
                    j+=10
                    print("Win")
                elif Box[3]==Box[5]==Box[7]==("X"):
                    j+=10
                    print("Win")
                elif Box[1]==Box[2]==Box[3]==("O"):
                    j+=10
                    print("Lose")
                elif Box[4]==Box[5]==Box[6]==("O"):
                    j+=10
                    print("Lose")
                elif Box[7]==Box[8]==Box[9]==("O"):
                    j+=10
                    print("Lose")
                elif Box[1]==Box[4]==Box[7]==("O"):
                    j+=10
                    print("Lose")
                elif Box[2]==Box[5]==Box[8]==("O"):
                    j+=10
                    print("Lose")
                elif Box[3]==Box[6]==Box[9]==("O"):
                    j+=10
                    print("Lose")
                elif Box[1]==Box[5]==Box[9]==("O"):
                    j+=10
                    print("Lose")
                elif Box[3]==Box[5]==Box[7]==("O"):
                    j+=10
                    print("Lose")
                elif j>=9:
                    print("Draw")



#win or lose for O

            if Team == 2:
                if Box[1]==Box[2]==Box[3]==("X"):
                    j+=10
                    print("Lose")
                elif Box[4]==Box[5]==Box[6]==("X"):
                    j+=10
                    print("Lose")
                elif Box[7]==Box[8]==Box[9]==("X"):
                    j+=10
                    print("Lose")
                elif Box[1]==Box[4]==Box[7]==("X"):
                    j+=10
                    print("Lose")
                elif Box[2]==Box[5]==Box[8]==("X"):
                    j+=10
                    print("Lose")
                elif Box[3]==Box[6]==Box[9]==("X"):
                    j+=10
                    print("Lose")
                elif Box[1]==Box[5]==Box[9]==("X"):
                    j+=10
                    print("Lose")
                elif Box[3]==Box[5]==Box[7]==("X3"):
                    j+=10
                    print("Lose")
                elif Box[1]==Box[2]==Box[3]==("O"):
                    j+=10
                    print("Win")
                elif Box[4]==Box[5]==Box[6]==("O"):
                    j+=10
                    print("Win")
                elif Box[7]==Box[8]==Box[9]==("O"):
                    j+=10
                    print("Win")
                elif Box[1]==Box[4]==Box[7]==("O"):
                    j+=10
                    print("Win")
                elif Box[2]==Box[5]==Box[8]==("O"):
                    j+=10
                    print("Win")
                elif Box[3]==Box[6]==Box[9]==("O"):
                    j+=10
                    print("Win")
                elif Box[1]==Box[5]==Box[9]==("O"):
                    j+=10
                    print("Win")
                elif Box[3]==Box[5]==Box[7]==("O"):
                    j+=10
                    print("Win")
                elif j>=9:
                    print("Draw")


    elif ToPlay == ("no"):
        Continue = False
