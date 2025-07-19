import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def handleRead(text):
    talk("The value of " + text[0] + " is " + str(text[1]))


def handleWrite(text):
    talk("The value of " + text[0] + " is now set to " + str(text[1]))


class Speech():
    def __init__(self):
        self.listener = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)

    def recognise(self):
        with self.mic as source:
            print("Please give a command:")
            talk("Please give a command")
            audio = self.listener.listen(source)
            try:
                command_text = self.listener.recognize_google(
                    audio, language="en-IN", pfilter=1)  # select recogniser
                return command_text.lower()
            except:
                print("something went wrong in voice recognition")

def getValue(text):
    split_sentence = text.split(' ')

    for value in split_sentence:
        if value.replace('.', '', 1).isdigit():
            return int(value)
            
if __name__ == "__main__":
   x = Speech().recognise()
   print(x)
   x = getValue(x)
   print(x)
   x=int(x)
   Gui.runCommand('Std_ViewGroup',int(x))
#    print(Speech().recognise())