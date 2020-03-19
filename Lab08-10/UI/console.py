from DOMAIN.business import MyVector

class VectorUI():
    def __init__(self,controller):
        self.__controller=controller
    
    @staticmethod
    def printMenu():
        s="1-Add a new vector" + '\n'
        s+="2-Print all vectors" + '\n'
        s+="3-Get vector at index" + '\n'
        s+="4-Update vector at index" + '\n'
        s+="5-Update vector by id" + '\n'
        s+="6-Delete vector by index" + '\n'
        s+="7-Delete vector by id" + '\n'
        s+="8-Plot all vectors" + '\n'
        s+="9-Add a scalar to a vector" + '\n'
        s+="10-Add two vectors" + '\n'
        s+="11-Substract two vectors" + '\n'
        s+="12-Multiplicate two vectors" + '\n'
        s+="13-Compute the sum of the elemens of a vector" + '\n'
        s+="14-Compute the product of elements in a vector" + '\n'
        s+="15-Find the average of elements in a vector" + '\n'
        s+="16-Find the minimum of elements in a vector" + '\n'
        s+"17-Find the maximum of elements in a vector" + '\n'
        return s
    
    @staticmethod
    def readPositiveInteger(msg):
        n=-1
        while(n<0):
            n=int(input(msg))
        return n
    
    @staticmethod
    def readColour(msg):
        c=input(msg)
        while  c not in ["r", "g", "b", "y", "m"]:
            c=input(msg)
        return c
            

    @staticmethod
    def readValues():
        n=VectorUI.readPositiveInteger("Introduce the number of elemetns:")
        v=[ ]
        for i in range(n):
            v.append(int(input))
        return v
        
    @staticmethod
    def readVector():
        nameid= VectorUI.readPositiveInteger("Please introduce the id(must be a number greater than 0:")
        colour= VectorUI.readColour("Please introduce the colour (should be r, g, b, y, or m)")
        typev=VectorUI.readPositiveInteger("Please introduce the type(must be a number greater than 0:")
        values=VectorUI.readValues()
        return MyVector(nameid,colour,typev,values)
    
    def mainMenu(self):
        while True:
            VectorUI.printMenu()
            try:
                option=VectorUI.readPositiveInteger("Please enter a value:")
                if option== "0":
                    return
                elif option== "1":
                    v=VectorUI.readVector()
                    self.__controller.addVector()
                elif option== "2":
                    l=self.__controller.getVectors()
                    for el in l:
                        print(el+'\n')
                elif option== "3":
                    index=int(input("Give the index"))
                    v=self.__controller.getVectorAtIndex()
                    print(v)
                elif option== "4":
                    nameid=input("Introduce the id:")
                    print("Introduce the new vector")
                    v=VectorUI.readVector()
                    self.__controller.updateVectorById(nameid,v)
                elif option== "5":
                    index=int(input("Introduce the index:"))
                    print("Introduce the new vector")
                    v=VectorUI.readVector()
                    self.__controller.updateVectorByIndex(index,v)
                elif option== "6":
                    index=int(input("Introduce the index:"))
                    self.__controller.deleteByIndex(index)
                elif option== "7":
                    nameid=input("Introduce the id:")
                    self.__controller.deleteById(nameid)
                else:
                    self.__controller.draw()
            except Exception as ex:
                print("An error occured" + str(ex))
    