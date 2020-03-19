

def FindPower(a):
    nmp=a
    while nmp & (nmp-1) != 0:
        nmp= nmp & (nmp-1)
    print(nmp)
    power=0
    while(nmp != 1):
        power+=1
        nmp/=2
    return power

a = int(input())
print(FindPower(a))
