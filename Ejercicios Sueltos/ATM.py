balance = int(input("How much money do you have?: "))

while True:
    balance = balance
    print("------------------------------------------------------------------------------------------"
    " Welcome to ATM"
"------------------------------------------------------------------------------------------")
    
    print("""
    1) Balance
    2) Withdraw
    3) Deposit
    4) Quit
    """)

    try:
        Option = int(input("Enter option: "))
    except Exception as e:
        print("Error: ", e)
        print("Enter 1, 2, 3 or 4 only")
        continue
    
    if Option == 1:
        print("Balance $", balance)
    if Option == 2:
        print("Balance $", balance)
        withdraw = float(input("Enter Withdraw amount $ "))
        if withdraw > 0:
            forewardbalance = (balance - withdraw)
            print("New Balance $", forewardbalance)
        elif withdraw > balance:
            print("None withdraw made")
    if Option == 3:
        print("Balance $", balance)
        deposit = float(input("Enter deposit amount $ "))
        if deposit > 0:
            forewardbalance = (balance + deposit)
            print("New Balance $ ", forewardbalance)
        else:
            print("None deposit made")
    if Option == 4:
        exit()