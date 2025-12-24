# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 
# We will solve this problem using bit mask
"""
Docstring for Arrays_&_Hashing.isUnique
ASCII: Total characters:128 (letters, digits and symbols)
Unicode: Universal characters to represent (languages, symbols, emojis)
Note: “ASCII is a 7-bit encoding that supports only English characters, while Unicode is a universal standard that represents characters from all languages, symbols, and emojis.”
Implementation:
1. If str.length>128: return False (cannot form a string of unique characters)
2. Use boolean arr[128] and set the flag if the character i is contained in the string
"""
def is_unique_naive(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def isUnique_ascii(s) -> bool:
    """
    Docstring for isUnique_ascii
    
    :param s: T.C is O(n), S.C is O(1) => since the loop will never iterate through more then 128 characters
    :return: Description
    :rtype: bool
    """
    if len(s) > 128: # ASCII has only 128 unique characters
        return False
    char_set = [False] * 128
    for ch in s:
        ascii_val = ord(ch)
        if char_set[ascii_val]:
            return False
        char_set[ascii_val] = True
    return True

"""
Better optimization: Bit vector using a single int (lowercase a–z)
seen = [False, False, True, False, ...];  Boolean list: 128 Python objects
checker = 00000000000000000000000000000100; Bit mask: One integer

Bit masking requires three strict conditions:
- The character set size is small (0-25)
- The size is fixed and known in advance
- Each character maps cleanly to a bit index

"""
def is_unique_bitmask(s: str) -> bool:
    checker = 0 #checker = 000000

    for ch in s:
        val = ord(ch) - ord('a')  # map a–z → 0–25 ; 'a' → val = 0; 'b' → val = 1
        if checker & (1 << val): # 1 << 0 = 000001; 1 << 1 = 000010
            return False
        checker |= (1 << val) # checker |= mask → 000001; checker |= mask → 000011

    return True



"""
- When you extend this to Unicode, the main change is that you can no longer assume a fixed size of 128 characters.
- Unicode has over 1 million possible code points, so a fixed boolean array is not practical.
In Unicode:
    - Max code point ≈ 1,114,112
    - Boolean array of that size is wasteful and slow to initialize

"""
# Use a list: still bad O(n^2)
# seen = []
# for ch in s:
#     if ch in seen:  # ❌ O(n)
#         return False
#     seen.append(ch)

# A set is built for fast membership checks
def isUnique_unicode_set(s)->bool:
    seen = set()
    for ch in s:
        if ch in seen:   # O(1)
            return False
        seen.add(ch)     # O(1)

# A dict is just a set with values.
# set     → hash table storing keys only
# dict    → hash table storing key value pairs




print(isUnique_ascii("apple"))
print(isUnique_ascii("aple"))

