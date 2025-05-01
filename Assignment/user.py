def
while True:
    print("1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Transaction history")
    print("6.Exit")

    choose = input("choose the number(1-6)")
    if choose == 1:
        print("Create your Account")
        Acc_number =1001
        Account_number = int(input("Enter account_num"))
        Holder_name = input("Enter your name")
        Initial_balance = int(input("Enter the balance"))

        if Account_number == Acc_number:
            print("Already exist")  
        else:
            print("successfully created account")

'''
    if choose == :
        print("Your balance is (balance)")

    elif choose == 2:
        amount = int(input("enter your amount "))

        if amount <= balance:
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
'''
    elif choose == 2:
        Deposit_money = int(input("enter your amount "))
        balance = balance + Deposit_money
        print("Deposit Successfull , your balance is (balance)")

    elif choose == 4:
        print("Thankyou")
        break

    else:
        print("choose any numbers")


