
import random

#user information
accounts={}
def creat_account():
    account_number= random.randint(1000000000, 9999999999)
    if account_number in accounts:

        print("account number is alredy exists!.try again.")
    
        return
    name=input("enter user name:")

initiol_balance=float(input(""))

   




user_name =input("enter your name :")
print(user_name.isalpha())
user_NIC_number=input("enter your NIC number :")
    return
#creat_account_number


account_number=print(account_number)


# admin menu bar=======================

print("=====MENU=====")
print("1.creat a account")
print("2.deposit money")
print("3.withdraw money")
print("4.check balance")
print("5.transaction history")
print("6.exit.")

choice=input("choose 1-4 option")
    if choice=="1":
        creat_account()
        elif choice=="2":
            deposit_money()
        elif choice=="3"
            withdraw_money()
        elif choice=="4"
            check_balance()
        elif choice=="5"
            transaction_history()
        elif choice=="6"
            print("exiting programe. thank you for using our service!")
            break
        else:
            print("invalid option. try again!")    


    
main()
