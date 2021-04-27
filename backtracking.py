def SubsetSum(X,T):
    if T == 0:
        return True
    elif T < 0 or X == []:
        return False
    else:
        x = X[0]
        With = SubsetSum(X[1:],T-x)
        Wout = SubsetSum(X[1:],T)
        return(With or Wout)
Xa = [8,6,7,5,3,10,9]
Ta = 15
SubsetSum(Xa,Ta)

def ConstructSubset(X,i,T):
    if T == 0:
        return []
    if T < 0 or i == 0:
        return None;
    Y = ConstructSubset(X,i-1,T)
    if Y != None:
        return Y
    Y = ConstructSubset(X,i-1,T-X[i])
    if Y != None:
        return Y + [X[i]]
    return None
    
ConstructSubset([8,6,7,5,3,10,9],10,15)
def IsWord(x):
    return x in {"BOTH","EARTH","AND","SATURN",""}
def splittable(A):
    n = len(A)
    if n == 0:
        return True
    for i in range(0,n):
        if IsWord(A[0:i+1]):
            if splittable(A[i+1:n]):
                return True
    return False
splittable("BOTHEARTH")


