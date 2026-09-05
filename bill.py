products = {
    1: ["Pen", 10],
    2: ["Notebook", 50],
    3: ["Bag", 500],
    4: ["Bottle", 200],
    5: ["Calculator", 800]
}

cart = []

print("====== WELCOME TO THE SHOP ======")

while True:

    print("\nAvailable Products:")

    for number in products:
        print(number, ".", products[number][0], "- ₹", products[number][1])

    print("0. Finish Shopping")

    choice = int(input("\nEnter product number: "))

    if choice == 0:
        break

    if choice in products:

        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            cart.append([choice, quantity])
            print("Added to cart!")

        else:
            print("Invalid quantity!")

    else:
        print("Invalid product number!")


# BILL
print("\n========== BILL ==========")

total_bill = 0

for purchase in cart:

    product_number = purchase[0]
    quantity = purchase[1]

    product_name = products[product_number][0]
    price = products[product_number][1]

    total = price * quantity

    print(product_name, "x", quantity, "=", total)

    total_bill = total_bill + total


print("--------------------------")
print("Total Bill: ₹", total_bill)


# DISCOUNT
if total_bill > 1000:

    discount = total_bill * 10 / 100
    print("Discount: 10%")

elif total_bill >= 500:

    discount = total_bill * 5 / 100
    print("Discount: 5%")

else:

    discount = 0
    print("Discount: No Discount")


final_bill = total_bill - discount

print("Discount Amount: ₹", discount)
print("Final Bill: ₹", final_bill)

print("==========================")
print("Thank You! Visit Again!")