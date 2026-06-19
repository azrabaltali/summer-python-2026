def BestTimeBuy(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # dp tablosu
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = -prices[0]
    
    for i in range(1, n):
        # hold: elimde hisse var
        dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
        
        # sold: sattım
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        # cooldown: bekliyorum
        dp[i][2] = max(dp[i-1][2], dp[i-1][1])
    
    return max(dp[n-1][1], dp[n-1][2])


prices = [1,2,3,0,2]
print(BestTimeBuy(prices))