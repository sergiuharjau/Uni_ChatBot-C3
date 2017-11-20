import socket,sys,time

def clientBackbone():
    host = "127.0.0.1"
    port = 5009
        #credentials needed to connect to the server
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
        #crucial bit of coding
    from accountClientSide import createUsername,createPassword,accountClientSide
           #imports the functions involved with account management
    print("Welcome to Zach Industries! We will now prompt you with the account manager.")
    
    n=0
   
    while True:
        dictionary=accountClientSide(n)
        
        username=dictionary["username"]  #pulls out values from dictionary
        password=dictionary["password"]
        login=dictionary["login"]
        
        sentMsg= username+ "       " +password + "       " + login
                           #puts them into a string so we can send them accross 
        thisSocket.send(sentMsg.encode())
        
        n = thisSocket.recv(1024).decode()
        if n== "Wrong":   
            print("Credentials don't match out database.")
            n=0
        if n== "Confirmed":
            print("You have successfullly logged in!")
            break
        else:
            n=int(n)  #the process starts again 
    
    print("You can now start chatting with Zach!")
        
    
    thisSocket.send(" ".encode())   
    
    infoString= thisSocket.recv(1024).decode()
    
    userInfoList=infoString.split(" ")   #gets a list from the server with all the info about the uesr 
    
    if userInfoList[0] == "" or userInfoList == " ":   #if the client doesn't have a name, ask him for one 
        print("It seems it's the first time you've ever logged in!")
        while True:
            terminalName = input("Input a name which the chatbot will call you: ") 
            if " " in terminalName or terminalName=="":
                print("Sorry, usernames can't be blank or contain spaces.")
            else:
                break
        terminalName= "   456   " + terminalName
        thisSocket.send(terminalName.encode())   #index it into the server 
        
        terminalName= thisSocket.recv(1024).decode()   #receive it back
        print("Everything is in order! Thanks.")
    else:
        terminalName=userInfoList[0]   #set the Terminal Name 
    
    while True:    
        
        message = input(terminalName + ": ")
        
        if message == "end": #keeps the conversation open until the user types end
            break
            
        from youtube import getMusic
        from manualplaylistCreator import manualCreatePlaylist
        
        if "music" in message and "play" in message:
            getMusic()
        elif "create" in message and "playlist" in message:
            pass#manualCreatePlaylist()
        else:
            message="Whoops we haven't coded that in yet"
            
        thisSocket.send(message.encode())
              #send the message to the server
                              
        receivedMess = thisSocket.recv(1024).decode()
                     
        print("Zach: ",end="") 
        print(receivedMess)    #Name of ChatBot
               
    thisSocket.close()
       
    print("I hope you enjoyed our services!")
        #this is where we print a final statement to the user

if __name__=="__main__":
    try:
        clientBackbone()
    except KeyboardInterrupt:
        print("\nShuting down. See you soon!")
        
        

        