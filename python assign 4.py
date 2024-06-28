##1. Write a program to find factorial of a number

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

##2.Write a python program to display multiplication table?
num=int(input("Enter the number of table"))

for i in range (num,num+1): 
      for j in range(1,11):
         print(num,'*',j,'=',i*j)
         

##3. Write a python program to print a fibonacci sequence


nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
  while count<nterms:
     nth=n1+n2
     print(nth)
     n1=n2
     n2=nth
     count+=1

##4. Write a program to find armstrong number


# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

   
##5. Write a program to get armstrong number within interval.

lower = int(input("Enter any number:"))
upper = int(input("Enter any number:"))

for num in range(lower, upper + 1):
    # Calculate the order of the number (number of digits)
    order = len(str(num))
    
    # Initialize the sum
    armstrong_sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** order
        temp //= 10
    
    if num == armstrong_sum:
        print(num)
##6. Write a program to find sum of natural numbers
n=int(input('Enter the term:'))
sum=0        
i=1
while i<=n:
    sum=sum+i 
    i+=1
print(sum)    