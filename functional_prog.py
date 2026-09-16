def greet():
    print("hello!")

a=greet #first-class function, function is assigned to a variable 
a()
a=greet()

pass a fuction as an argument
def square(x):
    print("square of",x,"is",x*x)

s=square
s(5)

def square(x):
    return x * x

def calculate(func, value):
    return func(value)

result = calculate(square, 5)
print("Result:", result)

# return a function from another function

def outer():
    def inner():
        print("hello")

    return inner

x=outer() #outer function is called and inner function is returned
x()

# higher order functions: map(), filter(), reduce(), sorted()

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
result=map(square, numbers) #map function returns a map object or map iterator, which is an iterable that generates the results on-the-fly as you iterate over it. It does not return a list directly.
print(list(result))

numbers=[1, 2, 3, 4, 5, 6]
def is_even(x):
    return x % 2 == 0

numbers=[1, 2, 3, 4, 5, 6]
result=filter(is_even, numbers) #filter function returns a filter object or filter iterator, which is an iterable that generates the results on-the-fly as you iterate over it. It does not return a list directly.
print(list(result))

from functools import reduce

def multiply(x,y):
    return x*y #x is the acculated value and y is the current value in the iterable.

numbers=[1,2,3,4]
result=reduce(multiply, numbers) #reduce function returns a single value by applying the function cumulatively to the items of the iterable, from left to right.
print(result)

# #sorted function returns a new sorted list from the items in iterable. It does not modify the original list.

#lambda functions
add = lambda x, y: x + y
result = add(5, 3)
print(result)

square = lambda x: x * x
result = square(4)
print(result)

numbers = [1,2,3,4]
result = list(map(lambda x: x * 2, numbers))
print(result)

numbers = [1,2,3,4,5,6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result) 