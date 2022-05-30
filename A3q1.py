def createList():       # function to create a List
    lst = []            # new empty list
    lenInput = int(input("Enter the list Length : "))       # length of the list
    for index in range(lenInput):           # iterating from 0 index
        takeInput = int(input("Enter Number : "))       # take the item for list
        lst.append(takeInput)           # adding those number into list using append 
    
    return lst          # returning the list for other use 


def allSum():       # adding all the number which is in List
    num = 0         # by default adding value num is 0
    newlst = createList()       #  calling the function and saving the return value
    for i in newlst:            # iterating newlst 
        num += i            # adding all those number 
    print(f"The Sum of list {newlst} is {num}")         # print the total sum of the list 



allSum()    # calling the allsum function