# linux
import os
text = "Enter your Name, Email Address and ID Number. Only valid inputs allow you to play. Age required to play game is 18 and older. You select a set of six numbers and run the game. You're allowed to generate 3 sets. Your selected set is compared to the game's lucky draw. Stand a chance to win ten million rand. If you meet the age requirement, click register. If not, click Exit."
os.system('espeak "{}"'.format(text))

# windows
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.say("Enter your Name, Email Address and ID Number. Only valid inputs allow you to play. Age required to play game is 18 and older. You select a set of six numbers and run the game. You're allowed to generate 3 sets. Your selected set is compared to the game's lucky draw. Stand a chance to win ten million rand. If you meet the age requirement, click register. If not, click Exit.").engine.runAndWait()
