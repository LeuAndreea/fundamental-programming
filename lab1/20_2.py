def FindPower(a):
    power=0
    nmp=1
    while (nmp <= a):
        nmp*=2
        power+=1
    return power-1

a=int(input())
print(FindPower(a))
