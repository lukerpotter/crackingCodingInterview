"""
Page 90
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""
def all_unique(stringToCheck:str):
    letters_already_seen = []

    for x in stringToCheck:
        if x in letters_already_seen:
            return False

        letters_already_seen.append(x)

    return True

def all_unique_no_additional_structures(stringToCheck: str):

    for outer_idx, outer_val in enumerate(stringToCheck):
        print(f"{outer_val}")
        for inner_val in stringToCheck[outer_idx + 1:len(stringToCheck)]:
            print(f"    {inner_val}")
            if outer_val == inner_val:
                return False

    return True

print(all_unique("abcdefga"))
print(all_unique_no_additional_structures("abcdefga"))
