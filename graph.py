##      0 -----> 1 ------> 4
##      |        |
##      |        |
##      |        |
##      |        V
##      |------> 3 ------> 5
##  2              <-----+

a = [[1,3],[3,4],[2],[5],[],[3]]

b =  [[0 for j in range(0,len(a))] for row in range(0,len(a))]

class Node:
    def __init__(self,data):
        self.children = []
        self.data = data
    def printout(self):
        print(self.data)


def adjToMat(adj,mat):
    for row,adjlist in enumerate(adj):
        for col in adjlist:
           mat[row][col] = 1 
    return mat

c = adjToMat(a,b)
def printMat(x):
    for i in x:
        print(i)
def prettyMat(x):
    colLabel = "  ".join([str(i) for i in range(0,len(x))])
    print(f"   {colLabel}")
    for row,i in enumerate(x):
        print(f"{row} {i}")
prettyMat(c)

def dfs(v):
    for row,adjlist in a:
        
