def longestCommonSubsequence(a, b):
    m=len(a)
    n=len(b)
    dp=[]
    
    for i in range(m+1):
        dp.append([])
        for j in range(n+1):
            dp[i].append((0,''))
                
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=(1+dp[i-1][j-1][0],dp[i-1][j-1][1]+' '+str(a[i-1]))   
            else:
                if dp[i-1][j][0]>dp[i][j-1][0]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i][j-1]
                    
    return dp[-1][-1][-1][1:]
  
