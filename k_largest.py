"""
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  =>  [6, 8, 7]
"""

def largest(arr, k):
    # APPROACH 1
    # sort the array
    # slice the last k part
    # return the list

    # sorted_arr = sorted(arr)
    # largest_k = sorted_arr[-k:]
    # return largest_k

    # APPROACH 2
    # loop over the arr
    # keep track of up to k largest
    # values seen so far in a new array
    largest_k = [] # length = k
    index = 0

    while index < len(arr) and len(largest_k) != k:
        # loop over
        # compare neighbour values
        # append the largest
        # during second and more iterations
        # check if the value at specific index is in the new array.
        # dont append the already existing value
        index += 1



arr = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3
print(largest(arr, k))
