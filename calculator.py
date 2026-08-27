def calculator():
    while True:
        n = int(input("Enter any number:"))

        if not (1 <= n <= 9):
            print("Invalid Input")
        else:
            ch = input("Do you want to calculate (y/n):")

            if ch == 'y':
                a = input("Enter your operator:")
                num = int(input("Enter your second number:"))

                if a == '+':
                    total = n + num
                elif a == '-':
                    total = n - num
                elif a == '*':
                    total = n * num
                elif a == '/':
                    total = n / num
                else:
                    print("Invalid operation")
                    continue

                print("The result of the operation is:", total)

            elif ch == 'n':
                print("Thank you for using calculator")
                break

calculator()