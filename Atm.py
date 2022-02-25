class Atm(object):

    def __init__(self, card_no, pin_no):
        self.card_no = card_no
        self.pin_no = pin_no
        self.bal = "xyz"

    def CashWithdrawal(self):
        print("Cash Withdrawn")

    def BalanceEnquiry(self):
        print("Balance =",self.bal)

    def CashDeposition(self):
        print("Cash Deposited")

Pnb = Atm("xxxxxxxxxxxx2598", "xxxx")
i = 0
while i != -1:
    num = int(input("Enter the work \n1.Cash Withdrawal \n2.Cash Deposition \n3.Balance \n-1.Ext \n: "))
    if num==1:
        Pnb.CashWithdrawal()
    elif num==2:
        Pnb.CashDeposition()
    elif num==3:
        Pnb.BalanceEnquiry()
    elif num==-1:
        break
    else:
        print("Invalid")