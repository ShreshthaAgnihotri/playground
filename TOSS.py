import random
def toss():
    print("TOSSING A COIN")
    ans = "Y"
    while ans.upper() == "Y":
        ans = input("Do you want to toss the coin? (Y/N): ")
        if ans == "Y":
            print("TOSSING A COIN")
            coin = random.randint(0,1)
            if coin == 0:
                print("HEADS")
            else:
                print("TAILS")
        elif ans == "N":
            print("Thank you for playing!")
        else:
            print("Invalid input. Please enter Y or N.")
toss()