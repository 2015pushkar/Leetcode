from typing import Counter
def allSubstrings(s):
    res = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            freq_table_each_substr = Counter(s[i:j])
            mx = max(freq_table_each_substr.values())
            mn = min(freq_table_each_substr.values())
            beauty = mx-mn
            print(s[i:j], freq_table_each_substr, beauty)
            if beauty > 0:
                res.append(s[i:j])
    return res
            
s = "aabcbaa"
print(allSubstrings(s))
