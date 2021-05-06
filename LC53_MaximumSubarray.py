#dp[i] gets largest subarray that ends at i,
#NOTE THIS MEANS WE MUST INCLUDE n[i]

#PREFIX optimization method
def MaxS(n):
    l = len(n)
    dp = [0] * l
    dp[0] = n[0]
    for i in range(1,l):
        if (dp[i-1]) > 0: #the previous subarray dp[i-1] can either help or not
            dp[i] = dp[i-1] + n[i] #The largest subarray that ends at i
            
        else:
            dp[i] = n[i] #if previous subarray doesnt help, we do not include dp[i-1]
            
        
    return max(dp) #dp represents several local maximas at different ending points
                   #we want the max to get the global maxima
    
    
print(MaxS([-2,1,-3,4,-1,2,1,-5,4])) 
