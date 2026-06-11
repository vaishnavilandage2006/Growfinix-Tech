from datetime import datetime
import webbrowser
import pyttsx3

engine = pyttsx3.init()

command = input("Enter command: ").lower()

if command == "time":
    msg = "Current Time is " + datetime.now().strftime("%H:%M:%S")
    print(msg)
    engine.say(msg)

elif command == "open browser":
    print("Opening Browser")
    engine.say("Opening Browser")
    webbrowser.open("https://www.google.com")

elif command == "play music":
    print("Playing Music")
    engine.say("Playing Music")

else:
    print("Command not recognized")
    engine.say("Command not recognized")

engine.runAndWait()