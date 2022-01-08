import random
library = ["python","tymon", "jenny"]
answer = str(random.choice(library))
print("Guess the word with " + str(len(answer)) + " letters" "(No capital letter)")
print("You have four chance")
chance = int(0)
correct = False
if answer == library[0]:
    print("Hint: the computer language now using")
if answer == library[1]:
    print("Hint: the code writer")
if answer == library[2]:
    print("Hint: the fake girl")
while correct == False:
    guess = str(input())
    if len(guess) > len(answer) or len(guess) < len(answer):
        print("Invalid input, it is not counted. Try again")
    if len(guess) == len(answer):
        if answer == guess:
            print("You are correct!!!")
            correct = True
        if answer != guess:
            chance += 1
            if chance != 4:
             for i in range(0, len(answer)):
                if answer[i] == guess[i]:
                    print(guess[i], end="")
                if answer[i] != guess[i]:
                    print("_", end="")
            print("\nYou are wrong, try again~")
        while chance == 4:
            print("NO more chance, you are loser!!!")
            chance += 1
            correct = True
