# abstract method
from abc import ABC, abstractmethod
from exception import InsufficientFundsError

class Customer:
    bank_name = "ABC Bank"
    def __init__(self, customer_name, account_number, balance=5000):
        self.customer_name = customer_name
        self._account_number =  account_number
        self.balance = balance
        print("customer created successfully!\n")

    def check_balance(self):
        return self.balance

class BankAccount(Customer):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            combined_balance = self.balance + other.balance
            return BankAccount(self.account_number, combined_balance)
        return NotImplemented

    def check_balance(self):
        return self.balance

class BankAccount(Customer):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.account_number, self.balance + other.balance)
        return NotImplemented

    def check_balance(self): # here duck typing is used
        return self.balance

class Employee:
    def __init__(self, employee_name, employee_id, salary):
        self.employee_name = employee_name
        self.__employee_id = employee_id
        self.salary = salary
        print("Employee created successfully!\n")

    def __del__(self):
        print("Employee object is being deleted.")

class Loan(Customer):
    def __init__(self, loan_amount, interest_rate, loan_term):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term

    def apply_loan(self):
        if self.loan_amount > 50000:
            print("Loan amount exceeds the limit.")
        else:
            print("loan approved!")
    @abstractmethod
    def calculate_interest(self):
        print("Calculating interest for the loan...")
        return self.loan_amount * self.interest_rate * self.loan_term
class Transaction(BankAccount):
    def __init__(self, transaction_type, amount, date):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date

    def withdraw(self, balance, amount):
        self.balance = balance
        if amount > self.balance:
            try:
                raise InsufficientFundsError("Insufficient funds for withdrawal.")
            except InsufficientFundsError as e:
                print(e)
                return self.balance
        self.balance -= amount
        print("withdrawal successful!")
        print("Remaining balance:", self.balance)
        return self.balance
    def deposit(self, balance, amount):
        self.balance = balance
        self.balance+=amount
        print("deposit successful!")
        print("updated balance:", self.balance)
        return self.balance

c=Customer("John Doe", "123456789", 1000)
b=BankAccount("123456789", 1000)
e=Employee("John Doe", "123456789", 1000)
l=Loan(1000, 0.05, 12)
t=Transaction("Withdrawal", 1000, "2026-09-03")
print("------ SMART BANKING SYSTEM ------ ")
print("Customer Name:", c.customer_name)
print("Account Number:", c._account_number)
print("Balance:", c.balance)
print("\n")
print(t.deposit(c.balance, 5000))
print("\n")
print(t.withdraw(c.balance, 2000))
print("\n")
print(l.apply_loan())
print("\n")
print("Bank Name:", c.bank_name)
print("\n")
print("MRO Output:", Customer.mro(),end="\n")
print("\n")
print("operator overloading result:")
print("total balance of two accounts:", (b + b).check_balance())
print("\n")
print("comparing two accounts:")
print(b==b)
print("\n")
print("abstract method implemented successfully")
print("interest calculated:", l.calculate_interest())
print("\n")




