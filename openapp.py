
# import required module
import pyttsx3
import os

""" 
# driver codeo
 
# create object and assign voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
 
# changing index changes voices but only
# 0 and 1 are working here
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
print("")
print("")
 
# introduction
print("  =============================================== Hello World!! ================================================")
engine.say('Hello World!!')
 
print("")
print("    My name is Divy Shah,I make this tool With this help of tool you can open below things.......")
 
print("\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER     \t 6.ADOBE ILLUSTRATOR \n\t 7.ADOBE PHOTOSHOP \t 8.MICROSOFT EDGE \n\t 9.NOTEPAD        \t 10.TELEGRAM \n\n\t\t     0. FOR EXIT")
 
print("\n        (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")
 
print("\n  ============================================ Welcome To My Tools ============================================")
pyttsx3.speak("Welcome to my tools")
print("")
print("")
 
pyttsx3.speak("chat with me with your requirements")
 
while True:
    # take input
    print("    CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
    p = input()
    p = p.upper()
    print(p)
 
    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue
 
    # assignements for diffenet applications in the menu
    elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("GOOGLE CHROME")
        print(".")
        print(".")
        os.system("chrome")
 
    elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("8" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EDGE")
        print(".")
        print(".")
        os.system("msedge")
 
    elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("NOTEPAD")
        print(".")
        print(".")
        os.system("Notepad")
 
    elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("5" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("VLC PLAYER")
        print(".")
        print(".")
        os.system("VLC")
 
    elif ("ILLUSTRATOR" in p) or ("AI" in p) or ("6" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("ADOBE ILLUSTRATOR")
        print(".")
        print(".")
        os.system("illustrator")
 
    elif ("PHOTOSHOP" in p) or ("PS" in p) or ("PHOTOSHOP CC" in p) or ("7" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("ADOBE PHOTOSHOP")
        print(".")
        print(".")
        os.system("photoshop")
 
    elif ("TELEGRAM" in p) or ("TG" in p) or ("10" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("TELEGRAM")
        print(".")
        print(".")
        os.system("telegram")
 
    elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EXCEL")
        print(".")
        print(".")
        os.system("excel")
 
    elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT POWERPOINT")
        print(".")
        print(".")
        os.system("powerpnt")
 
    elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT WORD")
        print(".")
        print(".")
        os.system("winword")
 
    # close the program
    elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
        pyttsx3.speak("Exiting")
        break
 
    # for invalid input
    else:
        pyttsx3.speak(p)
        print("Is Invalid,Please Try Again")
        pyttsx3.speak("is Invalid,Please try again")
        print(".")
        print(".")
        """ 
os.start("/Users/rico/Applications/Microsoft\ Excel")