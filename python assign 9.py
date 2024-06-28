"### 1. Write a Python program to check if the given number is a Disarium Number?"
'''def is_disarium_number(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)
    # Calculate the sum of digits raised to their respective positions
    sum_digits = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    # Check if the sum is equal to the original number
    return sum_digits == num

number = int(input("Enter a number to check if it's a Disarium number: "))
if is_disarium_number(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")

'''
##2. Write a Python program to print all disarium numbers between 1 to 100?"
def is_disarium_number(num):
    num_str = str(num)
    sum_digits = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return sum_digits == num

def print_disarium_numbers():
    disarium_numbers = []
    for num in range(1, 101):
        if is_disarium_number(num):
            disarium_numbers.append(num)
    return disarium_numbers


print("Disarium numbers between 1 and 100:")
print(print_disarium_numbers())
    
### 3. Write a Python program to check if the given number is Happy Number?"
def is_happy_number(num):
    def square_sum(n):
        return sum(int(digit)**2 for digit in str(n))
    
    slow = num
    fast = square_sum(num)
    
    while slow != fast:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))
        if slow == 1 or fast == 1:
            return True
    
    return slow == 1


number = int(input("Enter a number to check if it's a Happy Number: "))
if is_happy_number(number):
    print(f"{number} is a Happy Number.")
else:
    print(f"{number} is not a Happy Number.")


"### 4. Write a Python program to print all happy numbers between 1 and 100?"
def is_happy_number(num):
    def square_sum(n):
        return sum(int(digit)**2 for digit in str(n))
    
    slow = num
    fast = square_sum(num)
    
    while slow != fast:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))
        if slow == 1 or fast == 1:
            return True
    
    return slow == 1

def print_happy_numbers():
    happy_numbers = []
    for num in range(1, 101):
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers


print("Happy numbers between 1 and 100:")
print(print_happy_numbers())


### 5. Write a Python program to determine whether the given number is a Harshad Number?"
def is_harshad_number(num):
    # Calculate the sum of digits of the number
    digit_sum = sum(int(digit) for digit in str(num))
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

number = int(input("Enter a number to check if it's a Harshad Number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")

"### 6. Write a Python program to print all pronic numbers between 1 and 100?"
def is_pronic_number(num):
    for i in range(num):
        if i * (i + 1) == num:
            return True
    return False

def print_pronic_numbers():
    pronic_numbers = []
    for num in range(1, 101):
        if is_pronic_number(num):
            pronic_numbers.append(num)
    return pronic_numbers

# Test the function
print("Pronic numbers between 1 and 100:")
print(print_pronic_numbers())
