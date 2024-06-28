### 1. Write a program that calculates and prints the value according to the given formula:
'''Q = Square root of [(2 C D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.

Example

Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24
'''

C,H=50,30
R=[]
for i in range(3):
 D=int(input('Enter value'))
 a =(2*C*D)/H
 Q=a**0.5
 R.append(round(Q,0))
 
for e in R:
  print(e,end=',') 



### 2. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

def generate_array(X, Y):
    # Initialize an empty 2-dimensional array
    array_2d = []

    # Iterate over rows
    for i in range(X):
        # Initialize a temporary row
        row = []
        # Iterate over columns
        for j in range(Y):
            # Append the element value to the row
            row.append(i * j)
        # Append the row to the 2-dimensional array
        array_2d.append(row)

    return array_2d

# Function to print the array
def print_array(array):
    for row in array:
        print(row)

# Main function to take input and generate the array
def main():
    try:
        X = int(input("Enter the number of rows (X): "))
        Y = int(input("Enter the number of columns (Y): "))

        # Generate the array
        result_array = generate_array(X, Y)

        # Print the array
        print("Generated 2-dimensional array:")
        print_array(result_array)
    except ValueError:
        print("Please enter valid integers for X and Y.")

# Run the main function
if __name__ == "__main__":
    main()

 ### 3. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically."

def sort_words(input_string):
    # Split the input string into a list of words
    words = input_string.split(',')

    # Remove any leading or trailing whitespace from each word
    words = [word.strip() for word in words]

    # Sort the list of words alphabetically
    sorted_words = sorted(words)

    # Join the sorted words into a comma-separated string
    sorted_string = ', '.join(sorted_words)

    return sorted_string

# Example usage:
input_sequence = input("Enter a comma-separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print("Sorted sequence:", sorted_sequence)


 ### 4. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically."


input_sequence = input("Enter a whitespace sequence of words: ")

word=input_sequence.split(' ')
word=set(word)
word=sorted(word)
print((',').join(word))

"### 5. Write a program that accepts a sentence and calculate the number of letters and digits."
sen=input("Enter the sentence")
count=0
for e in sen:
    count+=1 
print(count)

### 6. A website requires the users to input username and password to register. Write a program to check the validity of password input by users."

import re

def is_valid_password(password):
    # Define criteria for a valid password
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_characters = "!@#$%^&*()_+{}[];:'\"<>,.?/|\\"

    # Check password length
    if len(password) < min_length:
        return False

    # Check for presence of uppercase, lowercase, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special_char = True

    # Return True only if all criteria are met
    return has_uppercase and has_lowercase and has_digit and has_special_char

# Example usage:
password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid. Please make sure it contains at least 8 characters, including uppercase and lowercase letters, digits, and special characters.")
