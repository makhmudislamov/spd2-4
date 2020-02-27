"""
Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, 
return a list of all letter combinations they could have been trying to type on the keypad.

Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]
"""

T9_LETTERS = {  "2" : "abc", 
                "3" : "def",
                "4" : "ghi",
                "5" : "jkl",
                "6" : "mno",
                "7" : "pqrs",
                "8" : "tuv",
                "9" : "wxyz"               
                }

def t9_combos(digits, perms = []):
    if len(digits) == 0:
        return perms
    letters = T9_LETTERS[digits[0]]
    print(letters)
    perms.append(letters)
    # print(perms)
    new_perms = []
    for perm in perms:
        print("perm", perm)
        for letter in letters:
            # print("letter", letter)
            new_perms.append(perm + letter)
    return t9_combos(digits[1:], new_perms)
    

print(t9_combos("23", perms=[]))
