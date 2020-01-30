"""
reuturn the highest score handles based on common chars.
"""

def similarity_score(new_handle, all_handles):
    # should compare two strings and
    # +1 for common char
    # -1 for non-common char
    # return the total score

    score = 0
    new_handle = set(new_handle)
    all_handles = set(all_handles)
    print(all_handles)
    for char in new_handle:
        
        if char in all_handles:
            score += 1
        else:
            score -= 1
        print(char, score)
    return score




new_handle = 'iLoveDogs'
all_handles = 'eDogeCoin'

print(similarity_score(new_handle, all_handles))
