# =============================================================================
# Data Structures and Algorithms Nanodegree Udacity (Arrays Challenges)
# 
# Problem Statement:
# You have been given an array of length = n. The array contains integers from 0 to n - 2. 
# Each number in the array is present exactly once except for one number which is present twice. 
# Find and return this duplicate number present in the array. The expected time complexity for this problem is O(n) 
# and the expected space-complexity is O(1).
# 
# Example:
# 
#     arr = [0, 2, 3, 1, 4, 5, 3]
#     output = 3 (because 3 is present twice)
# =============================================================================

#Write your code in this function
def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        arr.pop()
        
        if num in arr:
            return num
        
#helper function for testing purpose
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# =============================================================================
# Test 1
# 
# arr = [0, 0]
# solution = 0
# test_case = [arr, solution]
# test_function(test_case)
# 
# Test 2
# 
# arr = [0, 2, 3, 1, 4, 5, 3]
# solution = 3
# test_case = [arr, solution]
# test_function(test_case)
# 
# Test 3
# 
# arr = [0, 1, 5, 4, 3, 2, 0]
# solution = 0
# test_case = [arr, solution]
# test_function(test_case)
# 
# Test 4
# 
# arr = [0, 1, 5, 5, 3, 2, 4]
# solution = 5
# test_case = [arr, solution]
# test_function(test_case)
# =============================================================================


        
        

