import random as rd

secretNum = rd.randint(1,100) 


print("welcome to guess the number game!")

tries = 0

while tries < 7:
    num = int(input("your number"))
    if secretNum < num:
        print("too long")
    elif secretNum > num:
        print("too short")
    else:
        print("Congratulation!")
        break
    tries = tries + 1
if tries == 7:
    print(f"unfotunately you lost, the secret number was {secretNum}")
