# import necessary libraries to make a script that makes the user's computer play the song "Never Gonna Give You Up" by Rick Astley
import webbrowser
import time
import os

# define the function that will play the song
def rickroll():
    # open the link to the song in a web browser
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # wait 10 seconds
    time.sleep(20)
    # close the web browser
    os.system("taskkill /im chrome.exe /f")
    

# call the function
rickroll()

# exit the window
exit()
