#Reversing a linkedlist
class ll:
    def __init__(self,content):
        self.content = content
        self.next = None
a = ll(3)
b = ll(4)
c = ll(7)
a.next = b
b.next = c
def outp(k):
    if k == None:
        return
    else:
        print(k.content)
        outp(k.next)
outp(a)

def rev(k):
    if k == None:
        return k
    elif k.next == None:
        return k
    else:
        IH = rev(k.next)
        k.next.next = k
        k.next = None
        return IH
outp(rev(a))
