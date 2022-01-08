import random
print("Number Guessing")
chance = int(input("Input the number of guess:"))
lowest = int(input("Input the lowest range(Minimum: 1):"))
highest = int(input("Input the highest range(Maximum: 3000):"))
ans = int(random.randint(lowest, highest))
chance_used = int(0)
correct = False
game = False
while game == False:
    guess = int(input(str(lowest) + " - " + str(highest) + ", Guess the number:"))
    if guess == ans:
        correct = True
        game = True
    if guess != ans:
        if guess < lowest or guess > highest:
            print("Out of the range!!!")
            chance_used -= 1
        chance_used += 1
        if guess > lowest and guess < ans:
            lowest = guess
        if guess < highest and guess > ans:
            highest = guess
        if chance - chance_used == 1:
            print("The last chance!!!")
        if chance == chance_used:
            game = True
if correct == True:
    print("You win the game!!!")
if correct == False:
    print("It is " + str(ans) + ". You lose the game!!!")

