def revString():            # creating a function for reversing the string
    revStr = []         # for storing the reverse string
    takeInput = input("Enter The String : ")    # enter the string
    revStr = takeInput[::-1]    # reversing  the string using slice method
    print(revStr)       # printing the reverse string

revString()         # calling the function