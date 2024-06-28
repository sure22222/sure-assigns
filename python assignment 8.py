### 1. Write a Python Program to Add Two Matrices?"
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]

for r in result:
    print(r)

### 2. Write a Python Program to Multiply Two Matrices?"


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]*Y[i][j]





### 3. Write a Python Program to Transpose a Matrix?
import numpy as np

# Create a sample matrix
a = np.array([[1, 2], [3, 4]])


transposed_matrix = a.transpose()

print("Original matrix:")
print(a)
print("\nTransposed matrix:")
print(transposed_matrix)

### 4. Write a Python Program to Sort Words in Alphabetic Order?\n"

def sort_words_alphabetically(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Sort the words in alphabetical order
    sorted_words = sorted(words)
    
    return sorted_words

# Test the function
input_sentence = input("Enter a sentence to sort words alphabetically: ")
sorted_words = sort_words_alphabetically(input_sentence)

print("Sorted words in alphabetical order:")
for word in sorted_words:
    print(word)



### 5. Write a Python Program to Remove Punctuation From a String?





import string

def remove_punctuation(input_string):
    # Create a translation table to remove punctuation
    translation_table = str.maketrans("", "", string.punctuation)
    # Remove punctuation from the input string
    clean_string = input_string.translate(translation_table)
    return clean_string


input_string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(input_string)

print("String after removing punctuation:", cleaned_string)
