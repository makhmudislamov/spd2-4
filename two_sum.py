def find_sum(arr, t):
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

    print(sorted_arr)

    pass




arr = [5, 3, 6, 8, 2, 4, 7]
t = 10
print(find_sum(arr, t))
