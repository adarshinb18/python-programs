class Bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("Amount deposited sucessfully")
        return self.bal
    def withdraw(self,amount):
        if amount>self.bal:
            print("insufficient balance")
            return self.bal
        else:
            self.bal=self.bal-amount
            print("Amount withdraw sucessfully")
            return  self.bal
b=Bank(1001,"aru","savings",3000)
dpamound=float(input("enter the amound to be deposited"))
print("account balance is:",b.deposit(dpamound))
wdamound=float(input("enter the amound to be withdraw"))
print("account balance is:",b.withdraw(wdamound))