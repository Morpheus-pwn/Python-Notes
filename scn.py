'''# scenario 1
shirt=int(input("enter the price of shirt: "))
shoes=int(input("enter the price of shoes: "))
total_price=shirt+shoes
print("total_price: ", total_price)
print("\n")
# scenario 2
balance=10000
withdraw=2500
new_balance=balance-withdraw
print("new_balance: ", new_balance)
print("\n")

# scenario 3
ticket_cost=250
num_tickets=4
total_cost=ticket_cost*num_tickets
print("total_cost: ", total_cost)
print("\n")

# scenario 4
bill_amount=1500
num_friends=4
pay=bill_amount/num_friends
print("each friend should pay: ", pay)
print("\n")

# scenario 5
total_chocolates=53
box_capacity=10
filled_boxes=total_chocolates//box_capacity
remaining_chocolates=total_chocolates%box_capacity
print("filled_boxes: ", filled_boxes)
print("remaining_chocolates: ", remaining_chocolates)
print("\n")

# scenario 6
duration_minutes=145
hours=duration_minutes//60
minutes=duration_minutes%60
print("hours: ", hours)
print("minutes: ", minutes)
print("\n")

# scenario 7
roll_number=int(input("enter roll number: "))
if(roll_number%2==0):
    print("roll number is even")
else:
    print("roll number is odd")
print("\n")

# scenario 8
side=5
area=side**2
print("area of square: ", area)
print("\n")

# scenario 9
wallet=500
amt=200
updated_ball=wallet+amt
print("updated balance: ", updated_ball)
print("\n")

# scenario 10
points=100
points+=50
points-=20
print("final score: ", points)
print("\n")

# scenario 11
student_score=65
pass_mark=40
if(student_score>=pass_mark):
    print("student passed")
else:
    print("student failed")
print("\n")

# scenario 12
password=input("enter password: ")
stored_password="password"
if(password==stored_password):
    print("password matches")
else:
    print("no match")
print("\n")

# scenario 13
stock=int(input("enter stock: "))
if(stock!=0):
    print("stock available")
else:
    print("stock not available")
print("\n")

# scenario 14
age=int(input("enter your age: "))
test_status=input("enter driving test status:")
if(age>=18 and test_status=="passed"):
    print("eligible for driving license")
else:
    print("not eligible for driving license")
print("\n")

# scenario 15
day=input("enter the day:")
if(day=="sunday" or day=="saturday"):
    print("weekend")
else:
    print("Not weekend")
print("\n")

# scenario 16
shop_amount=int(input("enter order amount: "))
membership=input("enter member type:")
if(shop_amount>=1000 or membership=="premium"):
    print("eligible for free delivery")
else:
    print("not eligible for free delivery")
print("\n")

# scenario 17
account_status=input("enter account status: ")
if(account_status!="blocked"):
    print("account is active")
else:
    print("account is blocked")
print("\n")

# scenario  18
age=24
graduation_status=input("enter graduation status: ")
banned_status=False
if(age>=21 and graduation_status=="completed" and not banned_status):
    print("candidate is eligible")
else:
    print("candidate is not eligible")
print("\n")

# scenario 19
products = ["Laptop", "Mobile", "Tablet", "Headphones"]
if("Laptop" in products):
    print("available")
else:
    print("not available")
print("\n")

# scenario 20
blocked_names = ["admin", "root", "system"]
usernames=input("enter username: ")
if(usernames not in blocked_names):
    print("restricted access")
else:
    print("access granted")
print("\n")

# scenario 21
email=input("enter the email: ")
if('@' in email):
    print('@' in email)
else:
    print("@ not found in email")
print("\n")

# scenario 22
list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1==list2)
print(list1 is list2)
print("\n")

# scenario 23
cart1 = ["Laptop", "Mouse"]
cart2 = cart1
print(cart1==cart2)
print(cart1 is cart2)
print("\n")'''

# scenario 24
permission_value=3
read=1
write=2
print("bitwise AND: ", permission_value & read)
print("bitwise and: ", permission_value & write)

# scenario 25
products=[]
product_price=1200
quantity=3
discount=500
for i in range(quantity):
    product=input("enter product name: ")
    products.append(product)
product_price*=quantity
final_amount=product_price
final_amount-=discount
if(final_amount>=2000):
    print("eligible for free delivery")
else:
    print("not eligible for free delivery")
if("laptop" in products):
    print("available")
else:
    print("not available")
print("\n")

# scenario 26 factorial of a number
num=int(input("enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial: " ,fact)

fact=int(input("enter a number: "))
n=fact
fact=1
while(n!=0):
    fact=fact*n
    n-=1
print("factorial: " ,fact)



