
### 1. Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
'''
def divisible(a,b):
 i=1
 while i<=n:
    if i%5==0 and i%7==0:
      yield i
    i+=1  


n=int(input("Print the numbers upto:"))
a=divisible(0,n)
for i in range(n):
 print(next(a),end=',')

'''
### 2. Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
'''def even(a,b):
 i=1
 while i<=n:
    if i%2==0:
      yield i
    i+=1  


n=int(input("Print the numbers upto:"))
a=even(0,n)
for i in range(n):
 print(next(a),end=',')
'''
### 3. Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
'''
def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the nth term.
    """
    fib_sequence = [0, 1] if n >= 2 else [0] if n == 1 else []  # Initialize the sequence based on n
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Add the next term to the sequence
    return fib_sequence

def main():
    # Get user input for the number of terms in the Fibonacci sequence
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    # Generate the Fibonacci sequence using list comprehension
    fib_sequence = fibonacci_sequence(n)

    # Print the Fibonacci sequence in comma-separated form
    print("Fibonacci Sequence ({} terms):".format(n), end=" ")
    print(*fib_sequence, sep=", ")

if __name__ == "__main__":
    main()'''
### 5. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
'''
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())  # Output: 0

square = Square(5)
print("Area of Square:", square.area())  # Output: 25


'''
### 4. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
a=str(input('Enter any mailid:'))

for e in a:
    if e=='@':
       break 
    print(e,end='')
     
