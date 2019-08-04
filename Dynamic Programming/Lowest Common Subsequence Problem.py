
def lcsDP(s1, s2,i,j,dp):


    if i == len(s1) or j == len(s2):
        return 0
    if s1[i]==s2[j]:
        if dp[i+1][j+1] == -1:
            smallAns = lcsDP(s1,s2,i+1,j+1,dp)
            dp[i+1][j+1] = smallAns
            ans = 1 + smallAns
        else:
            ans = 1 + dp[i+1][j+1]
    else:
        if dp[i+1][j] == -1:
            ans1 = lcsDP(s1,s2,i+1,j,dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]
        if dp[i][j+1] == -1:
            ans2 = lcsDP(s1,s2,i,j+1,dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
        ans = max(ans1,ans2)
    return ans
    

s1 =input().strip()
s2 =input().strip()
n = len(s1)
m = len(s2)
dp = [[-1 for i in range(m+1)] for j in range(n+1)]
print(lcsDP(s1, s2,0,0,dp))
