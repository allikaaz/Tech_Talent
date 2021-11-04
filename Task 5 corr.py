num_1 = int(input("kindly enter your first number"))
num_2 = int(input("kindly enter your second number"))
user_sign = input("please enter any operator of your choice among these (+, -, /,*,**,%,//) ")
if user_sign == "+":
    print(num_1 + num_2)
elif user_sign == "-":
    print(num_1-num_2)
elif user_sign == "*":
    print(num_1*num_2)
elif user_sign == "/":
    print(num_1/num_2)
elif user_sign == "**":
    print(num_1**num_2)
elif user_sign == "%":
    print(num_1 % num_2)
elif user_sign == "//":
    print(num_1//num_2)
else:
    print("Inappropriate sign was entered !") 