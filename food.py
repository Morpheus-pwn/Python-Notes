#read input from user using variables and display order details
name=input("Enter Customer Name: ")
item=input("Enter food item: ")
quantity=int(input("enter quantity: "))
price=float(input("enter price per item:"))
dist=float(input("enter delivery distance(in km): "))

print("\n------ ORDER DETAILS ------\n")

# name is the variable and it is displayed using print statement
print("Customer Name: ",name)
# type() function is used to check the data type of the variable
print("Type: ",type(name))
# id() function is used to check the memory address of the variable
print("Memory Address: ",id(name))

# similarly for other variables, it is followed...

print("\nFood item: ",item)
print("Type: ",type(item))
print("Memory Address: ",id(item))

print("\nQuantity: ",quantity)
print("Type: ",type(quantity))
print("Memory Address: ",id(quantity))

print("\nPrice per item: ",price)
print("Type: ",type(price))
print("Memory Address: ",id(price))
total_food_cost=price*quantity

print("\nDelivery Distance: ",dist)
print("Type: ",type(dist))
print("Memory Address: ",id(dist))
print("\nDelivery Charge: ",dist*6.0)

bill=(price*quantity)+dist*6.0
print("\nFinal Bill Amount: ",bill)
print("Type: ",type(bill))

print("\nChecking Data Types: ")
print("quantity is integer:",isinstance(quantity,int))
print("Price is float:",isinstance(price,float))
print("Final bill is float:",isinstance(bill,float))

