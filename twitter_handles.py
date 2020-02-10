"""
Twitter Follow Suggestions
You’re working an internship at Twitter and are tasked to improve suggestions for accounts to follow, 
which already works great for established accounts because it uses content from your tweets and other accounts 
you follow to suggest new ones. However, when a new user signs up none of this information exists yet, 
but Twitter still wants to make some follow suggestions. Your team asked you to implement a function that 
accepts a new user’s handle and an array of many other users’ handles, which could be very long – Twitter has 
over 330 million active accounts! You need to calculate a similarity score between a pair of handles by looking at 
the letters each contains, scoring +1 for each letter in the alphabet that occurs in both handles but scoring –1 
for each letter that occurs in only one handle. Your function should return k handles from the array that have 
the highest similarity score to the new user’s handle.

Example execution:
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrump', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']
"""

def similarity_score(new_handle, old_handle):
    """
    Helper function that compares two handles
    and returns the score
    """
    
    score = 0
    new_handle = new_handle.lower()
    old_handle = old_handle.lower()
    new_handle = set(new_handle)
    old_handle = set(old_handle)
    print(new_handle)
    print(old_handle)
    for char in new_handle:

        if char in old_handle and char.isalpha():
            score += 1
        elif not char.isalpha():
            continue
        else:
            score -= 1
        print(char, score)
    return score

def filter(new_handle, all_handles):
 
    # iterate over the list - all_handles
    # compare the length of new handle and each handle
    # append the handle if 
    # +-3 char len difference handles to empty list
    # return the list

    # OPTIMIZATION:
    # break new handle into substings in
    # uppercase >> iLoveDogs - 'i' 'Love' 'Dogs' 
    # substring should be longer than one char
    # check if old handles has this substring(s)
    pass


def score_mapper(new_handle, all_handles):
    # empty dictionary >> key, value - old handle and sim score 
    # call filter function
    # iterates though all handles:
    #   calls score calculator
    #   maps each handle and similarity score in dict
    # sorts in descending order based on score
    # return the dict?
    # TODO: check other data str since oyu;ll have to sort
    pass


def similar_handles(new_handle, all_handles, k):
    # call score mapper = dictionary
    # return first k number of items in the above 
    pass


new_handle = 'iLoveDogs'
all_handles = 'eDogeCoin'

print(similarity_score(new_handle, all_handles))
