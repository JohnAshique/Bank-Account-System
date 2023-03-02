from Bank_Acount import Bank_Account
if __name__ == '__main__':

    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    id = int(input("Enter your 4 digit ID: "))
    customer = Bank_Account(id)
    while(True):
        print("For deposit, Press 1")
        print("For withdraw, Press 2")
        print("To see your balance, Press 3")
        print("Press 4 to finish this session")
        choice = int(input("Enter your choice: "))
        if choice==1:
            customer.deposit()
        if choice==2:
            customer.withdraw()
        if choice==3:
            customer.display()
        if choice==4:
            break

