def accountServerSide(dictionary):
    if __name__=="__main__":
        x=input("Do you want to delete the database?\n")
        if x == "Yes, I do, avocados are great.":
            f1=open("database.txt","w")
            print("You monster.")
            f1.close()
        else:
            print("Nah, fam.")
        return()
    username=dictionary["username"]
    password=dictionary["password"]
    login=str(dictionary["login"])
    
    f1= open("database.txt", "r")
        #we open it in read mode
    string1= f1.read()
        #we read it as a stirng
    list1=string1.split()
        #we make it into a list
    f1.close()
    
    x=len(list1)
    
    listUser=list1[0:int(x/2)]
    listPass=list1[int(x/2):x]
    
    if login == "False":
        if username in listUser:
            return(1)
        listUser.append(username)
        listPass.append(password)
        list1=listUser+listPass
        
        f1=open("database.txt","w")        
        list1=listUser+listPass    
        string1=" ".join(list1)       
        f1.write(string1)
        f1.close()
        
        return(0)
    
    else:
        i=-1
        for element in listUser:
            i+=1
            if element == username:
                if listPass[i] == password:
                    return(7)
    return(2)


if __name__=="__main__":
    try:
        dictionary={}
        accountServerSide(dictionary)
    except KeyboardInterrupt:
        print("Shutting down.")
