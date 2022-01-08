import random
print("Dice Rolling Simulator, how many dices?")
no_dice = int(input())
done = False
while done == False:
    correct_input = False
    print("Shaking dice...")
    for i in range(0, no_dice):
        print(random.randint(1,6), end=" ")
    while correct_input == False:
        again = str(input("\nShake again?(Y/N)"))
        if again == str("N") or again == str("n"):
            done = True
            correct_input = True
        if again == str("Y") or again == str("y"):
            correct_input = True
        if again != str("N") and again != str("Y") and again != str("y") and again != str("n"):
            print("Plz input Y or N!!!")
print("Finish")
