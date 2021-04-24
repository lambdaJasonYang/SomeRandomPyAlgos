#1182A Filling Shapes
x = int(input())
#1 way to tile no rows
    #base case f(0) = 1 #put no tile down
    #base case f(1) = 0 #impossible
#IH
    #2 ways to file 2 columns
    #fn = 2 * f[n-2]
def fun(n):
    f = [1]*(n+1)
    f[0] =  1
    f[1] = 0
    for i in range(2,n+1):
        f[i] = 2 * f[i-2]
    return f[n]
        
    

print(fun(x))
