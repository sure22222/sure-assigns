    ### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?"


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def display_fibonacci_sequence(num_terms):
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(num_terms):
            print(fibonacci_recursive(i), end=" ")


num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
display_fibonacci_sequence(num_terms)


### 2. Write a Python Program to Find Factorial of Number Using Recursion?" 
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = int(input("Enter a non-negative integer to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial_recursive(number)
    print(f"The factorial of {number} is:", result)


### 3. Write a Python Program to calculate your Body Mass Index?"

    
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# Test the function
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your Body Mass Index (BMI) is:", bmi)


### 4. Write a Python Program to calculate the natural logarithm of any number?"

import math

def calculate_natural_logarithm(number):
    return math.log(number)

# Test the function
number = float(input("Enter a number to calculate its natural logarithm: "))

if number <= 0:
    print("Natural logarithm is not defined for non-positive numbers.")
else:
    result = calculate_natural_logarithm(number)
    print(f"The natural logarithm of {number} is:", result)


### 5. Write a Python Program for cube sum of first n natural numbers?\n"
n=int(input('Enter the number  of terms:'))
sum=0
for i in range(1,n+1):
   sum+=i**3
   
print(sum)