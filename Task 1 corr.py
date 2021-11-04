import random
RandNumb = random.randint(1,10)
print("Well I am thinking of a number between 1 and 10")
User_Name = input("Before we begin the task, tell me your name")
print("My name is "+ User_Name +" ")
print("Good name! "+ User_Name +" ")
guess = int(input("Take a guess of any number "+ User_Name +" "))
if RandNumb == guess:
    print("Good job "+ User_Name + "! you guessed my number")
else:
    print("You guess Wrongly, it was not: ", guess , "it was: ", RandNumb," better luck next time !")