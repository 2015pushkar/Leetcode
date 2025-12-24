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
def isUnique(s) -> bool:
    if len(s) > 128: # ASCII has only 128 unique characters
        return False
    char_set = [False] * 128
    for ch in s:
        ascii_val = ord(ch)
        if char_set[ascii_val]:
            return False
        char_set[ascii_val] = True
    return True
print(isUnique("apple"))
print(isUnique("aple"))

