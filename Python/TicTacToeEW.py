import random
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


def create_board(board):
    print("\t     |     |")
    print("\t  "+board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  "+board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  "+board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])
    print("\t     |     |")


x=0
create_board(theBoard)

team = input ("Would you like to play X or O: ")
if team == 'X':
    player1 = 'X'
    player2= 'O'
elif team == 'O':
    player1 = "O"
    player2 = 'X'
else:
    print("Sorry Try again")
    team = input ("Would you like to play X or O: ")



while x<9:

    user = input("\nChoose your tile: ")
    #Converting Integer into string for dictionary to be able to register
    user2 = random.randint (1,9)
    comp = str(user2)

    if theBoard[user] == " ":
        theBoard[user] = player1
        x+=2
    else:
        print("\nThe tile is already taken try again")

    if x<9:
        while theBoard[comp] != " ":
            user2 = random.randint (1,9)
            comp = str(user2)

        else:
            theBoard[comp] = player2

    create_board(theBoard)




    if team == 'X':
        if x >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] == 'X': # across the top
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] == 'X': # across the middle
                create_bord(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] == 'X': # across the bottom
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] == 'X': # down the left side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] == 'X': # down the middle
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] == 'X': # down the right side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] == 'X': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] == 'X': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break

            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != 'X': # across the top
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != 'X': # across the middle
                create_bord(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != 'X': # across the bottom
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != 'X': # down the left side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != 'X': # down the middle
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != 'X': # down the right side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != 'X': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != 'X': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break




    if team ==  'O':
        if x>=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] == 'O': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] == 'O': # across the middle
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] == 'O': # across the bottom
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] == 'O': # down the left side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] == 'O': # down the middle
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] == 'O': # down the right side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] == 'O': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] == 'O': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Win")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != 'O': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != 'O': # across the middle
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != 'O': # across the bottom
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != 'O': # down the left side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != 'O': # down the middle
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != 'O': # down the right side
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != 'O': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != 'O': # diagonal
                create_board(theBoard)
                print("\nGame Over.\n")
                print("You Lose")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if x == 9:
        print("\nGame Over.\n")
        print("It's a Tie!!")
