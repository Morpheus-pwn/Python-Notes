# even or odd
def even_odd(num):
    if(num%2==0):
        print(num," is even")
    else:
        print(num," is odd")

# positive or negative or zero
def positive_negative(num):
    if(num>0):
        print(num," is positive")
    elif(num<0):
        print(num," is negative")
    else:
        print(num," is zero")

# largest of two numbers
def largest_of_two(num1,num2):
    if(num1>num2):
        print(num1," is largest")
    elif(num1<num2):
        print(num2," is largest")
    else:
        print("both numbers are equal")

# largest of three numbers
def largest_of_three(a,b,c):
    if(a>b):
        if(a>c):
            print(a," is largest")
        else:
            print(c," is largest")
    elif(b>a):
        if(b>c):
            print(b," is largest")
        else:
            print(c," is largest")

def part2_largest_of_three(a,b,c):
    if(a>b and a>c):
        print(a," is largest")
    elif(b>a and b>c):
        print(b," is largest")
    else:
        print(c," is largest")

# check voting eligibility
def eligibility(age):
    if(age>=18):
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

# print numbers from 1 to 10
def print_numbers():
    for i in range(1,11):
        print(i,end=" ")

    print("\n")
    i=1
    while(i!=0):
        if(i<=10):
            print(i,end=" ")
            i+=1
        else:
            break

# print even numbers from 1 to 20
def print_even_numbers():
    for i in range(2,21,2):
        print(i,end=" ")

    i=1
    while(i!=0):
        if(i<=20):
            if(i%2==0):
                print(i,end=" ")
            i+=1
        else:
            break

# sum of first n numbers
def sum_of_n_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)

    print("\n")

    sum=0
    i=1
    while(i<=n):
        sum+=i
        i+=1
    print(sum)


# multiplication table of a number
def multiplication_table(num,limit):
    for i in range(1,limit+1):
        print(num,"X",i,"=",num*i)

    print("\n")

    i=1
    while(i<=limit):
        print(num,"X",i,"=",num*i)
        i+=1

# count from 1 to 10 using while loop
def count_1_to_10():
    i=1
    while(i<=10):
        print(i,end=" ")
        i+=1

    print("\n")

# reverse counting
def reverse_counting():
    for i in range(10,0,-1):
        print(i)

    print("\n")

    i=10
    while(i!=0):
        print(i)
        i-=1

# sum until user enters 0
def sum_until_zero():
    sum=0
    while True:
        n=int(input("Enter a number (0 to exit): "))
        if n==0:
            break
        sum+=n
    print("Sum:", sum)

    print("\n")

# skip multiples of 3
def skip_multiples_of_3(limit):
    for i in range(1,limit+1):
        if i%3==0:
            continue
        print(i,end=" ")

    print("\n")

    i=1
    while(i<=limit):
        if(i%3==0):
            i+=1
            continue
        else:
            print(i,end=" ")
            i+=1

# stop at number 7
def stop_at_7(limit):
    for i in range(0,limit+1):
        if i==7:
            break
        print(i,end=" ")

    print("\n")

    i=0
    while(i<=limit):
        if(i==7):
            break
        print(i,end=" ")
        i+=1

# print only odd numbers
def odd_numbers(limit):
    for i in range(1,limit+1,2):
        print(i,end=" ")

    print("\n")

    i=1
    while(i<=limit):
        if(i%2==0):
            i+=1
            continue
        else:
            print(i,end=" ")
            i+=1

# factorial of a number with and without recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

    print("\n")

    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

# count digits of a number
def count_digits(num):
    count=0
    while(num!=0):
        num//=10
        count+=1
    return count

# reverse a number
def reverse_number(num):
    rev=0
    while(num!=0):
        d=num%10
        rev=rev*10+d
        num//=10
    return rev

# check palindrome number
def palindrome_number(num):
    rev=0
    n=num
    while(num!=0):
        d=num%10
        rev=rev*10+d
        num//=10

    if(rev==n):
        print(rev," is a palindrome number")
    else:
        print(rev," is not a palindrome number")

# guess the secret number
def secret_number_guess(num):
    secret_number=7
    if(num==secret_number):
        print("Congratulations! You guessed the secret number.")
    else:
        print("Sorry, that's not the secret number. Try again.")

def main():
    print("Welcome to the Number Operations Program!")
    while True:
        print("\nMenu:")
        print("1. Even or Odd")
        print("2. Positive or Negative or Zero")
        print("3. Largest of Two Numbers")
        print("4. Largest of Three Numbers")
        print("5. Check Voting Eligibility")
        print("6. Print Numbers from 1 to 10")
        print("7. Print Even Numbers from 1 to 20")
        print("8. Sum of First N Numbers")
        print("9. Multiplication Table of a Number")
        print("10. Count from 1 to 10 using While Loop")
        print("11. Reverse Counting")
        print("12. Sum Until User Enters 0")
        print("13. Skip Multiples of 3")
        print("14. Stop at Number 7")
        print("15. Print Only Odd Numbers")
        print("16. Factorial of a Number with and without Recursion")
        print("17. Count Digits of a Number")
        print("18. Reverse a Number")
        print("19. Check Palindrome Number")
        print("20. Guess the Secret Number")
        print("21. Exit")

        choice=int(input("Enter your choice: "))

        if choice==1:
            num=int(input("Enter a number: "))
            even_odd(num)
        elif choice==2:
            n=int(input("Enter a number: "))
            positive_negative(n)
        elif choice==3:
            num1=int(input("Enter first number: "))
            num2=int(input("Enter second number: "))
            largest_of_two(num1, num2)
        elif choice==4:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            c=int(input("Enter third number: "))
            largest_of_three(a, b, c)
        elif choice==5:
            age=int(input("Enter your age: "))
            eligibility(age)
        elif choice==6:
            print_numbers()
        elif choice==7:
            print_even_numbers()
        elif choice==8:
            n=int(input("Enter the value of n: "))
            sum_of_n_numbers(n)
        elif choice==9:
            num=int(input("Enter a number: "))
            limit=int(input("Enter the limit: "))
            multiplication_table(num, limit)
        elif choice==10:
            count_1_to_10()
        elif choice==11:
            reverse_counting()
        elif choice==12:
            sum_until_zero()
        elif choice==13:
            limit=int(input("Enter the limit: "))
            skip_multiples_of_3(limit)
        elif choice==14:
            limit=int(input("Enter the limit: "))
            stop_at_7(limit)
        elif choice==15:
            limit=int(input("Enter the limit: "))
            odd_numbers(limit)
        elif choice==16:
            n=int(input("Enter a number: "))
            print("Factorial (with recursion):", factorial(n))
            print("Factorial (without recursion):", factorial(n))
        elif choice==17:
            num=int(input("Enter a number: "))
            print("Count of digits:", count_digits(num))
        elif choice==18:
            num=int(input("Enter a number: "))
            print("Reversed number:", reverse_number(num))
        elif choice==19:
            num=int(input("Enter a number: "))
            palindrome_number(num)
        elif choice==20:
            num=int(input("Guess the secret number: "))
            secret_number_guess(num)
        elif choice==21:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

