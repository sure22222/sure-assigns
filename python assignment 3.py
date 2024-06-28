
#python assignment 3
##1. Write a program to check if number is positive,negative or zero?

num=int(input("Enter the number"))
if num<0:
   print('Number is negative')
elif num==0:
   print('Number is zero')
else:
   print('Number is Positive')               


##2. Write a program to check if number is odd or even
num=int(input("Enter the number:"))

if num%2==0:
   print('Number is even')
elif num%2!=0:
   print('number is odd') 
else:
  print('Number is 1')     


##3.Write a program to check leap year
year = int(input('Enter any Year:'))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))  
##4. Write a python program to check prime number
num=int(input("Enter the number greater than 1:"))
flag =False
for i in range(2,num):
    if num%i==0:
       flag=True
       break
if flag==True:    
  print('Number is not Prime')
else:
  print('Number is Prime')   


##5. Write a python program to get prime numbers in an interval of 1-10,000
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

   
print("Prime numbers between 1 and 10000:")
for num in range(1, 10001):
    if is_prime(num):
        print(num, end=" ")
