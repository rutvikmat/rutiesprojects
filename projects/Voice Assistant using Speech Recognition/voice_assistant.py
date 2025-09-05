import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for a command from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def process_command(command):
    """Processes the user's command."""
    if 'hello' in command:
        speak("Hello! How can I help you today?")
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif 'date' in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif 'exit' in command or 'bye' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I can't do that yet. Please try another command.")
    return True

if __name__ == '__main__':
    speak("Voice assistant activated.")
    active = True
    while active:
        command = listen()
        if command:
            active = process_command(command)