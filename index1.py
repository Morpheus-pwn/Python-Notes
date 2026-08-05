#DAY 3
'''x=10
x+=2
print(x)
x-=2
print(x)
x*=2
print(bool(x==10))'''

#DAY 4
'''age=int(input("enter your age: "))
if(age>=18):
    print("you are eligible to vote")
    print("you can vote")
else:
    print("you are not eligible to vote")
    print("you cannot vote")'''

'''mark=95
if(mark>=60):
    print("D grade")
elif(mark>=70):
    print("C grade")
elif(mark>=80):
    print("B grade")
elif(mark>=90):
    print("A grade")
else:
    print("Fail")'''

'''num=int(input("enter a number: "))

if(num>0):
    if(num%2==0):
        print("positive and even")
    else:
        print("positive and odd")
elif(num==0):
    print("the number is zero")
else:
    print("not a positive number")

for i in range(5):
    print(i,end="\n")
print("\n")
for i in range(1,6):
    print(i,end="\n")
print("\n")
for i in range(1,6,2):
    print(i,end="\n")
print("\n")
for i in range(5,0,-1):
    print(i,end="\n")'''

# DAY 5
'''for i in range(3,31,3):
    print(i,end=" ")'''

'''for i in range(3):
    for j in range(2):
        print(i,j)'''

'''i=1
while(i<=5):
    print(i)
    i+=1'''

'''for i in range(1,10):
    if(i==5):
        break
    print(i)
print("\n")

for i in range(1,10):
    if(i==5):
        continue
    print(i)
print("\n")

for i in range(1,10):
    if(i==5):
        pass
    print(i)'''

# day 6
'''def add(a,b):
    print(a+b)
result=add(10,20)
print(result)'''

'''def add(a, b):
    return a + b

print(add(10, 20))

# day 7
sqr = lambda x: x**2
print(sqr(5))'''

'''def greet(name,age):
    print("Hello",name)
    print("Your age is",age)

age=int(input("enter your age: "))
name=input("enter your name: ")
greet(age,name)

def hello(a,b):
    return a/b

print(hello(b=10, a=20))

def greetings(hi="hello"):
    print(hi)

greetings("hello there")'''

'''def total(*values): # *values is a tuple
    result=0
    for n in values:
        result+=n
    return result

print(total(10,20,30,40,50))
print(total(10,20,30))
print(total(10,20))'''

'''def student_values(**data):
    for key,value in data.items():
        print(key,value)

student_values(name="John", age=20, city="New York")

def demo(*args,**kwargs):
    print(args)
    print(kwargs)

demo(10,20,name="achu",age=25)'''

'''def show():
    x=10
    print(x)

print(x)
show()'''

'''x=10
def show():
    global x
    x=20
    print(x)
show()
print(x)'''

# DAY 8
'''x="global"
def outer():
    x="outer"

    def inner():
        # nonlocal x
        x="inner"
        print("x after inner: ",x)
    inner()
    print("x after outer: ",x)
outer()
print("x after global: ",x)'''

age=23
name=
print("name:",name)