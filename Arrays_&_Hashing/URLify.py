"""
Docstring for Arrays_&_Hashing.URLify
URLify: Write a method to replace all spaces in a string with'%20'You may assume that the string 
has sufficient space at the end to hold the additional characters, and that you are given the "true" 
length of the string
Input: "Mr John Smith", trueLength = 13 
Output: "Mr%20John%20Smith"

Solution: A common approach in string manipulation problems is to edit the string starting from the end and working backwards.

We will use this approach in this problem. The algorithm employs a two-scan approach. In the first scan, we 
count the number of spaces. By tripling this number, we can compute how many extra characters we will 
have in the final string. 

In the second pass, which Is done in reverse order, we actually edit the string. When 
we see a space, we replace it with %20. If there is no space, then we copy the original character.

Note: 
1. In python string is immutable
2. 3 chars replacing 1 char, net extra is 2
"""
def URLify(s: str, true_len) -> str:
     # consider only the true content
    # s = s[:true_len]

    # first pass
    count_space = 0
    for ch in s:
        if ch == " ":
            count_space += 1
    count_space *= 2
    new_len = true_len + count_space
    arr = [""] * new_len

    i = true_len - 1
    j = new_len - 1

    while i>=0:
        if s[i] == " ":
            arr[j] = "0"
            arr[j-1] = "2"
            arr[j-2] = "%"
            j-=3
        else:
            arr[j] = s[i]
            j-=1
        i-=1
    return "".join(arr)

print(URLify("Mr John Smith", 13))