'''
Created on Jan 13, 2019

@author: Leut
'''
from business import MyPoint
from repository import PointRepository


def printMenu():
    s="Choose an option" + "\n"
    s+="0.Exit" +"\n"
    s+="1. Add a point to the repository" + "\n"
    s+="2. Print all points " + "\n"
    s+="3. Get a point at a given index " + "\n"
    s+="4. Print all points of a given colour " + "\n"
    s+="5. Print all points that are inside a given square " + "\n"
    s+="6. Get all points that are inside a given rectangle " + "\n"
    s+="7. Get all points that are inside a given circle " + "\n"
    s+="8. Get the minimum distance between two points " + "\n"
    s+="9. Get the maximum distance between two points " + "\n"
    s+="10. Update a point at a given index" + "\n"
    s+="11. Update the colour of a point given its coordinates " + "\n"
    s+="12. Shift all points on the x axis " + "\n"
    s+=" 13. Shift all points on the y axis" + "\n"
    s+="14. Delete a point by index " + "\n"
    s+="15. Delete a point by coordinates " + "\n"
    s+="16. Delete all points that are inside a given square " + "\n"
    s+="17. Plot all points in a chart " + "\n"
    s+="18. Get and set the value of all properties for a point.  " + "\n"
    
    return s
    
def start():
    repo=PointRepository()
    printMenu()
    option=int(input("Give option:"))
    while (option!=0):
        if option==1:
            coord_x=input("Introduce the x coordinate:")
            while(int(coord_x)!=coord_x):
                coord_x=input("Introduce a number!")
            coord_y=input("Introduce the y coordinate: ")
            while(int(coord_y)!=coord_y):
                coord_y=input("Introduce a number!")
            colour=input("Introduce the colour. (Available colours are: red,green, blue, yellow and magenta)"+"\n")
            while colour not in ["red", "green", "blue", "yellow" , "magenta"]:
                colour=input("Unavailable colour. Try again!")
            p=MyPoint(int(coord_x),int(coord_y),colour)
            repo.add_point(p)
        if option==2:
            lst=repo.getall()
            for el in lst:
                print(el + "\n")      
        if option==3:
            index=int(input("Introduce the index:"))
            print(repo.get_point_at_index(index))
        if option==4:
            colour=input("Introduce the colour:")
            lst=repo.get_points_of_colour(colour)
            if len(lst)==0:
                print("There are no " + colour + " points.")
            else:
                for el in lst:
                    print(el + "\n")    
        if option==5:
            x=input("Introduce the x coordonate of the upper-left corner:")
            while(int(x)!=x):
                x=input("Introduce a number!")
            y=input("Introduce the y coordonate of the upper-left corner:")
            while(int(y)!=y):
                y=input("Introduce a number!")
            length=input("Introduce the length:")
            while(int(length)!=length):
                length=input("Introduce a number!")
            lst=repo.get_points_inside_sqaure(int(x), int(y), int(length))
            for el in lst:
                print(el + '\n')
        if option==6:
            x=input("Introduce the x coordonate of the upper-left corner:")
            while(int(x)!=x):
                x=input("Introduce a number!")
            y=input("Introduce the y coordonate of the upper-left corner:")
            while(int(y)!=y):
                y=input("Introduce a number!")
            length=input("Introduce the length:")
            while(int(length)!=length):
                length=input("Introduce a number!")
            width=input("Introduce the width:")
            while(int(width)!=width):
                width=input("Introduce a number!")
            lst=repo.get_points_inside_rectangle(int(x), int(y), int(length),int(width))
            for el in lst:
                print(el + '\n')    
        if option==7:
            
        if option==8:
            
        if option==9:
            
        if option==10:
            
        if option==11:
        if option==12:
        if option==13:
        if option==14:
        if option==15:
        if option==16:
        if option==17:
        if option==18:
        
        