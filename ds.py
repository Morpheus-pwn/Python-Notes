# day 1
word="python"
'''print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])'''

"""print(word[5::])

wd=["python","is","awesome"]
result=" ".join(wd)
print(result)"""

'''word1="python"
word2="is"
word3="awesome"
print(f"{word1} {word2} {word3}")
print("{} {} {} {}".format(word1,word2,"not",word3))
print(word1+" "+word2+" "+word3)'''

'''age=25
print("age:"+str(age))
print(f"age:{age}")

mixed=[10,"python",3.5,True]
print(mixed)

numbers=[10,20,30,40]
print(numbers[0])
print(numbers[-1])
print(numbers[-4:-1])
print(numbers[-1:-5:-1])
numbers[0]=60
print(numbers)


numbers.append(50)
print(numbers)
numbers.insert(2,25)
print(numbers)
numbers.extend([60,70,80])
print(numbers)'''

'''nums=[1,2]
nums.extend([3,4,5])
print(nums)
nums.append([6,7,8])
print(nums)
print(nums.remove(2))'''

'''nums=[1,2,3,4,2]
nums.remove(2)
nums.remove(10)
print(nums)'''

'''nums=[10,20,30]
x=nums.pop(1)
print(x)
nums.clear()
print(nums)'''


'''nums=[10,20,30,40,30]
print(nums.index(30))
# print(nums.index(100))
x=nums.count(30)
print(x)'''

'''nums=[10,40,30,20]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums=sorted(nums)
print(nums)
nums=sorted(nums,reverse=True)
print(nums)'''

'''fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(fruits[i])'''

'''nums=[10,20,30,40]
print(2 in nums)
print(20 in nums)
print(50 not in nums)
print(2 not in nums)


a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
d=a*3
print(d)'''

'''matrix=[[1,2],[3,4]]
print(matrix[0])
print(matrix[1])
print(matrix[0][1])
print(matrix[1][0])'''

'''numbers=(1,2,3,4)
print(type(numbers))
empty=()
print(type(empty))
t1=("0",)
print(type(t1))'''

'''x,y,z=(10,20, )
print(x)
print(y)
print(z)'''

'''colors=("red","green","blue")
print(colors[0])
print(colors[-1])'''

'''numbers=(10,20,30,40,50)
x=numbers[1:4]
print(x)
x=numbers[1:]
print(x)'''

# x=numbers[:3]
# print(x)
# x=numbers[:]
# print(x)
# x=numbers[::2]
# print(x)
# x=numbers[::-1]
# print(x)

'''def factorial(n):
    if(n==0 or n==1):
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5))'''

# Python program to find the Nth term in a Fibonacci series using recursion
'''def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))'''

# day 11

'''nums=(1,2,2,3)
print(nums.count(3))

nums1=(10,20,30)
print(nums1.index(20))'''

'''colors=("red","green","blue")
for color in colors:
    print(color)

student=("achu",20)
name,age=student
# print("name:",name)
# print("age:",age)
# name=student[0]
# age=student[1]
print("name:",name)
print("age:",age)'''

'''numbers=(1,2,3,4,5)
a, b, *c=numbers
print("a=",a)
print("b=",b)
print("c=",c)'''

'''nums_list=[1,2,3]
nums_tuple=tuple(nums_list)
print(nums_tuple)
nums_list=list(nums_tuple)
print(nums_list)'''

'''data=((1,2),((3,4),4))
print(data[1][0][0])
print(data[1][0])
print(data[0][0])
print(data[1][1])

datas=([1,2],3)
print(datas[0].append(4))
print(datas[0])'''

'''numbers={1,2,2,3,4,5}
print(type(numbers))
print(numbers)


nums=set([1,2,2,3,4,5])
print(nums)

set1={None}
print(type(set1))
empty_set=set()
print(type(empty_set))


numbers={1,2,3,4,5}
for i in numbers:
    if i==2 or i<4:
        print(i)

nums={10,20,30}
for item in nums:
    if i==0:
        print(item)
    elif i==1:
        print(item)
    elif i==2:
        print(item)
    else:
        print(item)

nums={1,2}
nums.add(2)
print(type(nums.add(3)))
print(nums)
print(type(nums))


nums={1,2,3}
nums.update([3,4,5])
print(nums)

nums={1,2,3}
nums.remove(3)
print(nums)'''

'''nums={1,2}
nums.update({2,3,4,5})
print(nums)
nums.discard(7)
print(nums)
nums.remove(7) this is key error

nums={1,2,3}
x=nums.pop() #pop() removes random element
print(x)
print(nums)
y=nums.clear()
print(nums)

A={1,2,3}
B={3,4,5}
c=A | B #union
d=A & B #intersection
e=A - B #difference
f=B - A #difference
g=A ^ B #symmetric difference
print(c) 
print(d)
print(e)
print(f)
print(g)

nums=frozenset([1,2,3])
print(type(nums))
# nums.add(4) #frozenset is immutable, attri
print(nums)'''

'''nums={1,2,3}
print(2 in nums)'''

person={"name":"pawan","age":23,"city":"kollam"}
print(person)
print(person["name"])

person1=dict(name="pawan shaji",age=23,city="kollam")
print(person1.get("phone_number",0))
print(person1)
person1["age"]=30
print(person1)
person1["phone_number"]="123-456-7890"
print(person1)
person1.update({"age":23,"city":"trivandrum","country":"india"})
print(person1)
person1.pop("country")
person1.popitem() #removes last item
print(person1)
del person1["city"]
print(person1)
print(person1.keys()) #returns all keys
print(person1.values()) #returns all values
print(person1.items()) #returns all key-value pairs

for key in person1:
    print(key)

for value in person1.values():
    print(value)
# data=dict(2="two",three=3,(3,4)="tuple")
data={1:"one","two":2,(3,4):"tuple"}
print(data)

student={"name":"rahul","marks":{"english":80,"maths":90}}
print(student)
print(student["marks"])
print(student["marks"]["maths"])