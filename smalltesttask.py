import pyttsx3
import os

#pyttsx3.speak("welcome")
pyttsx3.speak("Hi, This is Ruby, your own application guide. Let me help you with the applications on this computer")
while True:
        print("Hey !! Ruby Please chat with me ")
        p = input()

        if ("Please run" in p) and ("chrome" in p):
          os.system("chrome")

        elif (("Please run" in p) or ("execute" in p )) and  (("notepad" in p) or ("editor" in p)):
          os.system("notepad")

        elif ("Please run" in p) and ("player" in p ) and  ("media" in p):
          os.system("wmplayer")

        elif ("Please run " in p) and ("execute" in p ) and  ("Application" in p):
          os.system("word")

        elif ("Please run " in p) and ("execute" in p ) and  ("Application" in p):
          os.system("NFSMW2005")

        elif ("exit" in p)  or ("quit" in p):
          break

        else:
          print(" we don't support this application")
          pyttsx3.speak("Please try again")

	
