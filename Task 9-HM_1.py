num_1 = int(input("kindly enter your first number"))
num_2 = int(input("kindly enter your second number"))
user_sign = input("please enter any operator of your choice: a to Add, b to Subtract, c to Multiply, d to Divide, e for exponential, f to ")
if user_sign == "a":
    print(num_1 + num_2)
elif user_sign == "b":
    print(num_1-num_2)
elif user_sign == "c":
    print(num_1*num_2)
elif user_sign == "d":
    print(num_1/num_2)
elif user_sign == "e":
    print(num_1**num_2)
elif user_sign == "f":
    print(num_1 % num_2)
elif user_sign == "g":
    print(num_1//num_2)
else:
    print("Inappropriate letter was entered !") 