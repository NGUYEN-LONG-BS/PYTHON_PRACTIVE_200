# Excercise 1: Swap the number without using third varible

# enter the first number 4
# enter the Second number 5
# 4 5
# 5 4
x=int(input("enter the first number "))
y=int(input("enter the Second number "))
print(x,y)
x=x+y
y=x-y
x=x-y
print(x,y)



# Exercise 2: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# enter the number: 1234
# 4 3 2 1
n=input("enter the number: ")
y=n[::-1]       # in reverse order
# y=n[::1]      # in order
k=" ".join(y)
print(k)



# Excercise 3: Write a program that will give you the sum of 3 digits

# enter three digit number567
# 18
x=int(input("enter three digit number"))
a=x%10          # we will get last digit
num=x//10       # integer-divison here we will get first two digit
b=num%10        # here we will get last digit of two digit number
c=num//10       # here will get first digit of two digit number
print(a+b+c)

