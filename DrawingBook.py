n=input('total book page')
p=input('choose page no')
def pageCount(n, p):
    new=[]
    right=(n/2)-(p/2)
    new.append(right)
    new.append(p/2)
    new.sort()
    return (new[0])
print pageCount(n,p) 
