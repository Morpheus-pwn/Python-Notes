# import pickle as p
# data={"name":"pawan","age":20}
# with open("data.pkl","wb") as f:
#     p.dump(data,f)

# with open("data.pkl","rb") as f:
#     data=p.load(f)
#     print(data)

# import json as j
# data={"name":"pawan","age":20}
# with open("data1.json","wb") as f:
#     j.dump(data,f)

# with open("data1.json","rb") as f:
#     data=j.load(f)
#     print(data)

# class Account:
#     _balance=0 #protected class attribute
#     def __init__(self,name,_balance):
#         self.name=name #public instance attribute
#         self._balance=_balance #protected instance attribute

# #     def deposit(self,amount):
# #         self._balance+=amount
# #         return self._balance

# #     def withdraw(self,amount):
# #         self._balance-=amount
# #         return self._balance

# # a=Account("pawan",1000)
# # print(a.deposit(500))
# # print(a.withdraw(200))
# # print(a._balance)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount

#     def show_balance(self):
#         print("Balance:", self.__balance)

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()

# class D(B, C):
#     pass

# d = D()
# d.show()

with open("sample.txt","r") as f:
    for line in f:
        c=f.readline()
        print(c)
    