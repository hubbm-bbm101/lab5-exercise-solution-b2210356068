#exercise3
import random
number=random.randint(1,100)
guess=(int(input("Please guess the number : ")))

while guess!=number :
    if guess<number:
     guess=int(input("Increase your number "))
    elif  guess>number :
     guess=int(input("Decrease your number "))
else :
    print("CONGRATS")