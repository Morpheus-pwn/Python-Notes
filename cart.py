products=["Rice", "Sugar", "Oil", "Milk", "Bread"]
membership_types=["Gold", "Silver", "Regular"]
customer_name=input("enter customer name: ")
product_name=input("enter product name: ")
quantity=int(input("enter quantity: "))
price_per_product=float(input("enter price per product: "))
membership_type=input("enter membership type: ")
wallet_balance=float(input("enter wallet balance: "))

print("\n------ BILL DETAILS ------\n")
total_cost=quantity*price_per_product
final_bill=total_cost
if(membership_type in membership_types and membership_type=="Gold"):
    discount=final_bill*0.50
elif(membership_type in membership_types and membership_type=="Silver"):
    discount=final_bill*0.80
else:
    discount=0
gst_amount=(total_cost-discount)*0.02
final_bill+=gst_amount
delivery_charge=30
if(final_bill>499):
    delivery_charge=0
else:
    final_bill+=delivery_charge
final_bill-=discount
x=10
y=x
print("\nTotal Cost: ",int(total_cost))
print("GST Amount: ",int(gst_amount))
print("Final Bill Amount: ",int(final_bill))
print("\nWallet balance sufficient: ",wallet_balance>=final_bill)
wallet_balance-=final_bill
print("\nFree delivery eligible: ",final_bill>499)
print("\nProduct available: ",product_name in products)
print("\nIdentity Operator Results:")
print("list1 is list2: ",products is membership_types)
print("x is y: ",x is y)
print("\nBitwise Operations: ")
print("5 & 3=",5&3)
print("5 | 3=",5|3)
print("5 ^ 3=",5^3)
print("5 << 1=",5<<1)
print("5 >> 1=",5>>1)
