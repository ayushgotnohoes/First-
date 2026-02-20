import random

comp = random.randint(1, 3)
urStr = input("Enter your choice: ")
urDict = {"r":1,"p":2,"s":3}
revstring = {1:"rock",2:"paper",3:"scissor"}

you = urDict[urStr]

print(f"U chose {revstring[you]} \nComp chose {revstring[comp]}")

if comp == you:
    print("Its a tie")
elif comp == 1 and you == 2:
        print("U won!")
elif comp == 1 and you == 3:
        print("u lost")
elif comp == 2 and you == 1:
        print("u lost")
elif comp == 2 and you == 3:
        print("u lost")
elif comp == 3 and you == 1:
        print("u lost")
elif comp == 3 and you == 2:
        print("u lost")
else:
        print("Something went wrong!")