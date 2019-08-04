
def minSteps(n,dp):
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    i = 3
    while(i<=n):
        
        if i%2 == 0 and i%3 == 0:
            dp[i] = 1+min(dp[i-1],dp[i//2],dp[i//3])
        elif i%2 == 0 and i%3 != 0:
            dp[i] = 1+min(dp[i-1],dp[i//2])
        elif i%2 != 0 and i%3 == 0:
            dp[i] = 1+min(dp[i-1],dp[i//3])
        else:
            dp[i] = 1+dp[i-1]
            
        i=i+1
    return dp[n]
    
    


n = int(input())
dp = [-1 for i in range(n+1)]
print(minSteps(n,dp))
