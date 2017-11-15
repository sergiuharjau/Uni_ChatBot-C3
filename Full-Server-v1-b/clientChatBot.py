import socket,sys,time

def clientBackbone():
    host = "127.0.0.1"
    port = 5007
        #credentials needed to connect to the server
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
        #crucial bit of coding
    from accountManager import createUsername,createPassword,accountMain
           #imports the functions involved with account management
    print("Welcome... I'm Zach, your friendly robot companion and personal DJ")
    user=accountMain() #main account function, returns the username of the client
       #to note, people can't talk with the ChatBot without having an account. 
    print("Systems Online!")
    message = input(user + ": ")
        #we initialise it here in order to prevent an error
    while message != "end":    #keeps the conversation open until the user types end
        thisSocket.send(message.encode())
              #send the message to the server
        receivedMess = thisSocket.recv(1024).decode()
        
          # This is the same deal like with the server, this is where we will input the actual "music"
          # At the moment I will just put a placeholder print function, to see that it works
          
        from userInput import slow_type  #function which makes Zach type like a human
         
        print("Zach: ",end="")   #Name of ChatBot
        if receivedMess== "DESTROY ALL HUMANS!":
          slow_type(receivedMess,True)
        else:
          slow_type(receivedMess,False)   #calls the slow_type function 
        
        file= open("curseCount.txt", "r")
        doc= file.read()
        convert_List=doc.split()
        wordsinList= len(convert_List)
          
        message = input(user + ": ")
        if Message == "DESTROY ALL HUMANS!":
          break
              #we ask the user to input some more text, keep the conversation open
    thisSocket.close()
    file1=open("curseCount.txt","w")
    file1.close()
        #when the user types end, the loop breaks, and the connection closes
    print("I hope you enjoyed our services!")
        #this is where we print a final statement to the user

if __name__=="__main__":
    try:
        clientBackbone()
    except KeyboardInterrupt:
        print("\nShutting down. See you soon!")
        
        

        