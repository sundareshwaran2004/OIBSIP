
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

print("===== PYTHON VOICE ASSISTANT =====")

engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(message):
    print("Assistant:", message)
    engine.say(message)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening... Please speak.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=7
            )

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please repeat.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
    except OSError:
        speak("Microphone not found. Please check your microphone.")

    return ""

def process_command(command):
    if not command:
        return True

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command or "today" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "search for" in command:
        search_query = command.split("search for", 1)[1].strip()
        if search_query:
            speak("Searching for " + search_query)
            webbrowser.open(
                "https://www.google.com/search?q=" +
                search_query.replace(" ", "+")
            )
        else:
            speak("Please tell me what to search for.")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("Sorry, I don't recognize that command.")

    return True

speak("Voice Assistant started. Say hello to begin.")

while True:
    command = listen()
    if not process_command(command):
        break
