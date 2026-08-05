import sys
print(sys.getrecursionlimit())
accounts=[]
transactions=[]
bank_balance=500000
def create_account(account_type="savings", balance=0):
    '''this function creates a new bank account with the specified account type and initial balance.'''
    print("Account created successfully")
    print("Account type: ",account_type)
    print("Initial balance: ",balance)
    def create_pin(n):
        global accounts
        '''this function creates a 4 digit pin for the account holder.'''
        pin=int(input("Enter a 4 digit pin: "))
        if len(str(pin))==4:
            print("Pin created successfully")
            accounts.append({"account_type":account_type,"account_holder":account_holder,"balance":balance,"pin":pin})
            return pin
        elif n!=0:
            print("PIN Creation Attempt: ",4-n)
            create_pin(n-1)
        else:
            print("PIN creation failed. Please try again later.")

    pin=create_pin(n=3)
    def pin_verification(pin,n=3):
        '''this function verifies the pin entered by the account holder.'''
        entered_pin=int(input("Enter your pin: "))
        if entered_pin==pin:
            print("Pin verified successfully")
            return True
        else:
            print("PIN verification attempt", 4 - n)
            if n!=0:
                pin_verification(pin,n-1)
            else:
                print("PIN verification failed. Please try again later.")
                return False
            
    pin_verification(pin)
    return {"account_type":account_type,"account_holder":account_holder,"balance":balance,"pin":pin}

def deposit(balance,amount):
    global bank_balance,transactions
    '''this function deposits money into the account.'''
    print("Amount deposited successfully")
    balance+=amount
    bank_balance+=amount
    transactions.append({"type": "deposit", "amount": amount, "balance": balance})
    print("Updated balance: ",balance)
    return balance


def withdraw(balance,amount):
    global bank_balance,transactions
    '''this function withdraws money from the account.'''
    if balance>=amount:
        balance-=amount
        bank_balance-=amount
        transactions.append({"type": "withdrawal", "amount": amount, "balance": balance})
        print("Amount withdrawn successfully")
        print("Updated balance: ",balance)
        return balance
    else:
        print("Insufficient balance")
        return balance

def check_balance(account):
    '''this function checks the current balance of the account.'''
    global accounts
    for acc in accounts:
        if acc["account_holder"]==account:
            balance=acc["balance"]
            true_balance=balance
            break
        else:
            print("Account not found")
            print("balance is unknown")

def transaction_history():
    '''this function displays the transaction history of the account.'''
    if len(transactions)==0:
        print("No transactions found")
    else:
        for transaction in transactions:
            print(transaction)
            return transaction

def loan_eligibility(**details):
    '''this function checks the loan eligibility of the account holder.'''
    age=details.get("age")
    income=details.get("income")
    account_holder=details.get("account_holder")
    if age>=21 and income>=50000:
        loan_amount=income*4
        print("You are eligible for a loan")
        interest = lambda loan_amount, rate, time: loan_amount * rate * time / 100
        print("Interest: ",interest(loan_amount, 10, 2))
        return True
    else:
        print("You are not eligible for a loan")
        return False

while True:
    print("------ ONLINE BANKING SYSTEM ------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Loan Eligibility")
    print("7. Exit")

    choices=[1,2,3,4,5,6,7]
    choice=int(input("Enter your choice: "))
    if(choice not in choices):
        print("Invalid choice")
        continue

    if(choice==1):
        account_holder=input("Enter account holder name: ")
        account_type=input("Enter account type: ")
        balance=0
        accounts.append({"account_type":account_type,"account_holder":account_holder,"balance":balance})
        create_account(account_type,balance)
    elif(choice==2):
        deposit(amount=int(input("Enter deposit amount: ")),balance=5000)
    elif(choice==3):
        amount=int(input("Enter withdrawal amount: "))
        withdraw(balance,amount)
    elif(choice==4):
        account=input("Enter account holder name to check balance: ")
        true_balance=check_balance(account)
        print("balance: ",true_balance)
    elif(choice==5):
        transaction_history()
    elif(choice==6):
        account_holder=input("Enter account holder name: ")
        age=int(input("Enter your age: "))
        income=int(input("Enter your monthly income: "))
        details={"age": age, "income": income, "account_holder": account_holder}
        loan_eligibility(**details)
    elif(choice==7):
        print("Thank you for using Online Banking System")
        break

