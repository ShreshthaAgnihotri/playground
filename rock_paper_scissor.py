import random
print("------------------------------- ROCK PAPER SCISSORS----------------------------------" )

def register():

    print("REGISTER YOURSELF--------------->")
    username = input("CREATE USERNAME: ")
    password = input("CREATE PASSWORD: ")
    user = {"username": username,
        "password": password}

    print("REGISTRATION SUCCESSFUL!!!!")
    return user

def login(user):

    print("LOGIN YOURSELF------------------->")
    A = input("ENTER YOUR USERNAME: ")
    B = input("ENTER YOUR PASSWORD: ")
    if A == user["username"] and B == user["password"]:

        print("LOGIN SUCCESSFUL!!!!")
        return True

    else:

        print("INVALID USERNAME OR PASSWORD")
        return False   

def game(username):

    print("GAME BEGINS---------------------->")
    while True:
        n = random.randint(1,3)
        c = input("ENTER YOUR CHOICE (ROCK/PAPER/SCISSORS):")
        if c not in ["ROCK", "PAPER", "SCISSORS"]: 
            print("INVALID CHOICE!!!!") 
            continue
        mychoice = ''
        if n == 1:
            mychoice = "ROCK"
        elif n == 2:
            mychoice = "PAPER"
        else :
            mychoice = "SCISSORS"
        if c == "ROCK" and mychoice == "SCISSORS":
            print("I HAD SCISSORS!!!!! YOU WON ",username)
        elif c == "ROCK" and mychoice == "PAPER":
            print("OHHH!!! I HAD PAPER , YOU LOST")
        elif c == "PAPER" and mychoice == "SCISSORS":
            print("OHHH!!! I HAD SCISSOR , YOU LOST")    
        elif c == "SCISSORS" and mychoice == "ROCK":
            print("OHHH!!! I HAD ROCK , YOU LOST")
        elif c == "PAPER" and mychoice == "ROCK":
            print("I HAD ROCK!!!!! YOU WON ",username)
        elif c == "SCISSORS" and mychoice == "PAPER":
            print("I HAD PAPER!!!!! YOU WON ",username)
        elif c == "ROCK" and mychoice == "ROCK":
            print("AHHH!!!!! IT'S A TIE")
        elif c == "PAPER" and mychoice == "PAPER":
            print("AHHH!!!!! IT'S A TIE")  
        elif c == "SCISSORS" and mychoice == "SCISSORS":
            print("AHHH!!!!! IT'S A TIE")
        again = input("\nDO YOU WANT TO PLAY AGAIN? (Y/N): ")
        if again.lower() == "n": 
            break  

def main():

    print("========================================")
    print("          WELCOME TO THE GAME             ")
    print("========================================")

    user = register()

    while True:

        if login(user):

            while True:

                choice = input("\nDO YOU WANT TO CONTINUE? (Y/N): ")

                if choice.lower() == "y":

                    game(user["username"])

                elif choice.lower() == "n":

                    print("THANK YOU FOR PLAYING!!!!")
                    return            
         
main()                         


        





