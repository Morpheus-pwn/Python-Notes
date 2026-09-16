from functools import lru_cache

@lru_cache #least recently used cache memory
def square(x):
    print("Calculating...")
    return x*x

print(square(5))
print(square(5))
print(square(6))
print(square(6))

from functools import partial

def power(base,exp):
    return base**exp

square=partial(power,exp=2)
print(square(4))
print(square(5))
print(square(10))

# comprehensions: list, set, dict, generator, nested loop

numbers=[1,2,3,4,5]
squares=[x*x for x in numbers] #[expression for variable in list]
print(squares)

# set comprehension
numbers=[1,2,2,3,3,4]
squares={x*x for x in numbers} #{expression for variable in list}
print(squares)

#dictionary comprehension
numbers=[1,2,3,4,5]
squares={x:x*x for x in numbers} #{expression for variable in list}
print(squares)

# generator comprehension
numbers=[1,2,3,4,5]
squares=(x*x for x in numbers) #{expression for variable in list}
print(squares)
print(next(squares)) #1
print(next(squares)) #4
print(next(squares)) #9
print(next(squares)) #16
print(next(squares)) #25
print(list(squares)) #remaining values in the generator


#nested comprehension
matrix=[[1,2],[3,4]]
result=[x for row in matrix for x in row]
print(result)

# iterable and iterator

numbers=[1,2,3]
it=iter(numbers) #iter function obtains an iterator from the iterable
print(it) #<list_iterator object at 0x000001F9D8A1C6D0>
print(next(it)) #1
print(next(it)) #2
print(next(it)) #3
print(next(it)) #error

# generators
def count_up_to(n): #generator function
    count=1

    while count<=n:
        yield count #yield is used to return a value from the generator function
        count+=1
numbers=count_up_to(3)
print(next(numbers)) #1
print(next(numbers)) #2
print(next(numbers)) #3

# lazy evaluation: the values are generated when requested.

#decorator

def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# say_hello=my_decorator(say_hello)
# say_hello()
