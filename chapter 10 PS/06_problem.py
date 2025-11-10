from random import randint

class Train:
    def __init__(slf,trainNo):
          slf.trainNo = trainNo # nothing will happened if you change self to slf

    def book(harry,fro,to):
        print(f"ticket is booked in train no: {harry.trainNo} from {fro} to {to}") # nothing will happened if you change self to harry
    
    def getstatus (self):
        print(f"train no: {self.trainNo} is running on time!")
    
    def fare (self,fro,to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint (222,888)} rupess")

t = Train(12978)
t.book("Rampur","Ajmer")
t.getstatus()
t.fare("Rampur","Ajmer")
    