

def MySort(f,l):
    for i in range(len(l)):
        k=i
        while k>0 and not(f(l[k-1],l[k])):
            (l[k-1],l[k])=(l[k],l[k-1])
            k-=1
    return l

def MySearch(f,l):
    l2=[ ]
    for el in l:
        if f(el):
            l2.append(el)
    return l2

def MyFilter(f,l):
    return list(filter (lambda x:f(x),l))



