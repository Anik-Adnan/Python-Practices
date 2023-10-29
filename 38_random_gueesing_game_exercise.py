#random number guess
import random
i=1
wining_number=random.randint(1,100) #random number between 1 -100
while True:
    n=int(input("Guess number between 1 to 10 :"))
    if n==wining_number:
        print(f"You win! in {i} times ")
        break
    else:
        if n<wining_number:
            print("Too low!!")
        else:
            print("Too High")
    i+=1
