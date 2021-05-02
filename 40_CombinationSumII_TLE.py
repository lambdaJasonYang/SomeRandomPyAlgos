#40. Combination Sum II TLE
def combosum(s,t):
    if t == 0:
        return [[]]
    if len(s) == 0 and t != 0:
        return []
    #if s[0] == t:
    #    return [[t]]
    cand = s[0]
    rest = s[1:]
    newT = t-cand
    newOut = list(map(lambda x: [cand] + x,combosum(rest,newT)))
    return combosum(rest,t)+newOut
candidates = [2,5,2,1,2]
target = 5
bb = combosum(candidates,target)
vv = list(map(lambda x: x.sort(),bb))
c = []
for i in bb :
    if i not in c:
        c.append(i)
print(list(map(lambda x: list(x),c)))
