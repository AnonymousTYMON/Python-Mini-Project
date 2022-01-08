def player1():
    print("Player1 turn")
    location()
    global board
    board[3-y][x-1] = "X"

def player2():
    print("Player2 turn")
    location()
    global board
    board[3-y][x-1] = "O"

def location():
    global x
    global y
    correct = False
    while correct == False:
        x = int(input("X-coordinates: "))
        y = int(input("Y-coordinates: "))
        correct = False
        if 0 < x <= 3 and 0 < y <= 3:
            correct = True
        else:
            print("Out of range, try again")
            x = input("X-coordinates: ")
            y = input("Y-coordinates: ")
        if board[3-y][x-1] == "O" or board[3-y][x-1] == "X":
            correct = False
            print("This place is occupied, try again")

def check(occupied, player1_occupied, player2_occupied):
    global game_over
    global player1_win
    global player2_win
    for i in range(0,3):
        for i2 in range (0,3):
            if board[i][i2] != "■":
                occupied += 1
    if occupied == 9:
        game_over = True
    for i in range(0,3):
        if board[i] == ["X","X","X"]:
            game_over = True
            player1_win = True
        if board[i] == ["O","O","O"]:
            game_over = True
            player2_win = True
    for i2 in range(0,3):
        if board[i2][2-i2] == "X":
            player1_occupied += 1
        if board[i2][2-i2] == "O":
            player2_occupied += 1
        if player1_occupied == 3:
            game_over = True
            player1_win = True
        if player2_occupied == 3:
            game_over = True
            player2_win = True
    player1_occupied = int(0)
    player2_occupied = int(0)
    for i5 in range(0,3):
        if board[i5][i5] == "X":
            player1_occupied += 1
        if board[i5][i5] == "O":
            player2_occupied += 1
        if player1_occupied == 3:
            game_over = True
            player1_win = True
        if player2_occupied == 3:
            game_over = True
            player2_win = True
    player1_occupied = int(0)
    player2_occupied = int(0)
    for i3 in range(0,3):
        for i4 in range (0,3):
            if board[i4][i3] == "X":
                player1_occupied += 1
            if board[i4][i3] == "O":
                player2_occupied += 1
        if player1_occupied == 3:
            player1_win = True
            game_over = True
        if player2_occupied == 3:
            player2_win =True
            game_over = True
        player1_occupied = 0
        player2_occupied = 0

def game():
    print(f"3 {board[0]}\n2 {board[1]}\n1 {board[2]}\n    1    2    3")
    player1()
    check(occupied, player1_occupied, player2_occupied)
    if game_over == False:
        print(f"3 {board[0]}\n2 {board[1]}\n1 {board[2]}\n    1    2    3")
        player2()
        check(occupied, player1_occupied, player2_occupied)

board = [
    ["■","■","■"],
    ["■","■","■"],
    ["■","■","■"]
    ]

game_over = False
x = int()
y = int()
player1_occupied = int(0)
player2_occupied = int(0)
player1_win = False
player2_win = False
occupied = int(0)
print("Tic-Tac-Toe")
while game_over == False:
    game()
print(f"3 {board[0]}\n2 {board[1]}\n1 {board[2]}\n    1    2    3")
if player1_win == True:
    print("Player1 win!")
elif player2_win == True:
    print("Player2 win!")
else:
    print("Draw")
