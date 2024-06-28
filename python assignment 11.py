"### 1. Write a Python program to find words which are greater than given length k?"
'''
def find_words_greater_than_length(input_string, k):
    # Split the input string into words
    words = input_string.split()

    # Initialize a list to store words greater than length k
    result = []

    # Iterate over each word and check its length
    for word in words:
        if len(word) > k:
            result.append(word)

    return result


input_string = "This is a sample string with words of different lengths"
k = 5
words_greater_than_k = find_words_greater_than_length(input_string, k)
print(f"Words greater than length {k}: {words_greater_than_k}")

'''
"### 2. Write a Python program for removing i-th character from a string?"
'''
s1=input("enter the string:")
i=int(input('enter the ith term:'))
s2=s1[0:i:1]       
print(s2)'''
### 3. Write a Python program to split and join a string?
'''s1=input("enter any string:")
s2=s1.split(' ')
print(s2)
print(" ".join(s2))
'''
### 4. Write a Python to check if a given string is binary string or not?"
'''def is_binary_string(s):
    # Set of valid binary digits
    binary_digits = {'0', '1'}
    
    # Check if all characters in the string are valid binary digits
    for char in s:
        if char not in binary_digits:
            return False
    
    return True

# Test the function
string_to_check = input("Enter a string to check if it's a binary string: ")
if is_binary_string(string_to_check):
    print("The given string is a binary string.")
else:
    print("The given string is not a binary string.")

'''
###5. Write a Python program to find uncommon words from two Strings?
'''def find_uncommon_words(string1, string2):
    # Split strings into words
    words1 = string1.split()
    words2 = string2.split()
    
    # Convert words into sets
    set1 = set(words1)
    set2 = set(words2)
    
    # Find uncommon words using symmetric difference
    uncommon_words = set1.symmetric_difference(set2)
    
    return uncommon_words


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

uncommon_words = find_uncommon_words(string1, string2)
print("Uncommon words:", uncommon_words)

'''

 ### 6. Write a Python to find all duplicate characters in string?
  
s1=input("enter any string:")


for char in set(s1):
   freq=s1.count(char)
   if freq>1:
      print(char,end=' ')


###7. Write a Python Program to check if a string contains any special character?
import re

def contains_special_character(s):
    # Regular expression pattern to match special characters
    pattern = r'[^a-zA-Z0-9\s]'
    
    # Search for special characters in the string
    if re.search(pattern, s):
        return True
    else:
        return False

# Test the function
input_string = input("Enter a string: ")
if contains_special_character(input_string):
    print("The string contains special characters.")
else:
    print("The string does not contain any special characters.")




