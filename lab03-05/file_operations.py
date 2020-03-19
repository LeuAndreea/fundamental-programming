
def readFromFile(filename):
    l= [ ]
    try:
        fin= open(filename, "r")
        length=int (fin.readline( ))
        s=fin.readline( )
        fin.close( )
        s.strip( )
        s=s.split(",")
    except IOError as ex:
        print("Invalid file!" + str(ex))    
    i=0
    j=0
    while ( i<len(s) and  j<length):
        try:
            l.append(int(s[i]))
            j+=1
        except ValueError as ex:
            pass
        i+=1
    ###if (len(l) != length):
     ###   print("File not containing enough numbers!")        
    return l 

def writeToFile(l,filename):
    try:
        fout=open(filename,"w")
        for el in l:
            fout.write(str(el) + " ")
        fout.close()
    except IOError as ex:
        print("Invalid file!" + str(ex))

l=readFromFile("input.txt")
print(l)
writeToFile(l,"output.txt")
