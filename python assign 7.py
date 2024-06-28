### 1. Write a Python Program to find sum of array?"


def array_sum(arr):
    return sum(arr)


array = [1, 2, 3, 4, 5]
total_sum = array_sum(array)
print("Sum of the array elements:", total_sum)


 ### 2. Write a Python Program to find largest element in an array?\n"

array = [1, 2, 3, 4, 5]
largest_element = max(array)
print("Largest element of the array elements:", largest_element)


### 3. Write a Python Program for array rotation?"
def rotate_array_left(arr, k):
    # Perform array rotation towards the left by k positions
    return arr[k:] + arr[:k]

def rotate_array_right(arr, k):
    # Perform array rotation towards the right by k positions
    return arr[-k:] + arr[:-k]


array = [1, 2, 3, 4, 5]
rotate_left_by = 2
rotate_right_by = 3

rotated_left_array = rotate_array_left(array, rotate_left_by)
rotated_right_array = rotate_array_right(array, rotate_right_by)

print("Original array:", array)
print(f"Array after rotating left by {rotate_left_by} positions:", rotated_left_array)
print(f"Array after rotating right by {rotate_right_by} positions:", rotated_right_array)



### 4. Write a Python Program to Split the array and add the first part to the end?"
array = [1, 2, 3, 4, 5,6]
print(array[3::]+ array[:3:])

### 5. Write a Python Program to check if given array is Monotonic?
def is_monotonic(arr):
    # Check if the array is non-decreasing
    is_non_decreasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    # Check if the array is non-increasing
    is_non_increasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    
    # If either condition is True, the array is monotonic
    return is_non_decreasing or is_non_increasing

#
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 2, 3, 2, 4]

print("Array1 is monotonic:", is_monotonic(array1))
print("Array2 is monotonic:", is_monotonic(array2))
print("Array3 is monotonic:", is_monotonic(array3))
