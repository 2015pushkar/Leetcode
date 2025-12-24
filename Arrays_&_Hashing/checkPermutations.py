"""
Docstring for Arrays_&_Hashing.checkPermutations
Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
other.
Questions to ask:
1. Is the permutation comparison case sensitive; Eg: God a permutation of dog?
2. If whitespace is significant

We will assume for this problem that the comparison is case sensitive and 
whitespace is significant. So, "god " is different from "dog". 

first that strings of different lengths cannot be permutations of each other
"""
""" Solution #1: Sort the strings. 
If two strings are permutations, then we know they have the same characters, but in different orders. There
fore, sorting the strings will put the characters from two permutations in the same order. We just need to 
compare the sorted versions of the strings. 

Time Complexity
Sorting takes O(n log n)

Space Complexity
Sorting creates new lists → O(n)

"""
def checkPermutations_sort(s1: str, s2: str) -> bool:
    # check Length
    if len(s1) != len(s2):
        return False
    # Step 2: Sort both strings
    return sorted(s1) == sorted(s2)

"""
Solution #2: Check if the two strings have identical character counts. 
"""
def checkPermutations_freq(s1: str, s2: str) -> bool:
     # check Length
    if len(s1) != len(s2):
        return False
    count = [0]*128
    for ch in s1:
        count[ord(ch)] += 1
    for ch in s2:
        count[ord(ch)]-=1
        if count[ord(ch)]<0:
            return False
    return True

print(checkPermutations_sort("god ", "dog"))
print(checkPermutations_freq("god", "dog"))
