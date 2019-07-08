game_board = [[1,2,3],
              [4,5,6],
              [7,8,9]]
def showboard():
    for row in game_board:
        print(row)
def start():
    showboard()
    print("Please type the name of the first player along with surname if you like xD")
    global name1
    name1 = input()
    print("The name of the first player is " + name1)
    showboard()
start()
def everthing1():
    print("Please type where " + name1 +  " want to place on the board")
    input1 = int(input())
    if input1 == game_board[0][0] :
        game_board[0][0] = "X"
    elif input1 == game_board[0][1]:
        game_board[0][1] ="X"
    elif input1 == game_board[0][2]:
        game_board[0][2] = "X"
    elif input1 == game_board[1][0]:
        game_board[1][0] = "X"
    elif input1 == game_board[1][1]:
        game_board[1][1] = "X"
    elif input1 == game_board[1][2]:
        game_board[1][2] = "X"
    elif input1 == game_board[2][0]:
        game_board[2][0] = "X"
    elif input1 == game_board[2][1]:
        game_board[2][1] = "X"
    elif input1 == game_board[2][2]:
        game_board[2][2] = "X"
    showboard()
everthing1()
def start2():
    print("Please type the name of the second player wants also the surname is you want! xD")
    global name2
    name2 = input()
    print("The name of the second player is " + name2)
start2()
def everthing2():
    print("It is now the chance of " + name2)
    showboard()
    input2 = int(input())
    if input2 == game_board[0][0]:
        game_board[0][0] = "O"
    elif input2 == game_board[0][1]:
        game_board[0][1] = "O"
    elif input2 == game_board[0][2]:
        game_board[0][2] = "O"
    elif input2 == game_board[1][0]:
        game_board[1][0] = "O"
    elif input2 == game_board[1][1]:
        game_board[1][1] = "O"
    elif input2 == game_board[1][2]:
        game_board[1][2] = "O"
    elif input2 == game_board[2][0]:
        game_board[2][0] = "O"
    elif input2 == game_board[2][1]:
        game_board[2][1] = "O"
    elif input2 == game_board[2][2]:
        game_board[2][2] = "O"
    showboard()

def logic1():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][1] == "X":
        print(name1 + " has one  Congratulations!!")

    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")

    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print(name1 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
def logic2():
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][1] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")

    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print(name2 + " has oneCongratulations!!")
    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")

    elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")
    elif game_board[0][2] == "O" and game_board[1][2] == "X" and game_board[2][2] == "O":
        print(name2 + " has one Congratulations!! GAME OVER!!!!!!!!!!!!!")

everthing2()
logic2()

everthing1()
logic1()

everthing2()
logic2()

everthing1()
logic1()

everthing2()
logic2()
#logic 1.0
logic1()
#logic 2.0

logic2()
