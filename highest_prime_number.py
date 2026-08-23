#This function takes a number as input and finds the highest prime digit in that number. If there are no prime digits, it informs the user accordingly.

def highest_prime_number():
    n = int(input("Enter a number:"))
    highest = 0
    while n>0:
        digit = n%10
        if digit>highest:
            if digit == 2 or digit ==3 or digit == 5 or digit == 7:
                highest = digit   
        n = n//10
    if highest == 0:
        print("There is no prime digit in the given number")
    else:
        print("The highest prime digit is:", highest)

highest_prime_number()


    







