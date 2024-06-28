### 1. Write a Python program to print "Hello Python"?
print('Hello World') 
### 2. Write a Python program to do arithmetical operations addition and division.?
def operations(a,b,c):
    d=a+b/c
    return d
a=int(input('Enter first variable:'))
b=int(input('Enter Second variable:'))
c=int(input('Enter Third variable:'))
print(operations(a,b,c))

### 3. Write a Python program to find the area of a triangle?
b=int(input('Enter base length:'))
h=int(input('Enter height length:'))
a=1/2*b*h
print('The area of triangle is:',a)

### 4. Write a Python program to swap two variables?

a=int(input('Enter first variable:'))
b=int(input('Enter Second variable:'))
c=int(input('Enter Third variable:'))

c=a
a=b
b=c
print('The swapped variables are:',a,b)




### 5. Write a Python program to generate a random number?

import random

print(random.randint(0,1000))