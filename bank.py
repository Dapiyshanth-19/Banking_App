balance=50000


def withdraw():
    global balance
    ammount=int(input("enter the ammount :"))
    balance=balance-ammount
    print("withdraw ammount is :",ammount)
    print("new balanceis :",ammount)

withdraw()
'''''