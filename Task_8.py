print("Welcome to PizzaHub Spot")
Psize = int(input("Enter your favourite pizza size between 8 -12 inches:"))
if Psize == 8:
    print("Here is your confirmation of size 8 inches Pizza !")
elif Psize == 10:
    print("Here is your confirmation of size 10 inches Pizza !")
elif Psize == 12:
    print("Here is your confirmation of size 12 inches Pizza !")
else:
    print("You entered wrong size inches for your Pizza !")
#print("Do you want extra topping on your Pizza please? ")
#yn = ["yes", "no"]
user_top = input(" Would you like extra toppings on your pizza?:")
if user_top == "yes":
    print("Toppings like fries/kebab will be added to your pizza!")
else:
    print("NO topping will be added")
print("How do you want to pay for your order please ? ")
payment = ["Card", "Cash"]
pay = input("Cash or Card ?")
if pay == payment[0]:
    print("Swipe in your card please !")
elif pay == payment[1]:
    print("Your cash please ?")
else:
    print("You have picked wrong option")