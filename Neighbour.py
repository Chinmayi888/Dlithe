def max_stolen_value(val):
    n = len(val)
    if n == 0:
        return 0
    if n == 1:
        return val[0]
    dp = [0] * n
    dp[0] = val[0]
    dp[1] = max(val[0], val[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], val[i] + dp[i-2])
    return dp[-1]
val = [6, 7, 1, 3, 8, 2, 5]
print(max_stolen_value(val))  
