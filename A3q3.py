def oddEvenCount():         # creating the oddEventCount function
    takeInput = input("Enter the String : ")    # input the string
    countUpper = 0          # bydefault upper value is 0
    countLower = 0          # By default lower value is 0
    for index in takeInput:     # Iterating the String 
        if(index.isupper()):    # check if index value is upper ?
            countUpper +=1      # If true then countUpper = countUpper + 1
        elif(index.islower()):      # check if index value is lower ?
            countLower +=1          # If true then countLower = countLower + 1
        
    print(f"No. of Upper case characters : {countUpper}")       # Printing the count value of Upper
    print(f"No. of Lower case Characters : {countLower}")       # printing the count value of Lower

oddEvenCount()          # Calling the function



