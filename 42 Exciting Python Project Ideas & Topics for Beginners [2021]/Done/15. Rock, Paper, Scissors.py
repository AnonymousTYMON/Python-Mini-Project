import random
def paper(computer):
    if computer == "paper":
        draw(you)
    if computer == "scissors":
        lose()
    if computer == "stone":
        win(win_count, you)
def scissors(computer):
    if computer == "paper":
        win(win_count, you)
    if computer == "scissors":
        draw(you)
    if computer == "stone":
        lose()
def stone(computer):
    if computer == "paper":
        lose()
    if computer == "scissors":
        win(win_count, you)
    if computer == "stone":
        draw(you)
def user_move(you, correct1):
    if you.lower() != "paper" and you.lower() != "scissors" and you.lower() != "stone":
        correct1 = False
    while correct1 == False:
        you = str(input("Invalid input, plz try again\n"))
        if you.lower() == "paper" or you.lower() == "scissors" or you.lower() == "stone":
            correct1 = True
    computer = str(move[random.randint(0,2)])
    print("The computer pick " + computer)
    if you.lower() == "paper":
        paper(computer)
    if you.lower() == "scissors":
        scissors(computer)
    if you.lower() == "stone":
        stone(computer)
def draw(you):
    print("You draw, try again")
    you = str(input())
    user_move(you, correct1)
def win(you, correct2):
    print("You win!!!")
    global win_count
    win_count += 1
    print(win_count)
    you = str(input("Continue? (Y/N)\n"))
    correct2 = False
    if you.upper().strip("ESAO") == "N" or you.upper().strip("ESAO") == "Y":
        correct2 = True
    while correct2 == False:
        you = str(input("Yes or No (Y/N)\n"))
        if you.upper().strip("ESAO") != "N" and you.upper().strip("ESOA") != "Y":
            print("Invalid input, plz try again!\n")
        if you.upper().strip("ESAO") == "N" or you.upper().strip("ESAO") == "Y":
            correct2 = True
    if you.upper().strip("ESAO") == "N":
        end()
    if you.upper().strip("ESOA") == "Y":
        you = str(input("Your move?\n1.paper\n2.scissors\n3.stone\n"))
        user_move(you, correct1)
def lose():
    print("You lose!!!")
    end()
def end():
    print("The game ended\nWinning count: " + str(win_count))

move = [str("paper"), str("scissors"), str("stone")]
print("Play \"Paper, Scissors, Stone\" with the computer")
you = str(input("Your move?\n1.paper\n2.scissors\n3.stone\n"))
correct1 = True
win_count = 0
user_move(you, correct1)
