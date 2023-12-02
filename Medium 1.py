from collections import Counter

def find_majority_elements(nums):
    n = len(nums)
    threshold = n // 3

    count_map = Counter(nums)
    result = [num for num, count in count_map.items() if count > threshold]

    return result

# Custom Input
input_string = input("Input: ")
nums = list(map(int, input_string.split()))

majority_elements = find_majority_elements(nums)
print("Output:", majority_elements)

 """This code is designed to find an element in the array that has occured more than n/3 times, where n is the size of array.
 Using the Counter class from collections module to count the occurence of each element in the input array 'nums' .
 n find the length of the nums, threshold calcultes the value of n/3 and stores in it .
 The Counter object (count_map) stores the count of occurrences for each unique element in the nums array.
 Then it iterates through count_map and creates a list named result containing elements that have a count 
 greater than the calculated threshold.
 The function returns the result list containing elements that appear more than n/3 times in the input array.
 We take custom input from user call the function, pass the value and obtain the results"""

