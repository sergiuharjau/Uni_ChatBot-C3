def getMusic():

        print("Loading...")
        n=1
        import time
        import urllib
        import urllib.request
        import urllib.parse
        import re
        import pafy   #For the code to run you must install the latest pafy and youtube-dl
        import webbrowser

        print("Done.")
        user_search = urllib.parse.urlencode({"search_query" : input("Enter your search here... ")})       #Retrieves users search input
        print("Searching...")
        youtube_content = urllib.request.urlopen("http://www.youtube.com/results?" + user_search)     #Searches youtube using user input
        youtube_results = re.findall(r'href=\"\/watch\?v=(.{11})', youtube_content.read().decode())     #Retrieves the search results from youtube and decodes them
        url1 = "http://www.youtube.com/watch?v=" + youtube_results[0]      #Saves the url of the first search result
        url2 = "http://www.youtube.com/watch?v=" + youtube_results[1]
        url3 = "http://www.youtube.com/watch?v=" + youtube_results[2]
        url4 = "http://www.youtube.com/watch?v=" + youtube_results[3]
        url5 = "http://www.youtube.com/watch?v=" + youtube_results[4]
        url6 = "http://www.youtube.com/watch?v=" + youtube_results[5]      #Saves the url of the first search result
        url7 = "http://www.youtube.com/watch?v=" + youtube_results[6]
        url8 = "http://www.youtube.com/watch?v=" + youtube_results[7]
        url9 = "http://www.youtube.com/watch?v=" + youtube_results[8]
        url10 = "http://www.youtube.com/watch?v=" + youtube_results[9]
        video1 = pafy.new(url1)         #Assigns the url to pafy and names it video
        video2 = pafy.new(url2)
        video3 = pafy.new(url3)
        video4 = pafy.new(url4)
        video5 = pafy.new(url5)
        video6 = pafy.new(url6)         #Assigns the url to pafy and names it video
        video7 = pafy.new(url7)
        video8 = pafy.new(url8)
        video9 = pafy.new(url9)
        video10 = pafy.new(url10)
        print("Here's what I found:")
        print("1." + video1.title)         #Prints the exact title from youtube of the video
        print("2." + video2.title)
        print("3." + video3.title)
        print("4." + video4.title)
        print("5." + video5.title)
        while True:
                choice1 = input("Choose the correct song by typing the correct number: ")
                print("Press Enter to see the next 5 options... ")

                if choice1 == '1':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url1) 
                        return()#Opens the url in your default browser
                elif choice1 == '2':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url2)
                        return()
                elif choice1 == '3':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url3)
                        return()
                elif choice1 == '4':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url4)
                        return()
                elif choice1 == '5':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url5)
                        return()
                elif choice1 == '':
                        print("6." + video6.title)         #Prints the exact title from youtube of the video
                        print("7." + video7.title)
                        print("8." + video8.title)
                        print("9." + video9.title)
                        print("10." + video10.title)
                        while True:
                                choice1 = input("Choose the correct song by typing the correct number: ")
                                if choice1 == '6':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url6) 
                                        return()#Opens the url in your default browser
                                elif choice1 == '7':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url7)
                                        return()
                                elif choice1 == '8':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url8)
                                        return()
                                elif choice1 == '9':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url9)
                                        return()
                                elif choice1 == '10':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url10)
                                        return()
                                else:
                                        print("Sorry that was not an option, try again")
                        
                else:
                        print("Sorry that was not an option, try again")

getMusic()
