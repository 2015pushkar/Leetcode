from collections import Counter

def lengthOfLongestSubstring(s: str) -> int:
    """
    - Check all the substrings one by one to see if it has no duplicate character.
    - allUnique - return True if all the characters in the substring are unique
    Hash table, string, sliding window
    """
    # Method-1
    # we enumerate over the substring using two indices i=0 to n-1 and j=i+1 to n
    # If a string has duplicate character, we return false - we can use a set here
    #  O(n^3)
    # def check(start, end):
    #     chars = set()
    #     for i in range(start, end+1):
    #         c = s[i]
    #         if c in chars:
    #             return False
    #         chars.add(c)
    #     return True

    # n = len(s)
    # res = 0
    # for i in range(n):
    #     for j in range(i, n):
    #         if check(i,j):
    #             res = max(res, j-i+1)
    # return res


    # Method-2: Sliding window
    # Maintain a hashmap and if any ch occurs more then once, drop the left most characters, until no duplicate characters.
    # The worst case each character will be visited twice by i and j T.C: O(2n) = O(n)
    # S.C: O(min(m,n))
    # chars = Counter()
    # left = right = 0 # left - contract the window, right - extend the window
    # res = 0
    # while right < len(s):
    #     r = s[right]
    #     chars[r] += 1

    #     while chars[r]>1:
    #         l = s[left]
    #         chars[l] -= 1
    #         left += 1
    #     res = max(res, right - left + 1)
    #     right+=1
    # return res

    # Method-3: Sliding window optimized
    # The above solution requires 2n steps. It could be optimized to require only n steps
    # Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. then we skip the character immediately when we found a repeated character.
    left = right = 0
    res = 0
    chars = {}
    while right < len(s):
        r = s[right]
        if r in chars.keys():
            left = max(left, chars[r])
        res = max(res, right-left+1)
        chars[r] = right + 1
        right+=1
    return res




print(lengthOfLongestSubstring("abcdeafbdgcbb"))

# def test():
#     assert lengthOfLongestSubstring("abcabcbb") == 3
#     assert lengthOfLongestSubstring("bbbbb") == 1
#     assert lengthOfLongestSubstring("pwwkew") == 3
#     assert lengthOfLongestSubstring("") == 0
#     print("All tests passed!")

# test()



