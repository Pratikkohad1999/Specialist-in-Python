import pyttsx3
import os

pyttsx3.speak("Hi, This is Ruby. Let me help you with the applications on this computer")
while True:
	print("Which application would you like to open:", end=' ')
	p=input()
	if("run " in p) or ("open "in p):
		if("not " in p) or ("do not " in p) or ("dont " in p):
			exit()
		else:

			if ("notepad "in p) or ("text edittor"in p):
				pyttsx3.speak("opening notepad") 
				os.system("notepad")
			elif("notepad++"in p):
				pyttsx3.speak("opening Notepad++") 
				os.system("Notepad++")
			elif("wmplayer"in p):
				pyttsx3.speak("opening Windows Media Player") 
				os.system("wmplayer")
			elif("chrome"in p) or ("browser" in p):
				pyttsx3.speak("opening Google Chrome: Your internet browser") 
				os.system("chrome")
			elif("codeblocks"in p):
				pyttsx3.speak("opening Code Blocks: Your C compiler") 
				os.system("codeblocks")
			elif("Mozilla Firefox"in p) or ("mozilla firefox"in p) or ("firefox"in p):
				pyttsx3.speak("opening Mozilla Firefox: Your internet browser") 
				os.system("Mozilla Firefox")
			elif("Access"in p) or ("access"in p):
				pyttsx3.speak("opening Microsoft Access") 
				os.system("MSACCESS")
			elif("Excel"in p) or ("excel"in p):
				pyttsx3.speak("opening Microsoft Excel") 
				os.system("EXCEL")
			elif("Powerpoint"in p) or ("powerpoint"in p):
				pyttsx3.speak("opening Microsoft :Powerpoint") 
				os.system("POWERPNT")
			elif("Word"in p) or ("word"in p):
				pyttsx3.speak("opening Microsoft Word") 
				os.system("WORD")
      elif("netbeans"in p) or ("Netbeans"in p):
				pyttsx3.speak("opening Netbeans") 
				os.system("Netbeans")
      elif("Explorer"in p) or ("explorer"in p):
				pyttsx3.speak("opening Explorer") 
				os.system("Explorer")
      elif("nfs"in p) or ("NFSMW2005"in p):
				pyttsx3.speak("opening NFSMW") 
				os.system("NFSMW")
			else:
				print("dont support")
				pyttsx3.speak("Please try again")
	elif("close"in p) or ("stop"in p) or ("exit"in p):
		pyttsx3.speak("Thanks! meet you later")
		exit()
	elif("hi "in p) or ("hello"in p) or ("hey"in p):
		pyttsx3.speak("Hello!! Please order me to open whatever you like from the above applications.")
	else:
		pyttsx3.speak(" Please repeat your command")
