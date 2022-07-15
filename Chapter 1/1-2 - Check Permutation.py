"""
Page 90
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""
def check_permutation(string1:str, string2):

    # If the strings are not the same length, they cannot be permutations
    # of one another.
    if len(string1) != len(string2):
        return False

    # If a character is in string 1 but not in string 2, the two strings are
    # not permutations of one another.
    for x in string1:
        if x not in string2:
            return False

    return True

print(check_permutation("1234", "3241"))
#print(all_unique_no_additional_structures("abcdefga"))
