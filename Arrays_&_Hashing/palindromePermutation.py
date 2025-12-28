"""
Docstring for Arrays_&_Hashing.palindromePermutation
- Strings with even length must have all even counts of characters. 
- Strings of an odd length must have exactly one character with an odd count. 
"""

from collections import Counter

def is_permutation_palindrome(s: str) -> bool:
    # normalize: lowercase and keep only letters
    cleaned = [ch.lower() for ch in s if ch.isalpha()]

    freq = Counter(cleaned)

    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True

print(is_permutation_palindrome("aabbcdd"))       # True
print(is_permutation_palindrome("tact coa"))      # True
print(is_permutation_palindrome("racecar"))       # True
print(is_permutation_palindrome("aabbcd"))        # False
print(is_permutation_palindrome("abc"))           # False
print(is_permutation_palindrome("Tact Coa"))      # True
