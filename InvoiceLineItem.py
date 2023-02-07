#Sean Holbrook
#CIS261
#Invoice Line Item Calculator

print("Welcome to the Invoice Line Item Calculator Program")

#function prompting user to entire price as a float, else reject

def user_price():
    while True:
        try:
            price = float(input("Enter a price as a decimal: "))
            return price
        except ValueError:
            print("Invalid format, try again please.")
           

#function to prompt user to enter a quantity as an integer, else reject

def user_quantity():
    while True:
        try:
            quantity = int(input("Enter a quantity: "))
            return quantity
        except ValueError:
            print("Invalid format, try again please.")


#assign function return values to variables
price = user_price()
quantity = user_quantity()

#function to compute total and print format

def user_totals():
    total = (price * quantity)
    print(f"PRICE:   {price:.2f}")
    print(f"QUANTITY:   {quantity}")
    print(f"TOTAL:   {total:.2f}")
    print()
        

#the program running
user_totals()
again = input("Do you want to try again(y/n)?: ")
while again.lower() == "y":
    price = user_price()
    quantity = user_quantity()
    user_totals()
    again = input("Do you want to try again(y/n)?: ")


print("Bye!")
    
