def climbStairsREC(n: int) -> int:
    # Base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Recursive case
    return climbStairs(n - 1) + climbStairs(n - 2)

def climbStairsTDM(n: int) -> int: # REC + TD MEMO
    memo = {1:1, 2:2}
    def f(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = f(n-2) + f(n-1)
            return memo[n]
    return f(n)

n = 3
print(climbStairsTDM(n))