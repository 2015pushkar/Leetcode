def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0): # if an element in S don't exist in T at all. then consider it as 0
                return False
        return True

'''
        Here we use two dictionaries to count the frequency of each character in both strings.
        If the frequency counts are the same, then the strings are anagrams of each other.
        This allows us to check for anagrams in a single pass through the strings.
'''