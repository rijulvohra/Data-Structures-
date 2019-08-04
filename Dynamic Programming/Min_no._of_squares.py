

import sys
sys.setrecursionlimit(10000)
def minStepsTo1(n,dp):
    #Implement Your Code Here
    if(n == 0):
        return 0
    i = 1
    ans = 1000000
    while i*i <= n:
        #currAns = 1+minStepsTo1(n-i*i,dp)
        if dp[n] != -1:
            currAns = dp[n]
            return currAns
        else:
            currAns = 1 + minStepsTo1(n - i*i,dp)
        ans = min(ans,currAns)
        
        
        
        i = i+1
    dp[n] = ans
    return ans
        

        

    
n = int(input())
dp = [-1 for i in range(n+1)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
ans = minStepsTo1(n,dp)
print(ans)





