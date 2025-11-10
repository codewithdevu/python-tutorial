import random

# computer Randomly pick a number
computer = random.choice([-1,1,0])
yourstr = input("Enter your choice: ")
yourdict = {"st":1,"p":-1,"si":0}     
reversedict = {1:"stone",-1:"paper",0:"sizzer"}

you = yourdict[yourstr]

print(f" You choose: {reversedict[you]}  \n Computer choose: {reversedict[computer]}")

"divyansh /n yadav"

if (computer==you):
    print("ITS DRAW!")

else:
    if ( computer-you == -2 or computer-you == 1):
        print("YOU LOSE!")

    else:
        print("YOU WIN!")

StopIteration