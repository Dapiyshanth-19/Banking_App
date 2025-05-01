accounts = {}
account_number_counter = 1000

while True:
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choose = input("Choose the number (1-6): ")

    if choose == "1":
        name = input("Enter your name: ")
        balance = int(input("Enter initial balance: "))
        account_number_counter += 1
        accounts[account_number_counter] = [name, balance, []]
        print(f"Account created successfully! Your account number is {account_number_counter}")

    elif choose == "2":
        acc_num = int(input("Enter your account number: "))
        if acc_num in accounts:
            amount = int(input("Enter deposit amount: "))
            accounts[acc_num][1] += amount
            accounts[acc_num][2].append(f"Deposited: {amount}")
            print(f"Deposit successful. New balance: {accounts[acc_num][1]}")
        else:
            print("Account not found.")

    elif choose == "3":
        acc_num = int(input("Enter your account number: "))
        if acc_num in accounts:
            amount = int(input("Enter withdrawal amount: "))
            if accounts[acc_num][1] >= amount:
                accounts[acc_num][1] -= amount
                accounts[acc_num][2].append(f"Withdrew: {amount}")
                print(f"Withdrawal successful. New balance: {accounts[acc_num][1]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    elif choose == "4":
        acc_num = int(input("Enter your account number: "))
        if acc_num in accounts:
            print(f"Your current balance is: {accounts[acc_num][1]}")
        else:
            print("Account not found.")

    elif choose == "5":
        acc_num = int(input("Enter your account number: "))
        if acc_num in accounts:
            print("Transaction History:")
            for entry in accounts[acc_num][2]:
                print(entry)
        else:
            print("Account not found.")

    elif choose == "6":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Please choose between 1-6.")
