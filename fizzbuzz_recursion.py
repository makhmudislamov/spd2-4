"""
Let’s practice recursion on a very well-known (and pretty tired, tbh) interview problem.
You’re asked to write recursive FizzBuzz. 
Your function takes 2 integers: start and end, 
which are the first and last number in the sequence of integers to return in a list (array). 
However, if the number is a multiple of 3, put “Fizz” in the list instead of the number. 
If it’s a multiple of 5 put “Buzz” in the list. If it’s a multiple of 3 and 5, put “FizzBuzz” in 
the list.
Example: fizzbuzz(1, 20) ⇒ [1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, 
Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz]
"""

def recursive_fizzy(start, end):
    # declare start
    # declare empty array
    # if start % 3 == 0:
    # append "Fizz"
    # elif start % 5 == 0:
    # appemd "Buzz"
    # elif start % 3 and start % 5:
    # append "FizzBuzz"
    # else append the number itself
    # return the array

    # TASK1
    # recursively add numbers to array
    fizzy_array = []
    # recursifve function should 
    # do the division
    num = start
    while num <= end:
        if num % 3 == 0 and num % 5 == 0:
            fizzy_array.append("FizzBuzz")
        elif num % 3 == 0:
            fizzy_array.append("Buzz")
        elif num % 5 == 0 :
            fizzy_array.append("Fizz")
        else:
            fizzy_array.append(num)
        num += 1
        recursive_fizzy(num, end)

    return fizzy_array


print(recursive_fizzy(1, 20))
