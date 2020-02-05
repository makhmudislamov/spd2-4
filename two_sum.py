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
    found_pair = []

    while left_pointer < len(sorted_arr):
        while right_pointer > 0:
            pointers_sum = sorted_arr[left_pointer] + sorted_arr[right_pointer]
            if left_pointer == right_pointer:
                return []
            if pointers_sum == target:
                #  print(sorted_arr[left_pointer], sorted_arr[left_pointer])
                found_pair.append(sorted_arr[left_pointer])
                found_pair.append(sorted_arr[right_pointer])
                return found_pair
            elif pointers_sum > target:
                right_pointer -= 1
            elif pointers_sum < target:
                left_pointer += 1
        

arr = [5, 6, 6, 8,  2, 4, 7]
target = 16
print(find_sum(arr, target))
