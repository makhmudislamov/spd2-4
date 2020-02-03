"""
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  =>  [3, 7] or [6, 4] or [8, 2]
"""

def find_sum(arr, target):
    # sort the array in ascending order
    # keep one pointer at the beginning of the arr
    # another one at the end
    # check the sum of the both
    # return new array if its equal to target
    # if sum is greater than targer
    # move the right pointer to left until its equal or less then sum
    # if sum is less than sum
    # move the left pointer to right
    # return list(left and right nums) when its equal to target

    sorted_arr = sorted(arr)

    left_pointer = 0
    right_pointer = len(sorted_arr)-1

    while left_pointer < len(sorted_arr):
        while right_pointer > 0:
            pointers_sum = sorted_arr[left_pointer] + sorted_arr[right_pointer]
            if pointers_sum == target:
                 print(sorted_arr[left_pointer], sorted_arr[right_pointer])
            pass



arr = [5, 3, 6, 8, 2, 4, 7]
target = 10
print(find_sum(arr, target))
