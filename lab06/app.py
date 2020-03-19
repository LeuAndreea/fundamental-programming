'''
Created on Jan 13, 2019

@author: Leut
'''


try:
    f= open("input","r")
    lst=f.read()
    lst=lst.split(" ")
    f.close()
except IOError as e1:
    print("Something was wrong with the file" +str(e1))
except ValueError as e2:
    print("Something is wrong as value" + str(e2))
    

    
try:
    f=open("output","w")
    for el in lst:
        f.write(el + " ")
    f.close()
except IOError as e1:
    print("Something was wrong with the file" +str(e1))
except ValueError as e2:
    print("Something is wrong as value" + str(e2))