def longestPalindrome(s: str) -> str:
    """
    Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
    
    Example 2:
    Input: s = "cbbd"
    Output: "bb"

    Optimization: We want the longest palindrome
    - Check the longest length substrings and iterate toward the shorter-length substrings
    - This way the first time we find a substring that is a palindrome, we can imeediately return it as the answer
    
    Algorithm 1: Check all the substrings
    1. Create a helper to determine if a substring is a palindrome: check(i,j)
    """

    # def check(i, j):
    #     left = i
    #     right = j - 1

    #     while left < right:
    #         if s[left] != s[right]:
    #             return False

    #         left += 1
    #         right -= 1

    #     return True
    
    # # “Try every substring, but try long ones first so we can stop as soon as we find a palindrome.”
    # # It starts from the biggest possible length: len(s); Then goes down: len(s)-1, len(s)-2, ... , 1
    # # 5 -> [5,...,0] "babad"; length = 5
    # #  length = 4; start = 1 
    # for length in range(len(s), 0, -1):
    #     for start in range(len(s)-length+1):
    #         if check(start, start+length):
    #             return s[start:start+length]
    # return ""


    """
    Algorithm 2: Dynamic Programming
    """
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    ans = [0,0]
    # for len=1 - every word is a palindrome; setting all the diagonals to True
    for i in range(n):
        dp[i][i] = True
    # for len=2; if s[i] == s[i+1] then set dp[i][i+1] = True and update ans = [i,i+1]
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = [i,i+1]
    # Now iterate over diff
    for diff in range(2,n):
        for i in range(0, n-diff):
            j = i+diff
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                ans = [i,j]
    i,j = ans
    return s[i:j+1]

# def test():
res_str = longestPalindrome("babad")
    # assert res_str == "bab"
    # print(res_str)
    
# test()

