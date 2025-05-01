acc_num = int(input("Enter your account_number"))
name = input("Enter your namer")
balance = int(input("Enter your balancer"))


file = open('assignment.txt','a')
file.write(f"Your acc_num is: {acc_num}""\n")
file.write(f"Your name is: {name}""\n")
file.write(f"Your balance is: {balance}")
file.close()
