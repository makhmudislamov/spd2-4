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

def similarity_score(new_handle, all_handles):
    """
    STEP1: could be helper function that compares two handles
    compare two same length handles
    return the score
    """
    score = 0
    new_handle = new_handle.lower()
    all_handles = all_handles.lower()
    new_handle = set(new_handle)
    all_handles = set(all_handles)
    print(new_handle)
    print(all_handles)
    for char in new_handle:

        if char in all_handles and char.isalpha():
            score += 1
        elif not char.isalpha():
            continue
        else:
            score -= 1
        print(char, score)
    return score

def step2(new_handle, all_handles):
    
    pass


new_handle = 'iLoveDogsS'
all_handles = 'eDogeCoin'

print(similarity_score(new_handle, all_handles))
