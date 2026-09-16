a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=a/b
try:
    print(c)
except:
    raise ZeroDivisionError("Invalid operation")

print("start")
print(10/0)
print("end")

divisor = int(input("Enter a number: "))
try:
    result = 10 / divisor
except ZeroDivisionError as e:
    print("cannot divide by zero!", e)
except Exception as e:
    print("An error occurred:", e)
else:
    print(result)
finally:
    print("end")

def divide(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError as e:
        print("error occured inside divide()")
        raise

try:
    result=divide(10,0)
    print("result:",result)

except ZeroDivisionError:
    print("caller handled the error")


try: 
    x=10/0
except ZeroDivisionError as e:
    print("cannot divide by zero!", e)
except Exception as e:
    print("general error", e)

try:
    val = int(None)

except (ValueError, TypeError) as e: #tuple of exceptions, each exception is checked in order, like OR operator of exceptions
    print("invalid input:", e)

#nested try-except-finally blocks
try:
    f = open("data.txt", "r")

    try:
        data = f.read()
        number = int(data)

    except ValueError:
        print("File does not contain a valid integer")

    finally:
        f.close()

except FileNotFoundError:
    print("File not found")

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Attempted to withdraw {amount}, but only {self.balance} available"
            )
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

if __name__ == "__main__":
    b = BankAccount()
    try:
        b.withdraw(1000)
    except InsufficientFundsError as e:
        print(e)
