user_numb2 = int(input("Enter any number of your choice"))
if user_numb2 < 10:
    print("Number is smaller than 10")
else:
    print("The number is greater than 10") 
while user_numb2 < 10:
    print("The Number is now: "+str(int(user_numb2))+ " ")
    user_numb2 = user_numb2 + 1 