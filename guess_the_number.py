import random

def register():
    print("REGISTER YOURSELF--------------->")
    username = input("CREATE USERNAME: ")
    password = input("CREATE PASSWORD: ")
    user = {"username": username,
        "password": password}

    print("REGISTRATION SUCCESSFUL!!!!")
    return user

def login(user):

    print("LOGIN YOURSELF----------------->")

    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")

    if username == user["username"] and password == user["password"]:

        print("LOGIN SUCCESSFUL!!!!")
        return True

    else:

        print("INVALID USERNAME OR PASSWORD")
        return False   

def game():
    print("GAME STARTS--------------------->")
    n = random.randint(1,100)
    attempts = 1
    while True:
        num = int(input(f"MAKE YOUR GUESS [ATTEMPT - {attempts}]:"))
        if num == n:
            attempts+=1
            print("CONGRATULATIONS!!!! YOU GUESSED IT RIGHT IN",attempts,"ATTEMPTS")
            break
        elif num>n:
            attempts+=1
            print("YOUR GUESS IS HIGHER")
        elif num<n:
            attempts+=1
            print("YOUR GUESS IS LOWER")
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

                    game()

                elif choice.lower() == "n":

                    print("\nTHANK YOU FOR PLAYING!!!!")
                    return            
         
main()                 