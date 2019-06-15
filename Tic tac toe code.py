from playsound import *



game_board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

def show_board():
    for row in game_board:
        print(row)
show_board()

print("Please Type the name of the first player")
name1 = input()
print("Welcome to the game " + name1 + "!")

print("Type the place where " + name1 + " wants to place on")
show_board()
 # why tho
position1 = int(input())

def plotting_x():
    if position1 == game_board[0][0]:
        game_board[0][0] = "X"
        show_board()
    elif position1 == game_board[0][1]:
        game_board[0][1] = "X"
        show_board()
    elif position1 == game_board[0][2]:
        game_board[0][2] = "X"
        show_board()
    elif position1 == game_board[1][0]:
        game_board[1][0] = "X"
        show_board()
    elif position1 == game_board[1][1]:
        game_board[1][1] = "X"
        show_board()
    elif position1 == game_board[1][2]:
        game_board[1][2] = "X"
        show_board()
    elif position1 == game_board[2][0]:
        game_board[2][0] = "X"
        show_board()
    elif position1 == game_board[2][1]:
        game_board[2][1] = "X"
        show_board()
    elif position1 == game_board[2][2]:
        game_board[2][2] = "X"
        show_board()
plotting_x()

print("Please Type the name of the second player")
name2 = input()
print("Welcome to the game " + name2 + "!")

print("Type the place where " + name2 + " wants to place")
show_board()


position2 = int(input())

def plotting_y():
    if position2 == game_board[0][0]:
        game_board[0][0] = "Y"
        show_board()
    elif position2 == game_board[0][1]:
        game_board[0][1] = "Y"
        show_board()
    elif position2 == game_board[0][2]:
        game_board[0][2] = "Y"
        show_board()
    elif position2 == game_board[1][0]:
        game_board[1][0] = "Y"
        show_board()
    elif position2 == game_board[1][1]:
        game_board[1][1] = "Y"
        show_board()
    elif position2 == game_board[1][2]:
        game_board[1][2] = "Y"
        show_board()
    elif position2 == game_board[2][0]:
        game_board[2][0] = "Y"
        show_board()
    elif position2 == game_board[2][1]:
        game_board[2][1] = "Y"
        show_board()
    elif position2 == game_board[2][2]:
        game_board[2][2] = "Y"
        show_board()
plotting_y()

print("It is now the chance of " + name1)
position1 = int(input())
plotting_x()
#-----------------------------------------------------------------------------------------------------------------
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diagnol win

if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
# the above is vertical win
if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is horizontal win
else:
    print("It is now the chance of " + name2)
    position2 = int(input())
    plotting_y()
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diganol win
elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is vertical win
if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is horizontal win
else:
    print("It is now the chance of " + name1)
    position1 = int(input())
    plotting_x()
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diagnol win

if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is vertical win

if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is vertical win
else:
    print("It is now the chance of " + name2)
    position2 = int(input())
    plotting_y()


#Diagnol win only
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )

if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + "wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

# -----------------------------------------------------------------------------

#vertical win only
if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

#horizontal win only

if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "Y" and game_board[2][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#---------------------------------------------------------------------------------------------------------------------------------------------

name1
plotting_x()

if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diagnol win

if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
# the above is vertical win
if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is horizontal win
else:
    print("It is now the chance of " + name2)
    position2 = int(input())
    plotting_y()
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diganol win
elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is vertical win
if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is horizontal win
else:
    print("It is now the chance of " + name1)
    position1 = int(input())
    plotting_x()
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diagnol win

if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is vertical win

if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is vertical win
else:
    print("It is now the chance of " + name2)
    position2 = int(input())
    plotting_y()



name2
plotting_y()


if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diagnol win

if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
# the above is vertical win
if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is horizontal win
else:
    print("It is now the chance of " + name2)
    position2 = int(input())
    plotting_y()
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diganol win
elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is vertical win
if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is horizontal win
else:
    print("It is now the chance of " + name1)
    position1 = int(input())
    plotting_x()
if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" +" wins CONGRATS!" )
elif game_board[0][0] == "Y" and game_board[1][1] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" +" wins congrats!" )
elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][1] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is diagnol win

if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[1][0] == "Y" and game_board[2][0] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][1] == "Y" and game_board[1][1] == "Y" and game_board[2][1] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][2] == "Y" and game_board[1][2] == "Y" and game_board[2][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")
#the above is vertical win

if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[0][0] == "Y" and game_board[0][1] == "Y" and game_board[0][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[1][0] == "Y" and game_board[1][1] == "Y" and game_board[1][2] == "Y":
    print("Strike " + name2 + "" + " wins CONGRATS!")

elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
    print("Strike " + name1 + "" + " wins CONGRATS!")
#the above is vertical win
else:
    print("It is now the chance of " + name2)
    position2 = int(input())
    plotting_y()



