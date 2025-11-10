'''
1 fpr sizzer
-1 for stone
0 for paper

'''
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
    print("its draw!")

else:
    if(computer==-1 and you==1): #(computer - you == -2 )
        print("you lose!")

    elif(computer==-1 and you==0):#(computer - you == -1)
        print("you win!")

    elif(computer==0 and you==1):#(computer - you == -1)
        print("you win!")

    elif(computer==0 and you==-1):#(computer - you == 1)
        print("you lose!")

    elif(computer==1 and you==-1):#(computer - you == 2)
        print("you win!")

    elif(computer==1 and you==0):#(computer - you == 1 )
        print("you lose!")
     
    else:
        print("something went wrong")



    
