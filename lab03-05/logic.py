'''
Created on Oct 27, 2018

@author: Leut
'''

def listToString(participants):    
    '''
    Description: transforms the list into a string for printing purposes
    Input: a list
    Output: the list converted into a string
    '''
    scores=""
    for el in participants:
        scores+=str(el)+" "
    return scores

def test_listToString( ):
    assert listToString([  ])==""
    assert listToString([12])=="12 "
    assert listToString([13,25,44,67,54])=="13 25 44 67 54 "
    assert listToString([ 10,10,10,10,100 ])=="10 10 10 10 100 "
    assert listToString([ 25,70,64,44 ])=="25 70 64 44 "

test_listToString( )


def storeOperations(operations,participants):
    '''
    Description: the list operations stroes all the modification ever made to the scores of participants,
        in order to make undoing operations possible
        -it checks if the list of score was changed after each request from the user
    Input: the list operations containining all the modifications made to the participants, the current scores list
    Output: the updated operations list
    '''
    if operations==[ ]:
        operations.append(participants[:])
    if operations[len(operations)-1] != participants:
        operations.append(participants[:])
    ###print(listToString(participants))
    return operations
    

def test_storeOperations():
    assert storeOperations ( [ [2,7,8,4], [2,7], [2,9,7,8,4] ], [2,9,7,8,4])==[ [2,7,8,4], [2,7], [2,9,7,8,4] ]
    assert storeOperations ( [ [20,12,13,4,5], [20,4,5], [20,29,12,13] ], [20,29,12,13,15])==[ [20,12,13,4,5], [20,4,5], [20,29,12,13],[20,29,12,13,15] ]
    assert storeOperations ( [[9,2,19,7], [2,19,7], [9,2,19]], [9,2,19])==[[9,2,19,7], [2,19,7], [9,2,19]]
    assert storeOperations ( [[5,4,16,17], [5,4,16], [5,4,17]], [5,4,17])==[[5,4,16,17], [5,4,16], [5,4,17]]
    assert storeOperations ( [[12,23,15,6], [12,6,23], [12,13,15]], [12,11,13,15])==[[12,23,15,6], [12,6,23], [12,13,15],[12,11,13,15]]

test_storeOperations( )

def addNewScore(participants, score):  
    '''
    Description: adds a new score into the list.
    Input: the list and the score which shall be added
    Output: the list containing the new added score.
    '''
    participants.append(score)
    return participants
    
def test_addNewScore( ):
    assert addNewScore([   ],20)==[20]
    assert addNewScore([0],0)==[0,0]
    assert addNewScore([1,2,3],4)==[ 1,2,3,4 ]
    assert addNewScore([10,10,10,10,100],100)==[10,10,10,10,100,100]
    assert addNewScore([25,70,64,44],50)==[25,70,64,44,50]
    
test_addNewScore( )


def insertNewScore(participants, index,score):
    '''
    Description: inserts a new score at a specified position
    Input: the list, the score which shall be inserted, the index where the score will be
    Output: the list with the new score inserted
    '''
    participants.insert(index, score)
    return participants

def test_insertNewScore( ):
    assert insertNewScore([  ],0,12 )==[12]
    assert insertNewScore([ 23 ],0,10)==[10,23]
    assert insertNewScore([ 1,2,3 ],3,4 )==[1,2,3,4]
    assert insertNewScore([25,70,64,44],2,50 )==[25,70,50,64,44]
    assert insertNewScore([13,25,44,67,54  ],3,67 )==[13,25,44,67,67,54  ]

test_insertNewScore( )

def removeScore(participants, index):
    '''
    Description: removes a score at a specified index
    Input:the list, the index where the score shall be deleted
    Output: the list with the score deleted    
    '''    
    del(participants[index])
    return participants

def test_removeScore( ):
    assert removeScore([10 ],0 ) == [  ]
    assert removeScore([100,27,33  ],2  ) == [100,27  ]
    assert removeScore([34,56,78,90,45,67,78  ],  4) == [34,56,78,90,67,78  ]
    assert removeScore([78, 45, 93, 6, 68  ],4  ) == [78, 45, 93, 6  ]
    assert removeScore([26, 69, 14, 85, 64, 39, 95, 48, 65, 36  ],  6) == [26, 69, 14, 85, 64, 39, 48, 65, 36]

test_removeScore( )


def removeMultipleScores(participants,stindex, fnindex):  
    '''    
    Description: removes scores between two specified indexes
    Input: the list and the indexes between which the elements shall be deleted
    Output: the list without the scores between the specified indexes  
    '''    
    i =1
    while i <= fnindex-stindex+1:
        del(participants[stindex])
        i+=1
    return participants

def test_removeMultipleScores ( ):
    assert removeMultipleScores([12 ],0  ,0  ) == [  ]
    assert removeMultipleScores([95, 22, 12, 16, 81, 61, 99],6 ,6  ) == [95, 22, 12, 16, 81, 61,   ]
    assert removeMultipleScores([25, 16, 13, 19, 7, 26, 40, 57, 6 ],0  ,8  ) == [  ]
    assert removeMultipleScores([46, 90, 82, 42, 79, 18, 88, 75, 78, 100], 6 ,7  ) == [46, 90, 82, 42, 79, 18,  78, 100  ]
    assert removeMultipleScores([58, 18, 61, 23 ],1  ,2  ) == [58, 23  ] 

test_removeMultipleScores( )
 
    
def replaceScore(participants, index,score):  
    '''
    Description: replaces the score from a specified position
    Input: the list, the score, the index where we shall replace the value
    Output: the list with the score replaced
    '''    
    participants[index]=score
    return participants

def test_replaceScore( ):
    assert replaceScore([ 12 ],0,11  ) == [ 11 ]
    assert replaceScore([2, 86, 25, 53, 12, 5  ],2,24    ) == [2, 86, 24, 53, 12, 5  ]
    assert replaceScore([ 80, 53, 86 ], 2,4    ) == [ 80, 53,4 ]
    assert replaceScore([ 64, 61, 45, 32, 74, 95, 41, 54, 99 ],6, 7    ) == [ 64, 61, 45, 32, 74, 95, 7, 54, 99 ]
    assert replaceScore([ 100, 12, 66, 16, 27, 76 ],5 ,19    ) == [100, 12, 66, 16, 27, 19  ]
    
test_replaceScore( )  

    

def findLessThan(participants,x):    
    ''' 
    Description: searches a list for elements less than x 
    Input: a list
    Output: a list containing only numbers less than x
    '''
    
    scores=[]
    for el in participants:
        if (el < x):
            scores.append(el)
    return scores

def test_findLessThan():
    assert findLessThan([30],31)==[30]
    assert findLessThan([50],50)==[ ]
    assert findLessThan([ 34, 79 ],51  ) == [34  ]
    assert findLessThan([3, 54, 39, 22, 64  ]  ,  56 )==[ 3, 54, 39, 22  ]
    assert findLessThan([99, 3, 25, 55, 22  ],  39 )==[   3, 25,  22 ]

test_findLessThan()


def findGreaterThan(participants,x):
    scores=[ ]
    for el in participants:
        if el>x:
            scores.append(el)
    return scores

def test_findGreaterThan( ):
    assert findGreaterThan([12,45,67,34],25 ) ==[45,67,34]
    assert findGreaterThan([20,6,8,25,40],10 ) ==[20,25,40]
    assert findGreaterThan([7,59,67,3,2,12],24 ) ==[59,67]
    assert findGreaterThan([25,32,64,89],90) ==[ ]
    assert findGreaterThan([9,41,32,12,20],21 ) ==[41,32]

test_findGreaterThan( )

def quickSort(participants,i,j):    
    '''    
    Description: sorts a given list between indexes i and j by a recursive method.
        -takes the first element as a pivot, and swap the elements such that
        when the loop is over all the elements less than the pivot shall be on its left,
        and the greater ones shall be on its right. 
        -the function recalls itself for sorting the elements of the list on the left of the pivot if there exists any,
        respectively on the right of it, such that eventualy all the list get sorted.
    Input: the list, the indexes between we must sort the elements 
    Output: the sorted list   
    '''
    low=i
    high=j
    direction=1
    if i==j:
        return
    while i!=j:
        if participants[i]>participants[j]:
            aux=participants[i]
            participants[i]=participants[j]
            participants[j]=aux
            direction *= -1
        if direction==1:
            j=j-1
        else:
            i=i+1
    if j>low:
        quickSort(participants,low,j-1)
    if j<high:
        quickSort(participants,j+1,high)

def sortList(participants):    
    ''' 
    Description: sorts all the elements increasingly
        using quick sort.
    Input: a list
    Output: the sorted list,without modifying the original list
    '''    
    scores=participants[:]
    quickSort(scores,0,len(scores)-1)
    return scores
    
def test_sortList(  ):
    assert sortList([3,2,1])==[1,2,3]
    assert sortList([1])==[1]
    assert sortList([49, 10, 66, 32, 17])==[10, 17, 32, 49, 66]
    assert sortList([79,14,9,22, 59, 88, 30, 15 ]) == [ 9, 14, 15, 22, 30, 59, 79, 88  ]
    assert sortList([33, 34, 67, 44, 33, 54, 67 ]) == [33, 33, 34, 44, 54, 67, 67   ]
    
test_sortList(  )


def sortGreaterThan(participants,x):    
    ''' 
    Description: searches for numbers greater than x and sorts them
    Input: a list
    Output: a list containing only elements greater than x, sorted
        using quick sort
    '''
    scores=findGreaterThan(participants, x)
    if (len(scores)!=0):
        quickSort(scores,0,len(scores)-1)
    return scores

def test_sortGreaterThan():
    assert sortGreaterThan([ ], 80) == [  ]
    assert sortGreaterThan([1],75)==[  ]
    assert sortGreaterThan([4,6,8,90],8)==[90  ]
    assert sortGreaterThan([17, 9, 11, 18, 2],4)==[ 9, 11,17, 18]
    assert sortGreaterThan([10,100,23,92,93,100,101],90)==[92,93,100,100,101]

test_sortGreaterThan(  )


def findAverage(participants,stindex,fnindex):    
    '''     
    Description: calculates the average of elements in a list
        within a specified range.
    Input: start index (stindex), finish index (fnindex), a list
    Output: the average
    '''    
    s=0
    for i in range(stindex,fnindex+1):
        s+= participants[i]
    average=s/(fnindex-stindex+1)
    return average

def test_findAverage():
    assert findAverage([1,1,1,1,1],0,4) == 1
    assert findAverage([12],0,0) == 12
    assert findAverage([0,1,2],1,2)== 1.5
    assert findAverage([1,2,3,4,5,6,7],0,6)==4
    assert findAverage([14, 12, 16, 15, 19, 4, 7, 17, 10, 6],5,8, )== 9.5

test_findAverage()
 
    
def findMin(participants,stindex,fnindex):   
    ''' 
    Description: The function searches through a list in order to find a minimum
        within a given range.
    Input: start index (stindex), finish index (fnindex), a list
    Output: the minimum of the elements    
    '''    
    minimum=participants[stindex]
    for i in range(stindex+1,fnindex+1):
        if (participants[i]<minimum):
            minimum=participants[i]
    return minimum

def test_findMin():
    assert findMin([12],0,0)==12
    assert findMin([12,100,1,102],1,2)==1
    assert findMin([14, 12, 16, 15],0,2)==12
    assert findMin([9, 20, 19, 16, 3, 11, 10],1,5)==3
    assert findMin([2, 10, 12, 5, 4, 14],0,5)==2

test_findMin()


def findMultiplesOf(participants,stindex,fnindex,x):    
    ''' 
    Description: The function searches through a list in order to find multiples of x
            within a given range.
    Input: start index (stindex), finish index (fnindex), a list
    Output: list containing multiples of x    
    '''
    multiples=[]
    for i in range(stindex,fnindex+1):
        if (participants[i]%x==0):
            multiples.append(participants[i])
    return multiples

def test_findMultiplesOf():
    assert findMultiplesOf([10],0,0,10)== [10]
    assert findMultiplesOf([1,1,1,1,1],1,2,10)== [  ]
    assert findMultiplesOf([12,20,44,52,3,46,100,50],3,6,2)== [52,46,100]
    assert findMultiplesOf([0,0,0,0],0,3,59)==[0,0,0,0]
    assert findMultiplesOf([5, 14, 15, 3, 11, 75, 20, 16, 18, 13],1,5,3)==[15, 3, 75]

test_findMultiplesOf( )


def filterMultiplesOf(participants,score):
    '''
    Description: the function deletes the scores which are multiples of x.
    Input: a list
    Output: the list without the multiples of x.
    '''
    participants= findMultiplesOf(participants,0,len(participants)-1, score)
    return participants

def test_filterMultiplesOf():
    assert filterMultiplesOf([45,5,6,8,10],5)== [45,5,10]
    assert filterMultiplesOf([7,8,14,23,72],7)== [7,14]
    assert filterMultiplesOf([9,8,24,67,90,72],8)== [8,24,72]
    assert filterMultiplesOf([76,5,89,37,5],6)== [ ]
    assert filterMultiplesOf([60,89,49,70,10],10)== [60,70,10]

test_filterMultiplesOf()


def filterGreaterThan(participants, score):
    '''
    Description: the function deletes the scores which are greater than  x.
    Input: a list
    Output: the list without numbers greater than x..
    '''
    participants=findGreaterThan(participants, score)
    return participants
    
def test_filterGreaterThan():
    assert filterGreaterThan([3,7,9,1,2,20],5)==[7,9,20]
    assert filterGreaterThan([36,21,61,29,42],30)==[36,61,42]
    assert filterGreaterThan([16,28,88,37,51],40)==[88,51]
    assert filterGreaterThan([55,58,69,60,45],70)==[]
    assert filterGreaterThan([7,9,3,45,27,90,21],28)==[45,90]
    
test_filterGreaterThan( )

def undoOperation(operations,participants):
    '''
    Description: the function undoes the last operation done on the list participants,
        by using a list containing all the modifications made to the lsit participants
        -it empties the current list and then assigns it it's last form
    Input: a list
    Output: the list before the last operation
    '''
    operations.pop()
    
    while (participants!=[ ]):
        participants.pop()
    for el in operations[-1]:
        participants.append(el)
    return participants

def test_undoOperation():
    assert undoOperation ( [ [2,7,8,4], [2,7], [2,9,7,8,4] ], [2,9,7,8,4])==[2,7]
    assert undoOperation ( [ [20,12,13,4,5], [20,4,5], [20,29,12,13] ], [20,29,12,13])==[20,4,5]
    assert undoOperation ( [[9,2,19,7], [2,19,7], [9,2,19]], [9,2,19])==[2,19,7]
    assert undoOperation ( [[5,4,16,17], [5,4,16], [5,4,17]], [5,4,17])==[5,4,16]
    assert undoOperation ( [[12,23,15,6], [12,6,23], [12,13,15]], [12,13,15])==[12,6,23]
    
test_undoOperation( )