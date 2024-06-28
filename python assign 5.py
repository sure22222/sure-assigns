###1.Write a python program to find LCM

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

### 2. Write a Python Program to Find HCF?
def compute_hcf(x,y):
 if x>y:
  smaller=y
 else:
  smaller=x

 for i in range(1,smaller+1):
   if(x%i)==0 and (y%i)==0:
     hcf=i
 return hcf
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
print('The HCF is:', compute_hcf(num1,num2))
   
### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal? 
dec =int(input("Enter any number:"))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


### 4. Write a Python Program To Find ASCII value of a character?
c = input('Enter any character:')
print('The ASCII value is ', ord(c))

### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")



