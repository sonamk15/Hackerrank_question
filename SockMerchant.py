def soctkMerchan(ar):
    ar.sort()
    # print ar
    new=[]
    i=0
    while i<len(ar)-1:
        if ar[i] == ar[i+1]:
            new.insert(0,[ar[i],ar[i+1]])
            ar.remove(ar[i])
        i+=1
    return len(new)
print sockMerchant([10, 20, 20, 10, 10, 30, 50, 10, 20])