def min_path(arr,i,j,m,n,dp):
    if i == m-1 and j == n-1:
        return arr[i][j]
    
    if i+1 <= m-1 and j <= n-1:
        if dp[i+1][j] == -1:
            ans1 = min_path(arr,i+1,j,m,n,dp)
            min_ans1 = arr[i][j] + ans1
        else:
            min_ans1 = arr[i][j] + dp[i+1][j]
    if i <= m-1 and j+1 <= n-1:
        if dp[i][j+1] == -1:
            ans2 = min_path(arr,i,j+1,m,n,dp)
            min_ans2 = arr[i][j] + ans2
        else:
            min_ans2 = arr[i][j] + dp[i][j+1]
    if i+1 <= m-1 and j+1 <= n-1:
        if dp[i+1][j+1] == -1:
            ans3 = min_path(arr,i+1,j+1,m,n,dp)
            min_ans3 = arr[i][j] + ans3
        else:
            min_ans3 = arr[i][j] + dp[i+1][j+1]
        
    if i == m-1 and j < n-1 :
        dp[i][j] = min_ans2
        return min_ans2
    elif i < m-1 and j == n-1:
        dp[i][j] = min_ans1
        return min_ans1
    else:
        dp[i][j] = min(min_ans1,min_ans2,min_ans3)
        return min(min_ans1,min_ans2,min_ans3)
    
    
    
    
l = [int(i) for i in input().split()]
m = l[0]
n = l[1]
arr = [[int(i) for i in input().split()] for j in range(m)]
dp = [[-1 for i in range(n)]for j in range(m)]
dp[m-1][n-1] = arr[m-1][n-1]
min_cost = min_path(arr,0,0,m,n,dp)
print(min_cost)
