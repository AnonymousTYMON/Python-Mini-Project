import random
answer = random.randint(0,100)
time = int(0)
print("Welcome to the Number Guess")
print(answer)
correct = False
while correct ==False:
    guess = (input("Guess a number between 0 to 100: "))
    try:
        val = int(guess)
    except ValueError:
        print("This is not a valid integer. PLease try again")
        time -= 1
        continue
    val =int(guess)
    time += 1
    if val < 0 or val > 100:
        print("It is out of range. Please try again.")
        time -= 1
    if val == answer:
        correct = True
    if val > answer:
        print("This is higher than actual number. Please try again.")
    if val < answer:
        print("This is lower than actual number. Please try again.")
if correct == True:
    print("It is correct!")
    print("Number of guessing: "+ str(time))
    
