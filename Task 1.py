import random
RandNumb = random.randint(1,10)
print("Well I am thinking of a number between 1 and 10")
Name = input("Before we begin the task, tell me your name")
print("My name is "+ Name +" ")
print("Good name! "+ Name +" ")
guess = int(input("Take a guess of any number "+ Name +" "))
if guess == 6:
    print("Good job "+ Name + "! you guessed my number")
else:
    print("Wrong number, better luck next time")