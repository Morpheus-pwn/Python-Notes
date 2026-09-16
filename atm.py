class InsufficientBalanceError(Exception):
    pass

class ValueError(Exception):
    pass

def deposit(balance, amount):
    try:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        elif amount != int(amount):
            raise ValueError("Please enter a valid numeric amount.")
    except ValueError as e:
        print("Invalid input:", e)
    balance += amount
    return balance

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientBalanceError("Insufficient Balance\n")
            print("Transaction failed!")
    except InsufficientBalanceError as e:
        print(e)
    balance -= amount
    return balance

def check_balance(balance):
    return balance

while True:
    print("------ ATM BANKING SYSTEM ------ ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        balance=0
        amount = float(input("Enter the amount to deposit: "))
        try:
            try:
                if amount <= 0:
                    raise ValueError("Deposit amount must be positive.")
                elif amount != float(amount):
                    raise ValueError("Please enter a valid numeric amount.")
            except ValueError as e:
                print("Invalid input:", e)
        except Exception as e:
            print("Unexpected error occurred:", e)
        balance = deposit(balance, amount)
        print("Deposit successful! New balance:", balance)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        try:
            if amount > balance:
                raise InsufficientBalanceError("Insufficient Balance\n")
            else:
                balance = withdraw(balance, amount)
                print("Withdrawal successful! New balance:", balance)
        except Exception as e:
                    print("Exception occurred:", e)
        except InsufficientBalanceError as e:
            print(e)
        
    elif choice == '3':
        print("Current balance:", check_balance(balance))
        print("Transaction Successful!")
    elif choice == '4':
        print("Thank You For Using ATM Banking System\n")
        print("Session Closed Successfully ")
        break