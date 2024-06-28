
##1. Python program to convert kilometres to miles
d=int(input('Type the distance'))
conv_fac = 0.621371
print('total distance in miles:', d*conv_fac)


##2. Python program to convert celsius to fahreneit

celsius = int(input('Enter the temperature'))
 
# Converting the temperature to fehrenheit using the formula
fahrenheit = (celsius * 1.8) + 32
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
      % (celsius, fahrenheit))
### Write python program to display calendar

import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print(calendar.month(yy,mm))

##Write a python program to solve quadratic equation
import math 



def equationroots( a, b, c): 

	# calculating discriminant using formula
	dis = b * b - 4 * a * c 
	sqrt_val = math.sqrt(abs(dis)) 
	
	# checking condition for discriminant
	if dis > 0: 
		print("real and different roots") 
		print((-b + sqrt_val)/(2 * a)) 
		print((-b - sqrt_val)/(2 * a)) 
	
	elif dis == 0: 
		print("real and same roots") 
		print(-b / (2 * a)) 
	
	# when discriminant is less than 0
	else:
		print("Complex Roots") 
		print(- b / (2 * a), + i, sqrt_val) 
		print(- b / (2 * a), - i, sqrt_val) 

 
a = 1
b = 10
c = -24

# If a is 0, then incorrect equation
if a == 0: 
		print("Input correct quadratic equation") 

else:
	equationroots(a, b, c)
	

### Write a python program to swap two variables without using temp variable
	
x = 5
y = 7

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


